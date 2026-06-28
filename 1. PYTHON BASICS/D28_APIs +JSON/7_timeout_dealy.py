import requests

r=requests.get("https://httpbin.org/delay/6",timeout= 10)

print(r)