import requests

req = requests.get('http://naver.com')

# dir(객체) 내장함수는 객체 내부의 함수나 객체를 리스트로 알려줍니다.
print(dir(req))
print(req.headers)
print(req.url)
print(req.ok)
print(req.history)
print(req.status_code)

# lxml 패키지: parser보다 더 빠름
