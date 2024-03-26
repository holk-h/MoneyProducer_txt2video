from sys import stdout
from typing import Dict, List
import requests
import re
import time
from bs4 import BeautifulSoup


def get_chapter_url_list(book_url: str) -> List[str]:
    """
    根据书籍链接获取全部章节链接列表

    Parameters
    ----------
    book_url : str
        书籍链接

    Returns
    -------
    List[str]
        章节链接列表
    """
    # 匹配章节链接的正则表达式
    href_regex = "<dd><a href='(.*)' >"
    response = requests.get(book_url, headers=headers)
    response.encoding = 'utf-8'
    chapter_href_list = re.findall(href_regex, response.text)
    return [base_url+href for href in chapter_href_list]


def get_chapter_detail(chapter_url: str) -> Dict[str, str]:
    """
    根据章节链接获取章节信息

    Parameters
    ----------
    chapter_url : str
        章节链接

    Returns
    -------
    Dict[str, str]
        章节链接信息
    """
    # 反复尝试获取,直到有正确的信息
    while 1:
        response = requests.get(chapter_url, headers=headers)
        if '503 Service Temporarily Unavailable' not in response.text:
            break
        else:
            print('漏数据了，3 秒之后继续爬')
            time.sleep(3)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # 查找正文内容
    content = soup.find(attrs={'id': 'content'}).text
    # 标题
    title = soup.find('h1').text
    return {
        'content': content,
        'title': title,
        'url': chapter_url
    }


# 网站链接
base_url = 'http://www.xbiquge.la'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',
}
# 要采集的最大章节数
max_chapter_count = 10
# 书籍链接
book_url = 'https://www.xbiquge.la/10/10489/'
# 获取章节列表
chapter_url_list = get_chapter_url_list(book_url)
chapter_url_list = chapter_url_list[:max_chapter_count]
# 存储路径
file_name = 'book.txt'
with open(file_name, 'w', encoding='utf-8') as f:

    for index, chapter_url in enumerate(chapter_url_list, start=1):
        item = get_chapter_detail(chapter_url)
        f.write('标题: '+item['title']+'\n')
        f.write('原文链接: '+item['url']+'\n')
        f.write('正文内容: '+item['content']+'\n')
        stdout.write(f'进度:{index}/{len(chapter_url_list)}\r')
print('生成文件:',file_name)
