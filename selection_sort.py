import time

def Selection_sort(data,drawData,time_set):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1,len(data)):
            if data[min_index]>data[j]:
                drawData(data, getColorArray(len(data), i, j))
                time.sleep(time_set)
                min_index = j
        drawData(data, getColorArray(len(data), i, min_index))
        data[min_index],data[i] = data[i],data[min_index]

    drawData(data, ['green' for x in range(len(data))])
    time.sleep(time_set)

def getColorArray(dataLen,key,index):
    colorArray = []
    for i in range(dataLen):
        # base color
        if i >=key :
            colorArray.append('gray')
        else:
            colorArray.append('green')
        if i == key:
            colorArray[i] = 'blue'
        elif i == index:
            colorArray[i] = 'red'

    return colorArray