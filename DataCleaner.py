print('Hello World!')
import datetime
import numpy as np
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

def localMax(data, step):
    # Returns two list, a True/False list and a Value list
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


def nextHigh(data, i):
    nextHighValue= data.iloc[i].loc['maxValue']
    for j in range(i+1, data.shape[0]):
        if data.iloc[j].loc['isMax']== True:
            nextHighValue= data.iloc[j].loc['maxValue']
            break
    return nextHighValue

def nextLow(data, i):
    nextLowValue= data.iloc[i].loc['minValue']
    for j in range(i+1, data.shape[0]):
        if data.iloc[j].loc['isMin']== True:
            nextLowValue= data.iloc[j].loc['minValue']
            break
    return nextLowValue

def previousHigh(data, i):
    previousHighValue= data.iloc[i].loc['maxValue']
    j= i-1
    while j>= 0:
        if data.iloc[j].loc['isMax']== True:
            previousHighValue= data.iloc[j].loc['maxValue']
            break
        j= j- 1
    return previousHighValue

def previousLow(data, i):
    previousLowValue= data.iloc[i].loc['minValue']
    j= i-1
    while j>= 0:
        if data.iloc[j].loc['isMin']== True:
            previousLowValue= data.iloc[j].loc['minValue']
            break
        j= j-1
    return previousLowValue
    
def nextTrend(data, i, Trend):
    if data.iloc[i].loc['isMax'] == True:
        if ((nextHigh(data,i)<data.iloc[i].loc['maxValue']) and (nextLow(data,i)<previousLow(data,i))):
            Trend[i]= -1
        else:
            Trend[i]= 0

    
    if data.iloc[i].loc['isMin'] == True:
        if (nextLow(data, i) > data.iloc[i].loc['minValue']) and (nextHigh(data, i) > previousHigh(data, i)):
            Trend[i]= 1
        else:
            Trend[i]= 0

    return Trend

print('Bye')