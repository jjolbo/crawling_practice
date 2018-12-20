import requests
from bs4 import BeautifulSoup as bs

res = requests.get('https://www.daum.net')
soup = bs(res.text, 'html.parser')

css_selector = 'a.link_txt'

for i in soup.select(css_selector):
    blank_있는_sting = i.text
    중간_blank_없는_string = ' '.join(blank_있는_sting)
    print(중간_blank_없는_string)
    print(i['href'])

    # url = i['href'].replace("/list", "/read")
    # # print(url)
    # # res2 = requests.get(url)
    # # soup2 = bs(res2.text, 'html.parser')
    # # print(soup2.select('div > #articleBodyContents')[0].text)

    # print(i['data-clk'])

print(f"전체개수:{len(soup.select(css_selector))}")



# o_url = 'https://media.daum.net/issue/1219577?selectedNewsId=20181220120012122'
#
# new_no = o_url.split('=')[1]
#
# news_url = "http://news.v.daum.net/v/"
#
# print(news_url + new_no)
