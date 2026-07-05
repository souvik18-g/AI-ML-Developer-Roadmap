import requests

r=requests.get("https://httpbin.org/basic-auth/souvik/testing",auth= ("souvik","testing"))

print(r)
print(r.json())