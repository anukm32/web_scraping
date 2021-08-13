import requests
from bs4 import BeautifulSoup
website_url="https://infopark.in/companies/jobs/kochi-phase-2?"
key_words=["python"]
res=requests.get(website_url)
print(res.text)
soup=BeautifulSoup(res.text,'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})

for job in jobs:
   title_element= job.find("a")
   title=title_element.text
   link=title_element["href"]
   company_name=job.find("div",{"class":"jobs-comp-name "}).text
   post_date=job.find("div",{"class":"job-date "}).text
   print(title_element,company_name, post_date)
