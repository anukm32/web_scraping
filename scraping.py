import requests
from bs4 import BeautifulSoup
website_url="https://infopark.in/companies/jobs/kochi-phase-2?"
key_words=["python"]
res=requests.get(website_url)
print(res.text)
soup=BeautifulSoup(res.text,'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})
print(jobs)
for job in jobs:
   title_element= job.find("a")
   company=jobs.find("div",{"class":"jobs-comp-name "})
   post_date=jobs.find("div",{"class":"job-date "}).text
   company_name=company.text
   title=title_element.text
   link=title_element["href"]

   if any(word.lower() in title.lower() for word in key_words):
   
  
     print(title,company_name,post_date)


