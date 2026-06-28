import requests

r=requests.get("https://imgs.xkcd.com/comics/python.png")


with open ("comic.png", "wb") as f: # wb stands for write in binary
    f.write(r.content)


print(r.status_code)
print(r.headers)     

