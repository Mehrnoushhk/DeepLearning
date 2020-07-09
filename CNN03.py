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