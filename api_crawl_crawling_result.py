import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/section/101'
# print(url)

html = requests.get(url)
# print(html)

soup = BeautifulSoup(html.text, 'html.parser')
# print(soup)

articles = soup.select('.sa_list')
# print(articles)

for a in articles:
    print(a.select_one('.sa_text_title').text, end=' ')
    print(a.select_one('.sa_text_title')['href'])