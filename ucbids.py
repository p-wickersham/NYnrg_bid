#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 06:23:13 2021

@author: patrickwickersham
"""

import pandas as pd

df = pd.read_csv('20210101biddata_ucdata.csv', header=0)
    
Masked_Gen_ID = pd.DataFrame()
  
val = 'Masked Gen ID'
x = df['Masked Gen ID'].values


#%%
for df['Masked Gen ID'].values in df:
     if Masked_Gen_ID.has_key(df['Masked Gen ID'].values):
        Masked_Gen_ID[df['Masked Gen ID'].values] = Masked_Gen_ID[['Masked Gen ID'].values].append.value(val)
     if False:
        Masked_Gen_ID[(df['Masked Gen ID'].values(df['Mask Gen ID']) == Masked_Gen_ID[df['Masked Gen ID']].values(df['Masked Gen ID'])