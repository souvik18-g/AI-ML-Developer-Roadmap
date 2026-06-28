import requests
payload= {"age":20,"roll":57}
r=requests.post("https://httpbin.org/post", data=payload)
print(r.text)
print(r)
print(r.json())
r_json=r.json()
print(r_json["form"])