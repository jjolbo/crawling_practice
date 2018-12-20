import requests
req = requests.get('https://www.naver.com')
html = req.text

f = open('naver.html', 'w+')
f.write(html)
f.close()