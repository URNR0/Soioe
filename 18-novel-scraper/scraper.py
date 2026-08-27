import requests
from bs4 import BeautifulSoup
import time
import random
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_chapter_links(book_url):
    
    resp = requests.get(book_url, headers=HEADERS)
    resp.encoding = "gbk"
    soup = BeautifulSoup(resp.text, "html.parser") #html解析为对象

    return [a.get("href") for a in soup.select("#list dd a")]

def get_chapter(chapter_url, retries=3):
    for attempt in range(retries):         
        try:
            resp = requests.get(chapter_url, headers=HEADERS)
            resp.encoding = "gbk"
            soup = BeautifulSoup(resp.text, "html.parser")
            title = soup.select(".bookname h1")[0].text.strip()
            content = soup.select("#content")[0].text
            content = content.replace("\xa0", " ")
            return title, content        
        except Exception as e:
            print(f"  第 {attempt+1} 次尝试失败: {e}")
            if attempt == retries - 1:       
                raise                        
            time.sleep(5 * (attempt + 1))    

def download_novel(book_url, output_file='大主宰.txt'):
    domain = '/'.join(book_url.split('/')[:3])  
    chapters = get_chapter_links(book_url)

    with open(output_file, 'w', encoding='utf-8') as f:

        for i, chapter in enumerate(chapters, 1):
            time.sleep(random.uniform(1, 3))  #随机延迟
            full_url = domain + chapter
            try:
                title, content = get_chapter(full_url)
            except Exception as e:
                print(f"第{i}章失败，跳过: {e}")
                continue

            f.write(f"\n\n{title}\n")
            f.write('=' * 50 + '\n')
            f.write(content + "\n")

            if i % 50 == 0:      
                print(f"已下载 {i}/{len(chapters)} 章")
    
    print(f"已保存到 {output_file}")

book_url = "https://www.8tsw.com/0_1/"
download_novel(book_url)
