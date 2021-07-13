import time

def Bubble_sort(data, drawData, time_set):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data,['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(time_set)
    drawData(data, ['green' for x in range(len(data))])