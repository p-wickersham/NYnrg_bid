#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 09:45:58 2021

@author: patrickwickersham
"""

#%% 
#??? Convert to a fnx_def to loop over list get_bid_loc.py
#??? will require urlopen and read

# /!\ CURRENTLY THIS FILE REQUIRES YOU DOWNLOAD A BID.CSV.ZIP FILE MANUALLY
    
#%% Import modules
import csv
import io
import zipfile
import pandas as pd
import numpy as np


#%% retrieve and read a single-file .csv.zip into a dataframe
zipname = '20191201biddata_genbids_csv.zip'

df = pd.read_csv(zipname, 
                 compression='zip', 
                 header=0, sep=',', 
                 quotechar='"',
                 nrows=10000,
                 infer_datetime_format=(True),
                 keep_date_col=True)
col_names = df.columns
df.info()



### /!\ Men at work /!\
### Under construction - please excuse our dust-bytes while we code.
#df['Date Time'].split('00''JAN''0000':'hh':'mm':'ss')
# 


print(df['Date Time'].values[0])
print(len(df['Date Time'].values[0]))
#len(19) - blank space at beginning



#%%% splitting dates
for value in df['Date Time']:
    d_time = value.split(':')
    print(d_time)
    
                                  
#returns: ValueError: Length of values (4) does not match length of index (408262)