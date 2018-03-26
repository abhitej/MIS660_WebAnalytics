# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:16:30 2018

@author: smathew
"""
from bs4 import BeautifulSoup
#import re
import time
#import json
#import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
#from selenium.common.exceptions import StaleElementReferenceException

'''
class text_to_be_not_present_in_element(object):
    """ An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try :
            element_text = EC._find_element(driver, self.locator).text
            return not(self.text in element_text)
        except StaleElementReferenceException:
            return False
'''
def parse_movie_names(url, increment, maxRecord):

    #create dict
#    movie_list = {}
#    movie_list['MovieData']=[]
	# output file (flat file)
    fw=open('MovieList.txt','w') 
    
    driver = webdriver.Firefox()
    driver.get(url)
    # hardcoding the total number of records in the "Browse All" page.
    total_count=maxRecord
    # hardcoding the current number of records in the "Browse All" page.
    current_count=increment
    
    #clicking loop: keep expanding page till it is showing all movies
    elem = driver.find_element_by_xpath('//*[@id="show-more-btn"]/button')
    count=0
    
    while(True):
        
        #if it has finished clicking, break out of while loop
        if(current_count >= (total_count-1)):
            break

        else:
                #continue clicking
#            print('Continue Clicking')
            try:
                elem.click()
                # increment the current count with the default number of movies
                wait = WebDriverWait(driver, 30)
                
                current_count=current_count+increment
                print("Count: " + str(current_count))
                count=count+1
                print("Clicks: "+ str(count))
                wait = wait.until(EC.presence_of_element_located((By.ID,'show-more-btn')))
            except ElementNotVisibleException:
                break
            except TimeoutException:
                break
 
        
    print('Scraping now')
    #record each movie title and its url inside dict
    soup = BeautifulSoup(driver.page_source,"lxml")
    movies = soup.find_all('div', {'class' :"movie_info"})
    
    for movie in movies:

        url=movie.find('a',href=True)['href']
#        title = movie.find('h3',{'class' : 'movieTitle'}).text
        MovieFileName = str(url.split('/m/')[1]) + '.txt'
#        movie_list['MovieData'].append({title : url, 'FileName' : MovieFileName})
        
        # write to file 
        fw.write(url + '\t' + MovieFileName + '\n') 
        
    fw.close()
#    driver.quit()
    
#    with open('movie_urls.txt','w') as file:
#        json.dump(movie_list,file, indent=4)
    
if __name__=='__main__':
    print('Process Started')
    start = time.time()
    url='https://www.rottentomatoes.com/browse/dvd-streaming-all/'
    parse_movie_names(url, 32, 19100)
    end = time.time() - start
    print("Completed, time: " + str(end) + " secs")

