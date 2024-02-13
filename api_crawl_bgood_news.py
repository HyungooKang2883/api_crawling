import requests
from bs4 import BeautifulSoup as bs

# 비굿 뉴스 검색결과 추출하기

html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%B9%84%EA%B5%BF&oquery=%EB%AA%BB%EB%82%9C%EC%9D%B4%EB%86%8D%EC%82%B0%EB%AC%BC&tqi=iNVN9wqps8wssNWvlECssssstVK-479990')
soup = bs(html.text, 'html.parser') # 검색 결과 html로 저장
# print(soup)

articles = soup.select('.list_news > li')
# print(articles)

# 기사 제목 / 해당 링크 가져오기
title = soup.select_one('.news_tit').text
link = soup.select_one('.news_tit')['href']
# print(title)
# print(link)

# 제목 / 링크 리스트로 가져오기
for article in articles:
    title = article.select_one('.news_tit').text
    url = article.select_one('.news_tit')['href']
    print(title, end=' ')
    print(url)