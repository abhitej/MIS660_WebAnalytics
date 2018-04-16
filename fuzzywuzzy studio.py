# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 21:11:48 2018

@author: Abhitej Kodali
"""

import pandas as pd
from fuzzywuzzy import process, fuzz

names_array=[]
ratio_array=[]
def match_names(wrong_names,correct_names):
    for row in wrong_names:
        x=process.extractOne(row, correct_names, scorer=fuzz.token_set_ratio)
        names_array.append(x[0])
        ratio_array.append(x[1])
    return names_array,ratio_array

df = pd.read_csv("C:/Users/Abhitej Kodali/Google Drive/BIA 660 Team Project/Abhitej Workspace/Full Movie List_v2.csv")
wrong_names = df['Studio'].dropna().values

s = pd.read_csv("C:/Users/Abhitej Kodali/Google Drive/BIA 660 Team Project/Abhitej Workspace/Correct Studio List_v2.csv")
correct_names = s['Correct Studio'].values

name_match,ratio_match=match_names(wrong_names,correct_names)
 
a = pd.DataFrame(wrong_names, columns=['Studio'])
a['correct_studio']=pd.Series(name_match)
a['correct_studio_ratio']=pd.Series(ratio_match)