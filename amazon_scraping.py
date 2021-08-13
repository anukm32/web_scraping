import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGN617M/ref=sr_1_4?dchild=1&keywords=mobile&qid=1628877456&sr=8-4"

res=requests.get(url)

soup=BeautifulSoup(res.content,"lxml")
title=soup.find(id="productTitle").text
print(title)