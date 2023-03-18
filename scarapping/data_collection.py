# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:47:44 2020
@author: Ken
"""

# import glass_door_scrapping as gs 
import pandas as pd 

# path = "/Users/pawanacharya0123/Documents/python_question/DataScience/salaryP/scarapping/chromedriver"

# df = gs.get_jobs('data scientist',10, False, path, 30)

df= pd.read_csv('glassdoor_jobs.csv')
print(df.head())