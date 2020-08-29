#%%
import pandas as pd
import numpy as np
import mplfinance as mpl
# %%
dataGBP= pd.read_csv('GBPUSDm30.csv', skiprows= 23683)
import DataCleaner
from DataCleaner import dataCleaner
dataGBP= dataCleaner(dataGBP)
# %%
def shootingStar(data):
    isShootingStar= []
    O= dataGBP.columns.get_loc('Open')
    H= dataGBP.columns.get_loc('High')
    L= dataGBP.columns.get_loc('Low')
    C= dataGBP.columns.get_loc('Close')
    if dataGBP.iloc[i, O] > dataGBP.iloc[i, C]:
        upShadow= dataGBP.iloc[i, H]- dataGBP.iloc[i, O]
        body= dataGBP.iloc[i, O]- dataGBP.iloc[i, C]
        lowShadow= dataGBP.iloc[i, C]- dataGBP.iloc[i, L]
    