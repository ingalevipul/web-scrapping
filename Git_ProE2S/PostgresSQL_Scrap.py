import pandas as pd
from bs4 import BeautifulSoup
import requests as re
base_url="https://github.com"
url_list=[]
url=base_url+"/topics/postgresql?page="
for i in range(1,8):
   url_list.append(url+str(i))
Sr_NO=1
Github_info={}
all_info=[]

for url_link in url_list:
    doc=re.get(url).text
    html_data=BeautifulSoup(doc,"html.parser")
    main_div=html_data.find('div',class_="col-md-8 col-lg-9")
    all_articles=main_div.find_all('article',class_="border rounded color-shadow-small color-bg-subtle my-4")
    for item in all_articles:
      if(Sr_NO<=200):
         sub_div=item.find('div',class_="d-flex flex-auto")
         h3=sub_div.find('h3',class_="f3 color-fg-muted text-normal lh-condensed")
         Contri=h3.find('a').text.replace("\n","").strip()
         respo=h3.find('a',class_="text-bold wb-break-word").text.replace("\n","").strip()
         rating_span=item.find('span',class_="Counter js-social-count").text
         repo_url=f"{base_url}/{Contri}/{respo}"
  
         Github_info={
         "SR NO":Sr_NO,
         "Username":Contri,
         "Repository Name":respo,
         "Rating":rating_span,
         "URL":repo_url
       }
         all_info.append(Github_info)
      Sr_NO+=1

df=pd.DataFrame(all_info)
df.to_excel("PostgresSQL_DATA.xlsx")