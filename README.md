#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 10:27:17 2021

@author: patrickwickersham
"""

#Analysis Theory
Bid data submitted to the NYISO must be published and publicly available.  
To protect the identities this data is given masked id values for each market participant.

##Market Participant type
**masked bidder id, NUM**, A numeric (integer) identifier for bidder that can 
be tracked over time.
**masked source id, NUM**, A numeric (integer) identifier for source 
(generator) that can be tracked over time.
**masked sink id, NUM** A numeric (integer) identifier for sink (load) that 
can be tracked over time.
**masked location id, NUM**, A numeric (integer) identifier for location that 
can be tracked over time. 

#bid_zip_loc.py
get_bid_loc.py is the first program to run. It creates a directory of URL links for 
the downloadable .csv.zip files on the 
'http://mis.nyiso.com/public/P-27list.htm'

#bid_df.py
bid_df.py is a *proof of concept* program.  As of 6/7/21 it downloads the data 
from one .csv.zip file to clean, wrangle, and prepare for
analysis. The file chosen was the second to most recent file published in the 
genbids category.  Genbids was chosen becuase generation bids are the most 
commonly thought of bid type. The second to last file was chosen to ensure 
the most updated data management practices are coded for first but avoiding 
the most recently published file in case updates to the new data need to be 
made.

module bid_data_dict
-> gets list of web zips  (apa_final)
