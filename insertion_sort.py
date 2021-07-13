import time

def Insertion_Sort(data,drawData,time_set):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            drawData(data,getColorArray(len(data),i,j))
            time.sleep(time_set)
            data[j+1] = data[j]
            j -= 1

        drawData(data, getColorArray(len(data), i, j+1))
        time.sleep(time_set)

        data[j+1] = key

    drawData(data, ['green' for x in range(len(data))])
    time.sleep(time_set)

def getColorArray(dataLen,key,index):
    colorArray = []
    for i in range(dataLen):
        # base color
        if i <= key :
            colorArray.append('gray')
        else:
            colorArray.append('red')
        if i == key:
            colorArray[i] = 'blue'
        elif i == index:
            colorArray[i] = 'green'

    return colorArray