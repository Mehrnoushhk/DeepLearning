#%%
import pandas as pd
import numpy as np
import mplfinance as mpl
# %%
import DataCleaner
from DataCleaner import dataCleaner
dataEUR= pd.read_csv('EURUSDm30.csv', skiprows= 52494)
dataEUR= dataCleaner(dataEUR)
# %%
from DataCleaner import localMin, localMax
n_steps= 4
dataEUR= localMin(dataEUR, n_steps)
dataEUR= localMax(dataEUR, n_steps)
# %%
minMax= dataEUR[['minValue', 'maxValue']]
adp= mpl.make_addplot(minMax[len(minMax)-200:], type= 'scatter', markersize= 200 )
mpl.plot(dataEUR.iloc[dataEUR.shape[0]-200:,:], type= 'candle', figscale= 6, style= 'charles', addplot= adp)
# %%
columnsName= dataEUR.columns
dataEUR= dataEUR.reindex(columns= dataEUR.columns.tolist() + ['Trend','TrendValue'])
# %%
from DataCleaner import nextTrend
dataEUR= nextTrend(dataEUR)
# %%
j= dataEUR.columns.get_loc('TrendValue')
adp= mpl.make_addplot(dataEUR.iloc[dataEUR.shape[0]-200:, j], type= 'scatter', markersize= 200)
mpl.plot(dataEUR.iloc[dataEUR.shape[0]-200:, :], type= 'candle', style= 'charles', figscale= 6, addplot= adp)
# %%
j= dataEUR.columns.get_loc('Trend')
Up= 1
Down= 1
Cons= 1
for k in range(100, dataEUR.shape[0]-200, 200):
    for i in range(k, k+200):
        if dataEUR.iloc[i, j] == 1:
            upName= 'C:\\Users\\Maryam-Goli\\Documents\\CNNEUR\\UpTrend\\'+'Uptrend'+ str(Up)+ '.png'
            mpl.plot(dataEUR.iloc[i-100:i, :], type= 'candle', style= 'charles', axisoff= True, savefig= upName)
            Up += 1

        elif dataEUR.iloc[i, j] == 0:
            consName= 'C:\\Users\\Maryam-Goli\\Documents\\CNNEUR\\NoTrend\\'+'Notrend'+ str(Cons)+ '.png'
            mpl.plot(dataEUR.iloc[i-100:i, :], type= 'candle', style= 'charles', axisoff= True, savefig= consName)
            Cons += 1

        elif dataEUR.iloc[i, j] == -1:
            downName= 'C:\\Users\\Maryam-Goli\\Documents\\CNNEUR\\DownTrend\\'+'Downtrend'+ str(Down)+ '.png'
            mpl.plot(dataEUR.iloc[i-100:i, :], type= 'candle', style= 'charles', axisoff= True, savefig= downName)
            Down += 1

# %%
