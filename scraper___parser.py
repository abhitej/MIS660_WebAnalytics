import requests
from bs4 import BeautifulSoup
import re
import time
import requests
import os




def get_tomatometer(loc):
    
    tomato='NA' 
    tomatoChunk=loc.find('span',{'class':re.compile('meter-value superPageFontColor')})
    if tomatoChunk: tomato='Tomatometer: '+tomatoChunk.text.strip()
    
    return(tomato)

   
def get_tomato_avg_rating(loc):
    
    avg_rating='NA' 
    ratingChunk=loc.find('div',{'class':re.compile('superPageFontColor')})
    avg_rating = ratingChunk.text.replace("\n","").strip()

    return(avg_rating)


def get_tomato_reviews_count(loc):
    
    review_text='NA'
    review_value='NA' 
    
    reviewChunk_text=loc.find_all('span',{'class':re.compile('subtle superPageFontColor')})
    reviewChunk_value = loc.find_all("span",{'class':None})
    review_text = reviewChunk_text[1].text.strip()
    #print(review_text)
    review_values = reviewChunk_value[1].text.strip()
   # print(review_value)
    
    if len(review_values) in range (0,6):
        review_value = review_values.zfill(6)
        
    
    
        return(review_text+' '+review_value)
    
def get_tomato_fresh(loc):
    
    fresh='NA' 
    freshChunk_text=loc.find("span",{'class':'subtle superPageFontColor audience-info'})
    freshChunk_value=loc.find_all("span",{'class':None})
    fresh_text = freshChunk_text.text.strip()
    fresh_value = freshChunk_value[2].text.strip()
    if len(fresh_value) in range (1,5):
        fresh = fresh_value.zfill(6)
        return(fresh_text+' '+fresh)
        

  
    
def get_audience_rotten(loc):
    
    rotten='NA' 
    rottenChunk_text=loc.find_all("span",{'class':'subtle superPageFontColor audience-info'})
    rottenChunk_value=loc.find_all("span",{'class':None})
    rotten_text = rottenChunk_text[1].text.strip()
    rotten_value = rottenChunk_value[3].text.strip()
    if len(rotten_value) in range (1,5):
        rotten = rotten_value.zfill(6)
        return(rotten_text+' '+rotten)

    
    
        
    
def get_audience_score(loc):
    
    audience_score='NA' 
    audienceChunk=loc.find('div',{'class':re.compile('meter-value')})
    if audienceChunk: audience_score=audienceChunk.get_text().strip()
    
    return('Audience Rating :' +audience_score)
    
def get_audience_avg_rating(loc):
    
    audience_rating_text='NA'
    audience_rating_value='NA'
    
    audience_ratingChunk = loc.find('div',{'class':re.compile('audience-info hidden-xs superPageFontColor')})
    
        
        
    for span in audience_ratingChunk.find_all("div",{'class':None}):
        #print(span)
        audience_rating = span.text.replace("\n","").strip()
        #print(audience_rating[26:])
        
        audience_rating_text = audience_rating[:15]
       # print(audience_rating_text)
        audience_rating_value = audience_rating[26:32]
        #print(audience_rating_value)
        return(audience_rating_text+' '+audience_rating_value)
    
def get_audience_user_rating(loc):
    
    get_user='NA' 
    user_ratingChunk = loc.find('div',{'class':re.compile('audience-info hidden-xs superPageFontColor')})
    
        
        
    for span in user_ratingChunk.find_all("div",{'class':None}):
        #print(span)
        user_rating = span.text.replace("\n","").strip()
        get_user = user_rating.replace(",","")
        #print(len(get_user))
        
        get_user_text = get_user[:15]
        #print(get_user_text)
        
        get_user_value = get_user[16:]
        #print(len(get_user_value))
        #print(get_user_value)
        
    return(get_user_text+' ' +get_user_value)


###################################################################
    

def get_movie_rating(con):
    
    movie_rating='NA' 
    ratingChunk=con.find('div',{'class':re.compile('meta-value')})
    if ratingChunk: movie_rating=ratingChunk.text.strip()
    
    return(movie_rating)

def get_Genre(con):
    
    genre='NA' 
    genreChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
    genree = genreChunk[1].text.strip()
    genre = genree.replace("\n","").strip()
    return(genre)  

   

def get_Directed(con):
    
    directed='NA' 
    directedChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
    directedd = directedChunk[2].text.strip()
    directed = directedd.replace("\n","").strip()
    
    return(directed)  
    
def get_Written(con):
    
    try:
        
        written='NA'
        exp = 'SOME_EXCEPTION_OCCURED'
        writtenChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
        writtenn = writtenChunk[3].text.strip()
        written = writtenn.replace("\n","").strip()
        return(written)
    except Exception as e:
        return(exp)
    
def get_Theaters(con):
    
    try:
        
        exp = 'SOME_EXCEPTION_OCCURED'
        theatre='NA' 
        theatreChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
        theatree = theatreChunk[4].text.strip()
        theatre = theatree.replace("\n","").strip()
        return(theatre)  
    except Exception as e:
        return(exp)
        
def get_Streaming(con):
    
    try:
        
        exp = 'SOME_EXCEPTION_OCCURED'
        streaming='NA' 
        streamingChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
        streamingg = streamingChunk[5].text.strip()
        streaming = streamingg.replace("\n","").strip()
    
        return(streaming) 
    except Exception as e:
        return(exp)
    
def get_Box_Office(con):
    try:
        
        box='NA'
        exp = 'SOME_EXCEPTION_OCCURED'
        boxChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
        boxx = boxChunk[6].text.strip()
        box = boxx.replace("\n","").strip()
        return(box)
    except Exception as e:
        return(exp)
    #return(box)
    
def get_Runtime(con):
    try:
        
        runtime='NA'
        exp='SOME_EXCEPTION_OCCURED'
        runtimeChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
    
        runtimee = runtimeChunk[7].text.strip()
        runtime = runtimee.replace("\n","").strip()
        return(runtime)
    except Exception as e:
        return(exp)     
        
    #return(runtime)  

   
def get_Studio(con):
    try:
        
        studio='NA'
        exp='SOME_EXCEPTION_OCCURED'
        studioChunk=con.find_all('li',{'class':re.compile('meta-row clearfix')})
        studioo = studioChunk[8].text.strip()
        studio = studioo.replace("\n","").strip()
        return(studio)
    except IndexError as e:
        return(exp)         
        #print('EXCEPTION')
    #return(studio)  
    
    


####################################################################################

def get_movie_data(url):
    
    
    count = 0
    fw=open('reviews.txt','w')
    content=open('content.txt','w')
    
    

    

    for movie in open('movies.txt','r'):
        
        nn = movie.split('/')
        final = nn[2]
#        final = (str(nn).replace("_"," "))
        finals = final.replace("\n"," ")
        #content.write(finals)
        
        count = count+1
        
        
        page = 'https://www.rottentomatoes.com'+movie
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        response = requests.get(page, headers=headers)
        contents = response.content

        soup = BeautifulSoup(contents.decode('ascii', 'ignore'),'lxml')

        reviews=soup.find_all('div', {'class':re.compile('score_panel col-sm-17 col-xs-15')})
        
        for loc in reviews:
            

            tomato           = get_tomatometer(loc)
            avg_rating       = get_tomato_avg_rating(loc)
            review_count     = get_tomato_reviews_count(loc)
            fresh            = get_tomato_fresh(loc)
            rotten           = get_audience_rotten(loc)
            audience_score   = get_audience_score(loc)
            audience_rating  = get_audience_avg_rating(loc)
            user_rating      = get_audience_user_rating(loc)

            
        fw.write(tomato+'\t'+avg_rating+'\t'+review_count+'\t'+fresh+'\t'+rotten+'\t'+audience_score+'\t'
                     +audience_rating+'\t'+user_rating+'\t'+finals+'\n')
        
        print('Details written :'+str(count))
        
        content_body=soup.findAll('ul', {'class':re.compile('content-meta info')})
        
        for con in content_body:


            movie_rating =  get_movie_rating(con)
            genre        =  get_Genre(con)
            director     =  get_Directed(con)
            writer       =  get_Written(con)
            theatre      =  get_Theaters(con)
            stream       =  get_Streaming(con)
            box          =  get_Box_Office(con)
            run          =  get_Runtime(con)
            studio       =  get_Studio(con)
            
            
        content.write(finals+'\t'+movie_rating+'\t'+genre+'\t'+director+'\t'+writer+'\t'+theatre+'\t'+stream+'\t'+box+'\t'+run+'\t'+studio+'\n') # write to file 
		
        print('Content written :'+str(count))


    fw.close()  
    content.close() 
       
if __name__=='__main__':
    url='movie'
    get_movie_data(url)
    

