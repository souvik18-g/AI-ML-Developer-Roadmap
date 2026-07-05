import requests

r=requests.get("https://xkcd.com/353/")

print(r.text) # its show full html page & show only text form data 