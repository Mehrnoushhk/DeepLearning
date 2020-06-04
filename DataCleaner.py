def ClearData(filePath):
    # This function prepare metatrader exported file for machine learning use
    import pandas as pd
    data= pd.read_csv(filePath)
    data.columns= ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']
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

df= ClearData('https://raw.githubusercontent.com/Mehrnoushhk/DeepLearning/master/USDJPYm30.csv')
print(df.head())
print(type(df['Date']))