#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:18:37 2021

@author: patrickwickersham
"""
import pandas as pd
import numpy as np
import  io
import zipfile
import csv
from urllib.request import urlopen
url = urlopen('http://mis.nyiso.com/public/csv/biddata/20000101biddata_ucdata_csv.zip')
#Download Zipfile and create pandas DataFrame
#zipfile = ZipFile(StringIO(url.read()))
zipname = '20000101biddata_ucdata_csv.zip'
csvname = '20000101biddata_ucdata_csv'
inp_byte = zip.open(csvname)
inp_handle = io.TextIOWrapper(inp_byte)

x = pd.read_csv(zipfile.open('20000101biddata_ucdata_csv.zip'), 
                     header = 100000)
#%%
urllib = {}
for typ in bid_type:
    url = f"http://mis.nyiso.com/public/csv/biddata/20{y}{m}01biddata_{typ}_csv.zip"
    for y in yr:
        url = f"http://mis.nyiso.com/public/csv/biddata/20{y}{m}01biddata_{typ}_csv.zip"
        for m in mo:
            url = f"http://mis.nyiso.com/public/csv/biddata/20{y}{m}01biddata_{typ}_csv.zip"
            urllib = urllib.append(url)