import requests

r=requests.get("https://xkcd.com/353/")

print(r)      # here we checked its status
print(dir(r))  # its tell what can i do with this response
print(help(r)) # its give more details explanaation of object r

