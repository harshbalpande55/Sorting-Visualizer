import time

def Merge_sort(data, left, right, drawData, time_set):
    if left<right:
        middle = (left + right) // 2
        Merge_sort(data,left,middle,drawData,time_set)
        Merge_sort(data, middle + 1, right, drawData, time_set)
        merge(data, left, middle, right, drawData, time_set)

def merge(data ,left,middle,right,drawData,time_set):

    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(time_set)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]
    leftIdx = rightIdx = 0
    for dataIdx in range(left,right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx+=1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(time_set)

def getColorArray(lenght, left, middle, right):
    colorArray = []
    for i in range(lenght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append('pink')
        else:
            colorArray.append("white")
    return colorArray