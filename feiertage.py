# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 15:01:17 2019

@author: T.Schulz
"""

import numpy as np
import pandas as pd
import urllib3
from bs4 import BeautifulSoup
from ast import literal_eval
import csv

url = "https://feiertage-api.de/api/?jahr={jahr}&nur_land=TH"

# Fetch the html file
http = urllib3.PoolManager()
feiertage = pd.DataFrame()


for year in np.arange(2000,2099,1):
    data = http.request('get',url.format(jahr=year))
    data=data.data.decode()
    dat_dict = literal_eval(data)
    frame=pd.DataFrame.from_dict(dat_dict, orient='index')
    frame = frame.sort_values(by='datum')
    feiertage = pd.concat([feiertage,frame])
    
feiertage =feiertage.reset_index()


#%%
    

with open('feiertage.csv', 'w') as f:  
    f.write(feiertage.to_csv(sep=";"))
    
    