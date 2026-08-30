import requests
from bs4 import BeautifulSoup
import time
import random
import json
import os

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_novel_links(list_url, page=1):
    if page == 1:
        url = list_url                     # 第 1 页不带 ?page=
    else:
        url = f"{list_url}?page={page}"    # 第 2 页起带 ?page=N
    resp = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")
    novels = []
    for a in soup.select('a[href^="/novel/"]'):
        novels.append((a.text.strip(), a.get("href")))
    return novels

def get_read_path(novel_url):
    """从详情页找到"开始阅读"的 /book/ 链接"""
    resp = requests.get(novel_url, headers=HEADERS)
    soup = BeautifulSoup(resp.text, "html.parser")
    a = soup.select_one('a.btn_yuedu')   # 只挑"开始阅读"按钮(class 是 btn_yuedu)
    return a.get("href") if a else None

def get_chapter(read_url, retries=3):
    for attempt in range(retries):
        try:
            resp = requests.get(read_url, headers=HEADERS)
            soup = BeautifulSoup(resp.text, "html.parser")

            # 章节标题
            title_el = soup.select_one(".j_chapterName")
            title = title_el.text.strip() if title_el else ""

            # 正文:<p> 段落之间用 \n 连接
            div = soup.select_one(".read-content")
            content = ""
            if div:
                content = div.get_text("\n", strip=True)

            # 下一章
            next_a = soup.select_one("#j_chapterNext")
            next_path = next_a.get("href") if next_a else None

            return title, content, next_path
        except Exception as e:
            print(f"  第 {attempt+1} 次失败: {e}")
            if attempt == retries - 1:
                raise
            time.sleep(5 * (attempt + 1))   # 退避:5秒、10秒……

list_url = "https://www.alicesw.com/lists/21.html"
LIST_FILE = "novels.json"

# 先试着从缓存读;读不到(第一次跑)才重新抓
try:
    with open(LIST_FILE, "r", encoding="utf-8") as f:
        all_novels = json.load(f)
    print(f"从缓存读取 {len(all_novels)} 本")
except FileNotFoundError:
    all_novels = []
    page = 1
    while True:
        novels = get_novel_links(list_url, page)
        if not novels:
            break
        all_novels.extend(novels)
        page += 1
        time.sleep(random.uniform(1, 2))

    with open(LIST_FILE, "w", encoding="utf-8") as f:
        json.dump(all_novels, f, ensure_ascii=False)
    print(f"抓取完成,已缓存 {len(all_novels)} 本")

BASE = "https://www.alicesw.com"
os.makedirs("novels", exist_ok=True)


for title, novel_url in all_novels:
    try:
        read_path = get_read_path(BASE + novel_url)
        if read_path is None:
            print(f"{title}: 没找到阅读链接,跳过")
            continue

        chapters = []
        while read_path is not None:
            chapter_title, content, next_path = get_chapter(BASE + read_path)
            chapters.append(f"{chapter_title}\n{content}")
            read_path = next_path
            time.sleep(random.uniform(1, 2))

        filename = title.replace("/", "_").replace("\\", "_").replace(":", "_").replace("*", "_").replace("?", "_")
        with open(f"novels/{filename}.txt", "w", encoding="utf-8") as f:
            f.write("\n\n".join(chapters))
        print(f"已保存: {filename}.txt ({len(chapters)} 章)")
    except Exception as e:
        print(f"❌ {title}: 下载失败,跳过: {e}")
