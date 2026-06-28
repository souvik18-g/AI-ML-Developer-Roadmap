import requests
payload= {"age":20,"roll":57}
r=requests.get("https://httpbin.org/get", params=payload)
print(r.text)
print(r.url)