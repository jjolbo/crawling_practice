import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://music.bugs.co.kr/chart')
soup = bs(res.text, 'html.parser')


css_selector = 'p.title > a'

for i in soup.select(css_selector):
    blank_있는_sting = i.text
    중간_blank_없는_string = ' '.join(blank_있는_sting)
    print(중간_blank_없는_string)
    print(i['href'])
print(f"전체개수:{len(soup.select(css_selector))}")