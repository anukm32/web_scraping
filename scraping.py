import requests
from bs4 import BeautifulSoup
website_url="https://infopark.in/companies/jobs/kochi-phase-2?"
res=requests.get(website_url)
print(res.text)
soup=BeautifulSoup(res.text,'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})
print(jobs)
for job in jobs:
   title_element= job.find("a")
   title=title_element.text
   link=title_element["href"]
   print(title,link)


