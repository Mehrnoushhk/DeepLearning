print('Hi')
def dataCleaner(data):
    import datetime
    import numpy as np
    import pandas as pd
    data.columns= ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume'] 
    numericIndex= []
    for i in range(0, data.shape[0]):
        temptext= data.iloc[i, 0]
        a= int(temptext[0:4])
        b= int(temptext[5:7])
        c= int(temptext[8:])
        temptime= data.iloc[i, 1]
        h= int(temptime[:-3])
        m= int(temptime[3:])
        tempdate= datetime.datetime(year= a, month= b, day= c, hour= h, minute= m, second= 0)
        data.iloc[i,0]= tempdate
        numericIndex.append(i)
    del data['Time']
    data.set_index('Date', inplace= True)
    data.index= pd.to_datetime(data.index)
    data['ID']= numericIndex
    return data

def mergeCurrencies(data1, name1, data2, name2):
    import pandas as pd
    data1.columns= [name1+'Open', name1+'High', name1+'Low', name1+'Close', name1+'Volume']
    data2.columns= [name2+'Open', name2+'High', name2+'Low', name2+'Close', name2+'Volume']
    data1Step= data1.index.values[1]- data1.index.values[0]
    data2Step= data2.index.values[1]- data2.index.values[0]
    if data1Step == data2Step:
        fulldata= pd.merge(data1, data2, on='Date')
    return fulldata

# def localOptimum(data, nStep):
#     isMax= []
#     isMin= []
#     for i in range(nStep, data.shape[0]-nStep):
#         tempIsMax= True
#         tempIsMin= True
#         for j in range(i-nstep, i):
#             # This is the ith row, n previous candels
#             if data.iloc[i,1] < data.iloc[j, 1]:
#                 tempIsMax= False
#             if data.iloc[i, 2] > data.iloc[j, 2]:
#                 tempIsMin = False
            
# Define Local Maximum
def localMax(data, step):
    import numpy as np
    isMax= []
    maxValue= []
    for i in range(0, step):
        isMax.append(False)
        maxValue.append(np.nan)
    for i in range(step, data.shape[0]-step):
        tempOptimal= True
        tempValue= data.iloc[i, 1]
        for j in range(1, step+1):
            if (data.iloc[i,1] < data.iloc[i-j,1]) or (data.iloc[i,1] < data.iloc[i+j, 1]):
                tempOptimal= False
                tempValue= np.nan
            isMax.append(tempOptimal)
            maxValue.append(tempValue)
    for i in range(0, step):
        isMax.append(False)
        maxValue.append(np.nan)  
    return isMax, maxValue            


# Define Local Minimum
def localMin(data, step):
    import numpy as np
    isMin= []
    minValue= []
    for i in range(0, step):
        isMin.append(False)
        minValue.append(np.nan)
    for i in range(step, data.shape[0]-step):
        tempOptimal= True
        tempValue= data.iloc[i, 2]
        for j in range(1, step+1):
            if (data.iloc[i,2] > data.iloc[i-j,2]) or (data.iloc[i,2] > data.iloc[i+j, 2]):
                tempOptimal= False
                tempValue= np.nan
            isMin.append(tempOptimal)
            minValue.append(tempValue)
    for i in range(0, step):
        isMin.append(False)
        minValue.append(np.nan)  
    return isMin, minValue