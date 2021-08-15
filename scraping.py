import requests
from bs4 import BeautifulSoup
import csv
website_url="https://infopark.in/companies/jobs/kochi-phase-2?"
key_words=["python"]
res=requests.get(website_url)

soup=BeautifulSoup(res.text,'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})

for job in jobs:
   title_element= job.find("a")
   title=title_element.text.strip()
   link=title_element["href"]
   company_name=job.find("div",{"class":"jobs-comp-name "})
   post_date=job.find("div",{"class":"job-date "})
   if any(word.lower() in title.lower() for word in key_words):

        print (title_element.text.strip())
