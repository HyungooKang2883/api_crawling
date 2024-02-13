import requests
from bs4 import BeautifulSoup as bs

url = 'https://mania.kr/g2/bbs/board.php?bo_table=news'
html = requests.get(url)
soup = bs(html.text, 'html.parser')
# print(soup)

news = soup.select('.wz_news_row')
news_title = soup.select('.wz_news_subject_a')

print(news_title)

for t in news_title:
    print(t.text)
