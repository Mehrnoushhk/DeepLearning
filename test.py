import fileinput
import pandas as pd
inputData = []
for line in fileinput.input(files='f6bdc3bab15c11ea.txt'):
    inputData.append(line.strip())
print(inputData)
fileinput.close()
testNumbers = int(inputData[0])
matrix = []
i= 1
while i < len(inputData):
    matrixSize = int(inputData[i])
    tempList = []
    for j in range(1, matrixSize+1):
        tempList.append(inputData[i+j])
    matrix.append(tempList)
    i += matrixSize + 1
print(matrix)