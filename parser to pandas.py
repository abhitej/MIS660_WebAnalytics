# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:43:15 2018

@author: Abhitej Kodali
"""

from bs4 import BeautifulSoup
import pandas as pd
import os
#import datetime

def movie_extract(records, file):
    soup = BeautifulSoup(file,'html.parser')
    
    movie_rat = 'NA'
    movie_studio = 'NA'
    movie_genre = 'NA'
    movie_boxoffice = 0
    movie_release = 'NA'
    movie_runtime = 'NA'
    movie_director = 'NA'
    movie_writer = 'NA'
    aud_score = 0
    avg_crit_rat = 0
    tomatometer = 0
    avg_aud_rat = 0.
    user_aud_rat = 0
    fresh_crit_rat = 0
    rotten_crit_rat = 0
    movie = 'NA'
    
    #Movie Title
    try:
        movie = soup.find('h1',{'id':'movie-title'}).text.replace("\n","").strip('\n').strip()
    except:
        movie = 'NA'
    
    #Tomato-meter Score
    try:
        tomatometer = int(soup.find('span',{'class':'meter-value superPageFontColor'}).text.replace("%","").strip())
    except:
        tomatometer = 0
    
    a = soup.find_all('div',{'class':'superPageFontColor'})
    a_1 = soup.find('div',{'class':'critic-score meter'})
    if a_1:
        if 'Rating' in a[0].text:
            a1 = a[0].text.replace("Average Rating:","").replace("\n","").replace("\\n","").strip().split('/')
            if isinstance(float(a1[0]),float):
                avg_crit_rat = float(a1[0])/10
        if 'Fresh' in a[2].text:
            fresh_crit_rat = int(a[2].text.replace("Fresh:","").replace("\n","").replace("\\n","").strip())
        if 'Rotten' in a[3].text:
            rotten_crit_rat = int(a[3].text.replace("Rotten:","").replace("\n","").replace("\\n","").strip())
    
    reviews_crit_count = fresh_crit_rat + rotten_crit_rat
    
    #Audiene metrics - Popcornmeter
    b = soup.find('div',{'class':'audience-score meter'})
    
    try:
        aud_score = int(b.text.replace("\n","").replace("liked it","").replace("\\n","").replace("%","").strip())
    except:
        aud_score = 0
    try:
        b1 = soup.find('div',{'class':'audience-info hidden-xs superPageFontColor'}).text.replace(",","").replace("\\n","").strip().split()
        b2 = b1[2].split('/')
        if b2[0]!='N':
            avg_aud_rat = float(b2[0])/5
        user_aud_rat = int(b1[5])
    except:
        avg_aud_rat = 0.
        user_aud_rat = 0
    
    #Movie Info
    c1 = soup.find_all('div',{'class':'meta-value'})
    c2 = soup.find_all('div',{'class':'meta-label subtle'})
    
    for c in range(len(c2)):
        if c2[c].text.strip() == 'Rating:':
            movie_rat = c1[c].text.strip()
        elif c2[c].text.strip() == 'Studio:':
            movie_studio = c1[c].text.replace("\n","").strip('\n').strip()
        elif c2[c].text.strip() == 'Runtime:':
            movie_runtime = c1[c].text.replace("\n","").strip()
        elif c2[c].text.strip() == 'Box Office:':
            movie_boxoffice = int(c1[c].text.replace(",","").replace("$","").strip())
        elif c2[c].text.strip() == 'In Theaters:':
            c3 = c1[c].text.replace(",","").replace("Wide","").replace("\n","").replace("\\n","").replace("limited","").replace("wide","").strip()
            movie_release = c3.replace("\xc2\xa0","").strip()
        elif c2[c].text.strip() == 'Directed By:':
            movie_director = c1[c].text.replace("\n","").strip()
        elif c2[c].text.strip() == 'Written By:':
            movie_writer = c1[c].text.replace("\n","").strip()
        elif c2[c].text.strip() == 'Genre:':
            c3 = c1[c].text.strip().replace("\n","").split()
            movie_genre = " ".join(c3)
        else:
            continue
       
    records.append((movie,tomatometer,aud_score,avg_aud_rat,user_aud_rat,avg_crit_rat,reviews_crit_count,
                    fresh_crit_rat,rotten_crit_rat,movie_rat,movie_studio,movie_director,movie_writer,
                    movie_genre,movie_runtime,movie_release,movie_boxoffice))
    
    return records

if __name__=='__main__':
    records = []
    directory = os.path.normpath("C:/Users/Abhitej Kodali/Google Drive/BIA 660 Team Project/Samuel Workspace/Full Scraped Movie Pages/MoviePages")
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                f=open(os.path.join(subdir, file),'r')
                a = f.read()
                if 'movie-title' in a:
                    records = movie_extract(records, a)
                    f.close()
                else:
                    f.close()
                    continue
    
    movie_list = pd.DataFrame(records,columns=['Movie','Tomatometer','Audience_score','Audience_average_rating',
                                               'Audience_user_rating','Critic_average_rating','Critic_reviews_count',
                                               'Critic_fresh_rating','Critic_rotten_rating','Movie_rating',
                                               'Studio','Director','Writer','Genre','Runtime','Release_date',
                                               'Box_office'])
    movie_list = movie_list.replace(r'\\n','',regex=True)
    
    print(movie_list.head())
    movie_list.to_csv("C:/Users/Abhitej Kodali/Google Drive/BIA 660 Team Project/Abhitej Workspace/Full Movie List.csv", encoding='utf-8')
    