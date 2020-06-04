def ClearData(data):
    # This function prepare metatrader exported file for machine learning use
    data.columns= ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    import datetime
    for i in range(0, data.shape[0]):
        temptext= data.iloc[i, 0]
        a= int(temptext[0:4])
        b= int(temptext[5:7])
        c= int(temptext[8:])
        temptime= data.iloc[i, 1]
        h= int(temptime[:-3])
        tempdate= datetime.datetime(year= a, month= b, day= c, hour= h, minute= 0, second= 0)
        data.iloc[i,0]= tempdate
