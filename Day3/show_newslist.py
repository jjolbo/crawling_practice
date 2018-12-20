import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://www.naver.com/')
# print('동성제약' in res.text)

soup = bs(res.text, 'html.parser')

# print(soup.select('span.ah_k'))


# soup.select():  soup 해서 가져온 부분을 select 해주는 함수
# span.txt_issue: span 태그의 클래스를 가져오는 부분
# a.ca_a

for value in soup.select('a.ca_a'):
    print(value.text)