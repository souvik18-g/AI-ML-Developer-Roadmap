# step 0 : install all the requirments
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"
# step 1: get the html
r= requests.get(url)
print(r.status_code)
htmlcontent= r.content
# print(htmlcontent)

# step 2: parse the html
soup= BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify())
#step 3: html tree traversal 

#commonly use types of objects:

#Get the title of the html page
title=soup.title
# print(type(soup))#beautifulsoup
# print(type(title))#tag
# print(type(title.string))#navigablestring

#get the all paragraphs from the page
paras=soup.find_all('p')
# print(paras)


# print(anchor)

#get first element in the html pge
print(soup.find('p'))

#get claasses of any element in the html pge
print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p",class_="lead"))

#get text from the taags/soup
print(soup.find('p').get_text())
print(soup.get_text())

#get the all anchor tags from the page
anchors=soup.find_all('a')
all_links=set()

#get all the link on the page:

for link in anchors:
    href = link.get('href')

    if href != '#':
        all_links.add(href)

print(all_links)

for link in anchors:
    if (link.get('href')!= '#'):
        linkText= "https://codewithharry.com"+link.get('href')
        all_links.add(link)
        print(linkText)





