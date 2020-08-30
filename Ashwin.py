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
        buy_value.append(np.nan)
        sell_value.append(np.nan)
        hold_value.append(np.nan)
    for i in range(window_size, data.shape[0]):
        window_begin= i - window_size
        window_end = window_begin + window_size -1
        window_midle= (window_begin + window_end) / 2
        minimum= data.iloc[window_begin, low]
        maximum= data.iloc[window_begin, high]
        min_index= window_begin
        max_index= window_begin
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
            buy_value.append(np.nan)
            sell_value.append(maximum)
            hold_value.append(np.nan)
        elif min_index == window_midle:
            sell.append(False)
            buy.append(True)
            hold.append(False)
            buy_value.append(minimum)
            sell_value.append(np.nan)
            hold_value.append(np.nan)
        else:
            sell.append(False)
            buy.append(False)
            hold.append(True)
            buy_value.append(np.nan)
            sell_value.append(np.nan)
            hold_value.append(np.nan)
    data['Buy']= buy
    data['Sell']= sell
    data['Hold']= hold
    data['BuyValue']= buy_value
    data['SellValue']= sell_value
    data['HoldValue']= hold_value

    return data
          
# %%
GBP= labeling(GBP, 11)
# %%
adp_data= GBP[['BuyValue', 'SellValue']]
adp= mpl.make_addplot(adp_data.iloc[0:100, :], type= 'scatter', markersize= 200)
mpl.plot(GBP.iloc[0:100, :], type= 'candle', style= 'charles', figscale= 6, addplot=adp)
# %%
