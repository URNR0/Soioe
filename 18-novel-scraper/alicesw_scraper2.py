"""
alicesw_scraper 的改进版,相比 v1 的变化:
1. 每抓一章就追加写入文件(断点不丢数据);文件已存在的书直接跳过
2. 用 visited 集合防"下一章"链接死循环
3. 用 urllib.parse.urljoin 拼接 URL,不再手动字符串相加
4. 所有请求统一走 fetch():raise_for_status() 让 404/500 真正触发重试
5. 全局 requests.Session():复用连接,头部只设一次
6. 文件名清洗覆盖全部 Windows 非法字符,重名靠链接尾巴保证唯一
7. 类型注解 + @retry 装饰器(把重试逻辑从业务函数里抽出来)
"""
import requests
from bs4 import BeautifulSoup
import time
import random
import json
import os
import re
from urllib.parse import urljoin


BASE = "https://www.alicesw.com"
LIST_URL = "https://www.alicesw.com/lists/21.html"
LIST_FILE = "novels.json"
LIMIT = 50          # 只下载前 50 本;全量下载改成None

# Session 全局只用一个:TCP 连接自动复用(更快、对服务器更礼貌),
# 头部在这里设一次,后面所有请求都不用再传 headers=
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})


def retry(times: int = 3, delay: float = 5.0):
    """重试装饰器:v1 里 get_chapter 的重试循环,现在任何函数都能套用"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == times - 1:
                        raise                     # 最后一次仍失败:抛出去,由外层决定跳过
                    wait = delay * (attempt + 1)  # 退避:5 秒、10 秒……
                    print(f"  第 {attempt+1} 次失败: {e},{wait} 秒后重试")
                    time.sleep(wait)
        return wrapper
    return decorator


def fetch(url: str) -> BeautifulSoup:
    """统一的请求入口:发请求 + 检查状态码 + 解析。

    v1 的问题:requests.get 对 404/500 页面不报错,而是返回一个装着
    错误页的 resp,BeautifulSoup 在里面什么也找不到,悄悄返回空结果。
    raise_for_status() 让这类失败真正抛出异常,重试才有意义。
    """
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # 网站限流时返回 HTTP 200 的"提示信息"页,和错误页一样要当成失败处理
    if soup.title and soup.title.get_text(strip=True) == "提示信息":
        m = re.search(r'let msg = "(.*)"', resp.text)
        raise RuntimeError(f"被网站限流: {m.group(1) if m else '访问异常'}")

    return soup


def get_novel_links(list_url: str, page: int = 1) -> list[tuple[str, str]]:
    url = list_url if page == 1 else f"{list_url}?page={page}"
    soup = fetch(url)
    novels = []
    for a in soup.select('a[href^="/novel/"]'):
        novels.append((a.text.strip(), a.get("href")))
    return novels


@retry()
def get_read_path(novel_url: str) -> str | None:
    """从详情页找到"开始阅读"的 /book/ 链接"""
    a = fetch(novel_url).select_one("a.btn_yuedu")
    return a.get("href") if a else None


@retry()
def get_chapter(read_url: str) -> tuple[str, str, str | None]:
    soup = fetch(read_url)

    # 章节标题
    title_el = soup.select_one(".j_chapterName")
    title = title_el.text.strip() if title_el else ""

    # 正文:<p> 段落之间用 \n 连接
    div = soup.select_one(".read-content")
    content = div.get_text("\n", strip=True) if div else ""

    # 下一章(javascript: 开头的"假链接"当成没有下一章)
    next_a = soup.select_one("#j_chapterNext")
    next_path = None
    if next_a:
        href = next_a.get("href")
        if href and not href.startswith("javascript"):
            next_path = href

    return title, content, next_path


def sanitize_filename(title: str, href: str) -> str:
    """清洗 Windows 文件名非法字符;再拼上链接尾巴(如 123.html)防重名覆盖"""
    for ch in '\\/:*?"<>|':
        title = title.replace(ch, "_")
    tail = href.rstrip("/").split("/")[-1]
    return f"{title}_{tail}"


def load_or_fetch_list() -> list[tuple[str, str]]:
    """有缓存读缓存,没有才逐页抓列表页"""
    try:
        with open(LIST_FILE, "r", encoding="utf-8") as f:
            all_novels = json.load(f)
        print(f"从缓存读取 {len(all_novels)} 本")
        return all_novels
    except FileNotFoundError:
        pass

    all_novels = []
    page = 1
    while True:
        novels = get_novel_links(LIST_URL, page)
        if not novels:
            break
        all_novels.extend(novels)
        page += 1
        time.sleep(random.uniform(1, 2))

    with open(LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(all_novels, f, ensure_ascii=False)
    print(f"抓取完成,已缓存 {len(all_novels)} 本")
    return all_novels


def download_novel(title: str, novel_url: str) -> None:
    read_path = get_read_path(urljoin(BASE, novel_url))
    if read_path is None:
        print(f"{title}: 没找到阅读链接,跳过")
        return

    filepath = os.path.join("novels", sanitize_filename(title, novel_url) + ".txt")
    if os.path.exists(filepath):
        print(f"跳过(已存在): {filepath}")
        return

    visited: set[str] = set()   # 防死循环:网站若把"下一章"错误指向旧章节,立刻停
    chapter_count = 0
    while read_path is not None:
        full_url = urljoin(BASE, read_path)   # 自动处理相对/绝对路径
        if full_url in visited:
            print("  ⚠️ 检测到重复的章节链接,提前停止")
            break
        visited.add(full_url)

        chapter_title, content, next_path = get_chapter(full_url)

        # 第一章用 "w" 创建文件,之后用 "a" 追加——
        # 这样中途断了,已下载的章节也都在磁盘上
        mode = "w" if chapter_count == 0 else "a"
        with open(filepath, mode, encoding="utf-8") as f:
            f.write(f"{chapter_title}\n{content}\n\n")
        chapter_count += 1

        read_path = next_path
        time.sleep(random.uniform(1, 2))

    print(f"已保存: {filepath} ({chapter_count} 章)")


def main() -> None:
    all_novels = load_or_fetch_list()
    if LIMIT is not None:                 # [:None] 恰好等于全量,所以统一走切片
        all_novels = all_novels[:LIMIT]
    os.makedirs("novels", exist_ok=True)

    for title, novel_url in all_novels:
        try:
            download_novel(title, novel_url)
        except Exception as e:
            print(f"❌ {title}: 下载失败,跳过: {e}")


if __name__ == "__main__":
    main()
