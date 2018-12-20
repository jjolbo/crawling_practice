import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://www.naver.com')
soup = bs(res.text, 'html.parser')


css_selector = 'a.ca_a'

for i in soup.select(css_selector):
    blank_있는_sting = i.text
    중간_blank_없는_string = ' '.join(blank_있는_sting)
    print(중간_blank_없는_string)
    print(i['href'])
    url = i['href'].replace("/list", "/read")
    print(url)
    res2 = requests.get(url)
    soup2 = bs(res2.text, 'html.parser')
    print(soup2.select('#articleBodyContents')[0].text)

    print(i['data-clk'])

print(f"전체개수:{len(soup.select(css_selector))}")