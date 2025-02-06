from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import requests


driver=webdriver.Chrome()
base_url="https://www.trustpilot.com/categories/bars_cafes"
load_more_url="?page="
info_list=[]

for i in range(1,4):
    driver.get(base_url+load_more_url+str(i))
    html_data=requests.get(base_url+load_more_url+str(i))
    doc=BeautifulSoup(html_data.text,"lxml")
    pass_click=driver.find_element(By.CSS_SELECTOR,"h1[class='typography_typography__23IQz typography_h1__3CI-9 typography_weight-regular__iZYoT typography_fontstyle-normal__1_HQI styles_categoryBusinessHeaderTitleMobile__2VVI9']")
    driver.execute_script("arguments[0].click();",pass_click)
    driver.execute_script("window.scrollTo(0, window.scrollY + 290)")
    btn_index=0
    
    buttons=driver.find_elements(By.CSS_SELECTOR,"button[class='styles_iconWrapper__3Rp-n']")
    info_cards=doc.find_all('div',class_="paper_paper__29o4A card_card__2F_07 card_noPadding__1tkWv styles_wrapper__2QC-c styles_businessUnitCard__1-z5m")
    for items in info_cards:
        if(btn_index<len(buttons)):
            
            name=items.find('p',class_="typography_typography__23IQz typography_h4__IhMYK typography_weight-heavy__36UHe typography_fontstyle-normal__1_HQI styles_displayName__1LIcI")
            score_span=items.find('span',class_="typography_typography__23IQz typography_bodysmall__24hZa typography_weight-regular__iZYoT typography_fontstyle-normal__1_HQI styles_trustScore__nLHX2")
            if(score_span==None):
                TrustScore="-"
            else:
                TrustScore=score_span.text.replace("TrustScore","")
            reviews_span=items.find('span',class_="styles_ratingSeparator__30CX7")
            if(reviews_span==None):
                total_reviews="-"
            else:
                total_reviews=reviews_span.nextSibling
            if(i>1):
                driver.execute_script("window.scrollTo(0, window.scrollY + 170)")
            else:
                driver.execute_script("window.scrollTo(0, window.scrollY + 190)")
            driver.execute_script("arguments[0].click();",buttons[btn_index])
            li_lst=driver.find_elements(By.CSS_SELECTOR,"li[class='styles_item__3UwLI']")
            if(not len(li_lst)==2):
                address="--"
                website="www."+li_lst[0].text
            else:
                website="www."+li_lst[0].text
                address=li_lst[1].text.replace(" · ",",")
            info_dict={
                "Name":name.text,
                "Trust Score":TrustScore,
                "Total reviews":total_reviews,
                "Website Name":website,
                "Loaction":address
            }
            info_list.append(info_dict)
        btn_index+=1
driver.close()
df=pd.DataFrame(info_list).drop_duplicates(keep='first',ignore_index=True)
df.to_excel("Bars_Cafe_DATA.xlsx")   