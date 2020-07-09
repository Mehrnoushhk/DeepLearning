import numpy as np
import pandas as pd
import datetime
import mplfinance as mpl
print(mpl.__version__)
url= 'https://raw.githubusercontent.com/Mehrnoushhk/DeepLearning/master/GBPUSDm30.csv'
data= pd.read_csv(url) 
from DataCleaner import dataCleaner
data= dataCleaner(data)
from DataCleaner import localMax
from DataCleaner import localMin
dataMax, dataMaxValue= localMax(data, 4)
dataMin, dataMinValue= localMin(data, 4)
minMax= pd.DataFrame(list(zip(dataMinValue, dataMaxValue)), columns=['min', 'Max'])
data['isMax']= dataMax
data['maxValue']= dataMaxValue
data['isMin']= dataMin
data['minValue']= dataMinValue
isMaxid= 6
maxValueid= 7
isMinid= 8
minValueid= 9
Trendid= 10