# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 22:26:10 2021

@author: Caroline
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    
#links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
#       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
    
link1 = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv'
link2 = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'


df = pd.read_csv(link1)
dt = pd.read_csv(link2)




fig, ax = plt.subplots()
dt.plot(x='date', y='unemployment', ax=ax)
plt.show()



print(dt.head())
print(dt.query)

#Filtro
dt.query('unemployment > 8.5', inplace = True)


print(df.tail(10))
print(df.dtypes)

