#%%
import pandas as pd
import numpy as np
import mplfinance as mpl
# %%
GBP= pd.read_csv('GBPUSDm30.csv', nrows= 1000)
# %%
import DataCleaner
from DataCleaner import dataCleaner
GBP= dataCleaner(GBP)
# %%
def labeling(data, window_size):
    low= data.columns.get_loc('Low')
    high= data.columns.get_loc('High')
    buy= []
    sell= []
    hold= []
    buy_value=[]
    sell_value = []
    hold_value= []
    for i in range(0, window_size):
        buy.append(False)
        sell.append(False)
        hold.append(False)
        
    for i in range(window_size, data.shape[0]):
        window_begin= i - window_size
        window_end = window_begin + window_size -1
        window_midle= (window_begin + window_end) / 2
        minimum= data.iloc[window_begin, low]
        maximum= data.iloc[window_begin, high]
        for j in range(window_begin, window_end + 1):
            min_number = data.iloc[j, low]
            max_number = data.iloc[j, high]
            if min_number < minimum:
                minimum= min_number
                min_index = j
            if max_number > maximum:
                maximum = max_number
                max_index = j
        if max_index == window_midle:
            sell.append(True)           
            buy.append(False)
            hold.append(False)
        elif min_index == window_midle:
            sell.append(False)
            buy.append(True)
            hold.append(False)
        else:
            sell.append(False)
            buy.append(False)
            hold.append(Trur)
    data['Buy']= buy
    data['Sell']= sell
    data['Hold']= hold

    return data
    

    
        
        