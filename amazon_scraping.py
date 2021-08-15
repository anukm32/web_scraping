import requests
from bs4 import BeautifulSoup
url="https://www.amazon.in/Samsung-Galaxy-Space-Black-Storage/dp/B07HGN617M/ref=sr_1_4?dchild=1&keywords=mobile&qid=1628877456&sr=8-4"

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}
res=requests.get(url,headers=headers)

soup=BeautifulSoup(res.content,'html.parser')
title=soup.find(id="productTitle").get_text()

print(title.strip())

price=soup.find(id="desktop_unifiedPrice").get_text()

print(price.strip())
price_convert=float(price)