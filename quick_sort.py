import time
def partition(data,head,tail,drawData,time_set):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(time_set)

    for j in range(head,tail):
        if data[j]<pivot:
            drawData(data, getColorArray(len(data), head, tail, border,j,True))
            time.sleep(time_set)
            data[border],data[j] = data[j],data[border]
            border += 1
        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(time_set)

    # swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail,True))
    time.sleep(time_set)
    data[border],data[tail] = data[tail],data[border]
    return border

def Quick_sort(data,head,tail,drawData,time_set):
    if head < tail:
        partition_index = partition(data,head,tail,drawData,time_set)
        # LEFT PARTITION
        Quick_sort(data,head,partition_index-1,drawData,time_set)
        # RIGHT PARTITION
        Quick_sort(data,partition_index+1,tail,drawData,time_set)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base color
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'
        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray