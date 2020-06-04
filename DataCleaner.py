def ClearData(filePath, name):
    # This function prepare metatrader exported file for machine learning use
    import pandas as pd
    data= pd.read_csv(filePath)
    data.columns= ['Date', 'Time', name+'Open', name+'High', name+'Low', name+'Close', name+'Volume']
    import datetime
    for i in range(0, data.shape[0]):
        temptext= data.iloc[i, 0]
        a= int(temptext[0:4])
        b= int(temptext[5:7])
        c= int(temptext[8:])
        temptime= data.iloc[i, 1]
        h= int(temptime[0:2])
        m= int(temptime[3:])
        tempdate= datetime.datetime(year= a, month= b, day= c, hour= h, minute= m, second= 0)
        data.iloc[i,0]= tempdate
    del data['Time']
    data.set_index('Date', inplace= True)
    data.index= pd.to_datetime(data.index)
    return data
def mergeCurrencies(data1, data2):
    import pandas as pd
    data1Step= data1.iloc[0,1]- data1.iloc[0,0]
    data2Step= data2.iloc[0,1]- data2.iloc[0,0]
    print(data1Step)
    print(data2Step)
    # if data1Step == data2Step:
    #     fulldata= pd.merge(data1, data2, on='Date')
    # else:
    fulldata= data1
    return fulldata


urlEUR='https://raw.githubusercontent.com/Mehrnoushhk/DeepLearning/master/EURUSDm30.csv'
urlGBP='https://raw.githubusercontent.com/Mehrnoushhk/DeepLearning/master/GBPUSDm30.csv'

dfEUR= ClearData(urlEUR, 'EUR')
dfGBP= ClearData(urlGBP, 'GBP')
print(dfEUR.head())
print(dfGBP.head())
dfMarket = mergeCurrencies(dfEUR, dfGBP)
print(dfMarket.head())



""" 
import mplfinance as mpl
mpl.plot(df.iloc[0:100,:], type= 'candle', style= 'charles', figscale= 6) 
"""