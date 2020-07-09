import numpy as np
import pandas as pd
import datetime
import mplfinance as mpl
url= 'https://raw.githubusercontent.com/Mehrnoushhk/DeepLearning/master/GBPUSDm30.csv'
data= pd.read_csv(url) 
from DataCleaner import dataCleaner
data= dataCleaner(data)
from DataCleaner import localMax
from DataCleaner import localMin
dataMax, dataMaxValue= localMax(data, 4)
dataMin, dataMinValue= localMin(data, 4)
data['isMax']= dataMax
data['maxValue']= dataMaxValue
data['isMin']= dataMin
data['minValue']= dataMinValue