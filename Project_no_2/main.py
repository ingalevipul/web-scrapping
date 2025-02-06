#import
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
url = "https://www.themoviedb.org/movie"
base_url = "https://www.themoviedb.org"
main_url="/movie?page="
index=1
movie_info = {}
info_lst = []
#url list for pages to be scrapped
url_list=[]
for number in range(1,60):
     url_list.append(base_url+main_url+str(number))


#scrapping each link in list
for link in url_list:
    doc = requests.get(link, headers=header).text
    soup = BeautifulSoup(doc, "lxml")
    section = soup.find('section', class_="panel results")
    main_div = section.find_all('div', class_="card style_1")
    #extracting data
    for div in main_div:
        #for creating list of movies info with only 1000 records
        if(index<=1000):
            #movie name ,release dat,url,rating
            movie_div = div.find('div', class_="content")
            movie_name = movie_div.find('a').text
            release_date = movie_div.find('p').text
            sub = div.find("div", class_="outer_ring")
            rating_div = sub.find("div")
            rating = rating_div["data-percent"]
            movie_anchor = movie_div.find('a')
            sub_url = movie_anchor['href']
            url_movie = base_url + sub_url
            #movie runtime,director,genres

            docment = requests.get(url_movie, headers=header).text
            movie_soup = BeautifulSoup(docment, 'lxml')
            genre_span = movie_soup.find('span', class_="genres")
            runtime_span = movie_soup.find('span', class_="runtime")
            #for movies with no runtimee
            if(runtime_span==None):
                runtime="Not defined"
            else:
                runtime=runtime_span.text.strip()
           

            profiles = movie_soup.find_all('li', class_="profile")
            for item in profiles:
                li_class = item.find('p', class_="character")
                current_profile = item.find('a')
                if ("Director" in li_class.text):
                    break
            genre_tag= genre_span.find_all('a')
            genre_lst=[]
            for category in genre_tag:
                genre_lst.append(category.text)
            #converting list to string of genre of movies
            genre=",".join(genre_lst)
            #add key and values in dict
            movie_info = {
            "Name": movie_name,
            "Rating": rating,
            "Genre": genre,
            "Release Date": release_date,
            "Runtime":runtime,
            "Director": current_profile.text,
            "URL": url_movie
            }
            #creating list of dicts
            info_lst.append(movie_info)
        index+=1

#creating dataframe for list of movie information
df=pd.DataFrame(info_lst)
#converting dataframe to csv file
df.to_csv("Movie_Data.csv")