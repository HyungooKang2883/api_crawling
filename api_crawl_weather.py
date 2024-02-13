from bs4 import BeautifulSoup as bs
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# print(html.text) # 사이트 html 전체 불러오기

soup = bs(html.text, 'html.parser') # beautifulsoup4 이용하여 html
# print(soup)

data1 = soup.find('div', {'class':'weekly_forecast_area'}) # div태그의 class속성, weekly_forecast_area의 속성값 가져오기
# print(data1)

data2 = data1.findAll('strong') # strong 태그를 가진 html 불러오기
# print('data2:', data2)

needed_data = data2[0].text # .text를 활용하여 태그 안의 내용만 가져오기
# print('what is needed_data:', needed_data)

