#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 03:20:56 20219

@author: patrickwickersham
"""
#Calling the zipped csv file URL names from "r" website and storing them in 
#a dictionary.  This dictionary will be used to call out various different 
#attributes from the various datasets for comparison and analysis.
    
#%% Beautiful Soup - Extract zip urls
  
import requests
from bs4 import BeautifulSoup


#conda install BeautifulSoup

r = requests.get('http://mis.nyiso.com/public/P-27list.htm')
print(r.status_code)
html = r.content.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
#print(soup.prettify())
links = soup.select("a") 

genbidsubstr = "genbids"      #genbidsubstr and following 5 substrings 
loadbidsubstr = "loadbids"
tranbidsubstr = "tranbids"
ucbidsubstr = "ucdata"
tccbidsubstr = "tccbids"
icapbidsubstr = "icapbids"

genbids = {}
loadbids ={}
tranbids = {}
ucbids = {}
tccbids = {}
icapbids = {}

for link in links:
    address = link['href']
    text = link.text
    if genbidsubstr in link["href"]:
        address = link["href"]
        text = link.text
        genbids[f"{text}"] = address
    elif loadbidsubstr in link["href"]:
        address = link["href"]
        text = link.text
        loadbids[f"{text}"] = address
    elif tranbidsubstr in link["href"]:
        address = link["href"]
        text = link.text
        tranbids[f"{text}"] = address
    elif ucbidsubstr in link["href"]:
        address = link["href"]
        text = link.text
        ucbids[f"{text}"] = address
    elif tccbidsubstr in link["href"]:
        address = link["href"]
        text = link.text
        tccbids[f"{text}"] = address
    elif icapbidsubstr in link["href"]:
        address = link["href"]
        text = link.text
        icapbids[f"{text}"] = address
        
        
        
#%%%
