#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:52:14 2021

@author: patrickwickersham
"""
import requests
from bs4 import BeautifulSoup

#%% --- Open NYISO Bid Data Directory
NYISO_bid_dir =  'http://mis.nyiso.com/public/P-27list.htm' 
RESPONSE = requests.get(NYISO_bid_dir, stream=True)  
#requests.get(stream=True) -> /!\ holds path open until all data is used or 
#call Response.close /!\                                             
    
#print(r.status_code)
if RESPONSE.status_code == requests.codes.ok:
    HTML = RESPONSE.content.decode("utf-8") 
    soup = BeautifulSoup(HTML, "html.parser")    
    #To check soup -> print(soup.prettify())

    LINKS = soup.select("a")    

      

#%% --- Create dictionary to store bid data
GB_TAG = "genbids" 
ICAP_TAG = "icapbids" # narrowed scope of data collection to two generation bids and installed capacity bids for expedience in prrof of concept.
genbids = {}
icapbids = {}

#Later versions will store the above dictionaries using hierarchical indexing 



#%% --- Filter URLs into their corresponding dictionaries /!\ (this creates a dictionary of web addresses, ZIPPED PAYLOAD STILL NOT UNPACK YET)
for LINK in LINKS:
    URL = LINK['href']
    TEXT = LINK.TEXT                    #parse text->date published for posterity
    
    if GB_TAG in LINK['href']:
        URL = LINK["href"]
        TEXT = LINK.TEXT
        genbids[f"{TEXT}"] = URL    #creates dictionary with text(pub date) as key
    if ICAP_TAG in LINK['href']:
        URL = LINK["href"]
        TEXT = LINK.TEXT
        icapbids[f"{TEXT}"] = URL
        
RESPONSE.close()
