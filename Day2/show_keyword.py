import requests
from bs4 import BeautifulSoup as bs

res = requests.get('http://www.daum.net')
# print('동성제약' in res.text)

soup = bs(res.text, 'html.parser')

# print(soup.select('span.ah_k'))


# soup.select():  soup 해서 가져온 부분을 select 해주는 함수
# span.txt_issue: span 태그의 클래스를 가져오는 부분


v = 0
for value in soup.select('span.txt_issue'):
    if v % 2:
        print(value.text)
    v += 1

# 다음 시간부터는 크롤링 하니까 늦지 않기!! 다음주 화요일 수요일정도부터 크롤링한 데이터 분석하기
# 늦으면 크리스마스 다음날부터 진행할듯

