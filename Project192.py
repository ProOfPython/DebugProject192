import pandas as pand
import matplotlib.pyplot as plot
import numpy

rawData = pand.read_csv('Project192+/bmi.csv')

srchUnder = rawData.loc[(rawData['bmi']) < 18.5 ]['gender'].reset_index(name = 'gender')
srchWell = rawData.loc[18.5 <= (rawData['bmi']) <= 24.9 ]['gender'].reset_index(name = 'gender')
print(srchUnder)
print(srchWell)

plot.bar