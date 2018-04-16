# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:18:38 2018

@author: Abhitej Kodali
"""

import pandas as pd
import re


def critic_score_eval(c,df):
    c1 = []
    for i in range(len(c)):
        c2 = re.split('/ |, ',str(c[i]))
        for c3 in c2:
            c1.append(str(c3).strip())
    c4 = {}
    for i in range(len(c1)):
        if c1[i] in c4:
            c4[c1[i]] = c4[c1[i]] + 1
        else:
            c4[c1[i]] = 1
    c5 = {}
    for i in c4:
        a = 0
        b = 0
        for y in range(len(c)):
            if i in str(c[y]):
                a = a + (df.loc[y,'Critic_average_rating']*df.loc[y,'Critic_reviews_count'])
                b = b + df.loc[y,'Critic_reviews_count']
                c5[i] = a/b
            
    return c5

def aud_score_eval(a,df):
    a1 = []
    for i in range(len(a)):
        a2 = re.split('/ |, ',str(a[i]))
        for a3 in a2:
            a1.append(str(a3).strip())
    a4 = {}
    for i in range(len(a1)):
        if a1[i] in a4:
            a4[a1[i]] = a4[a1[i]] + 1
        else:
            a4[a1[i]] = 1
    a5 = {}
    for i in a4:
        x = 0
        y = 0
        for j in range(len(a)):
            if i in str(a[j]):
                x = x + (df.loc[j,'Audience_average_rating']*df.loc[j,'Audience_user_count'])
                y = y + df.loc[j,'Audience_user_count']
                a5[i] = x/y
            
    return a5

if __name__=='__main__': 
    
    df = pd.read_csv("C:/Users/Abhitej Kodali/Google Drive/BIA 660 Team Project/Abhitej Workspace/Full Movie List.csv")
    
    s = pd.Series(df['Studio'])
    s1 = critic_score_eval(s,df)
    for i in range(len(s)):
        s2 = re.split('/',str(s[i]))
        crit_sc=0
        crit_mean=0
        for s3 in s2:
            crit_sc = crit_sc + df.Studio.map(s1)
            crit_mean = crit_sc/len(s2)
        df['Studio_critic_score'] = crit_mean
    
    d = pd.Series(df['Director'])
    d1 = critic_score_eval(d,df)
    for i in range(len(d)):
        d2 = re.split(',',str(d[i]))
        crit_sc=0
        crit_mean=0
        for d3 in d2:
            crit_sc = crit_sc + df.Director.map(d1)
            crit_mean = crit_sc/len(d2)
        df['Director_critic_score'] = crit_mean
    
    sa = pd.Series(df['Studio'])
    sa1 = aud_score_eval(sa,df)
    for i in range(len(sa)):
        sa2 = re.split('/',str(sa[i]))
        aud_sc=0
        aud_mean=0
        for sa3 in sa2:
            aud_sc = aud_sc + df.Studio.map(sa1)
            aud_mean = aud_sc/len(sa2)
        df['Studio_audience_score'] = aud_mean
    
    da = pd.Series(df['Director'])
    da1 = aud_score_eval(da,df)
    for i in range(len(da)):
        da2 = re.split(',',str(da[i]))
        aud_sc=0
        aud_mean=0
        for da3 in da2:
            aud_sc = aud_sc + df.Director.map(da1)
            aud_mean = aud_sc/len(da2)
        df['Director_audience_score'] = aud_mean
    
    df.to_csv("C:/Users/Abhitej Kodali/Google Drive/BIA 660 Team Project/Abhitej Workspace/Full Movie List_v2.csv", encoding='utf-8',index=False)
    