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
                 dtype=str)
column_names = df.columns 
df.info()
