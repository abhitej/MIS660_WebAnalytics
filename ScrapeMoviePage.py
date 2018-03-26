# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 21:26:08 2018

@author: smathew
"""
import requests
#import re
import os

def run(url):
   
#    FileName='justice_league_2017.html'
#    FullPath=os.path.join(path+'\MoviePages',FileName)
#    print(FullPath)
#    
    movieurls={} # new dictionary. Maps each word to each frequency 
    path = 'MovieList.txt'
    
    with open(path, encoding="utf-8") as fin:
    
        for line in fin: # read the file line by line   
            words=line.strip().split('\t')
            movieurls["url"]=words[0] 
            movieurls["filename"]=words[1]
            pageLink = url + movieurls["url"]
            print(pageLink)
        
            html=requests.get(pageLink)
            content = html.text.encode('utf-8','ignore')
            filename=movieurls["filename"]
            FullPath=os.path.join(os.getcwd() + '\Pages',filename)
            with open(FullPath,'wb') as fw:
                fw.write(content)
        
        fw.close()
    
    fin.close()
        
if __name__=='__main__':
    url='https://www.rottentomatoes.com'
    run(url)
    
    
 