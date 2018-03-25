#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:29:53 2018

@author: ugandhara
"""

from bs4 import BeautifulSoup
import re
import time
import requests

def moviename_url(path):
    mivieurls={} # new dictionary. Maps each word to each frequency 
 
    # this file has UTF-8 encoding issues so use following code to read instead just open
    with open(path, encoding="latin-1") as fin:
    
        for line in fin: # read the file line by line   
            words=line.strip().split('\t')
            mivieurls[words[1]]=words[0]          
    fin.close() #close the connection to the text file 

    return mivieurls


def run(url):
    urls = moviename_url('reviews.txt')

    fw=open('ratings.txt','w') # output file
    
    count =0
    for movie,murl in urls.items(): # for each page 
        count +=1
        #print("movie:"+murl)
        html=None
        pageLink=url+murl # make the page url
        #print(pageLink)
        
        	
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
        
        criticrscore,audiencescore,rating='NA','NA','NA' # initialize critic and text 
        
        ### crtic review details
        ##### tomoto meter
        tomatometer=soup.find('span', {'class':'meter-value superPageFontColor'}) # get tomoto meter reading
        if tomatometer:
            criticrscore=tomatometer.text#.encode('ascii','ignore')
            #print("criticrscore:"+criticrscore)
            
  

        ### audian review details       
        audience=soup.find('span', {'class':'superPageFontColor','style':'vertical-align:top'}) # get tomoto meter reading
        if audience:
            audiencescore=audience.text#.encode('ascii','ignore')
            #print("audiencescore:"+audiencescore.strip())

        ### Rating      
        ratings=soup.find('li', {'class':'meta-row clearfix'})# get tomoto meter reading 
        if ratings:
            ratingChunk=ratings.find('div',{'class':'meta-value'})
        if ratingChunk:
            rating= ratingChunk.text
        #print(rating)
            
        fw.write(movie+'\t'+criticrscore+'\t'+audiencescore+'\t'+rating+'\n') # write to file 
        print(count)                
        
        if(count == 100):
            fw.close()
            break
            
        '''
        for review in reviews:

            critic,text='NA','NA' # initialize critic and text 
            criticChunk=review.find('a',{'href':re.compile('/critic/')})
            if criticChunk: critic=criticChunk.text#.encode('ascii','ignore')

            textChunk=review.find('div',{'class':'the_review'})
            if textChunk: text=textChunk.text#.encode('ascii','ignore')	
            fw.write(critic+'\t'+text+'\n') # write to file 
		'''
        

    fw.close()

if __name__=='__main__':
    url='https://www.rottentomatoes.com'
    run(url)


