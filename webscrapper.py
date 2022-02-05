import requests
from bs4 import BeautifulSoup

request=requests.get("https://www.investopedia.com/articles/investing/012715/5-richest-people-world.asp")
data=request.content
# print(data)

soup=BeautifulSoup(data, "html.parser")

# print(soup.prettify)

richest=soup.find_all("div", {"@type": "ListItem"})
print(richest)

# id="mntl-toc__list_1-0"