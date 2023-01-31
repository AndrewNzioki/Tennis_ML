# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 09:28:11 2023

@author: acnzi
"""

import pandas as pd
import logging
import sys


logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


"""
In this project, we want to predict the ranking tier of a player based on the 
variables we have been given. We have many features so let us start

we want this to be a classification algorithm, so our y values will need to
be in classes, therefore we will need to encode the ranking variables in a way
that shows these classifications


"""
'''
Step 1: Extract, load and Transform Data

'''

tennis = pd.read_csv("tennis_stats.csv")
#print(tennis.head())



#print info on the table
#print(tennis.info())

#there are no null values, so we can continue


