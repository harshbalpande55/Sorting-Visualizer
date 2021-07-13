from tkinter import *
from tkinter import ttk
import random
from tkinter.font import Font
from bubble_sort import Bubble_sort
from quick_sort import Quick_sort
from merge_sort import Merge_sort
from insertion_sort import Insertion_Sort
from selection_sort import Selection_sort


window = Tk()
window.title("Sorting Algorithm Visualization")
window.maxsize(900,600)
window.config(bg='#FFD8CC')

# frame / base layout
UI_frame = Frame(window, width= 600, height=200, bg='#E98580')
UI_frame.grid(row=0, column=0, padx=5, pady=5)

canvas = Canvas(window, width=625, height=370, bg='#FFD8CC')
canvas.grid(row=1, column=0, padx=5, pady=5)

data = []

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    # width of the bar graph
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))
    window.update_idletasks()

def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))
    # ['red', 'red' ,....]
    drawData(data, ['red' for color in range(len(data))])

def StartAlgorithm():
    global data
    if not data:
        return
    if algMenu.get() == 'Quick Sort':
        l1 = Label(UI_frame, text="Time complexity of Quick Sort Algorithm is : O(n^2) ", fg='white', bg='#E98580',font=font_3)
        l1.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=W)
        Quick_sort(data, 0, len(data)-1, drawData, speedScale.get())

    elif algMenu.get() == 'Bubble Sort':
        l1 = Label(UI_frame, text="Time complexity of Bubble Sort Algorithm is : O(n^2) ", fg='white', bg='#E98580',font=font_3)
        l1.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=W)
        Bubble_sort(data,drawData,speedScale.get())

    elif algMenu.get() == 'Merge Sort':
        l1 = Label(UI_frame, text="Time complexity of Merge Sort Algorithm is : O(nlog(n)) ", fg='white', bg='#E98580',font=font_3)
        l1.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=W)
        Merge_sort(data,0,len(data)-1,drawData,speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        l1 = Label(UI_frame, text="Time complexity of Insertion Sort Algorithm is : O(n^2) ", fg='white', bg='#E98580',font=font_3)
        l1.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=W)
        Insertion_Sort(data,drawData,speedScale.get())

    elif algMenu.get() == 'Selection Sort':
        l1 = Label(UI_frame, text="Time complexity of Selection Sort Algorithm is : O(n^2) ", fg='white', bg='#E98580',font=font_3)
        l1.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=W)
        Selection_sort(data,drawData,speedScale.get())

    drawData(data, ['green' for x in range(len(data))])

font_1 = Font(size=18,weight='bold')
font_2 = Font(size=10)
font_3 = Font(size=15, weight='normal')

# User Interface Area
# Row[0]

l1 = Label(UI_frame, text="Select Algorithm: ",fg='white', bg='#E98580', font = font_1)
l1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

# variables
selected_algorithm = StringVar()
algMenu = ttk.Combobox(UI_frame,textvariable=selected_algorithm,values=['Bubble Sort','Quick Sort','Merge Sort','Insertion Sort','Selection Sort'],font=font_2)
algMenu.grid(row=0, column=1)
algMenu.current(0)

b1 = Button(UI_frame, text="Generate Array", command=Generate, bg='#FFC947',relief=RAISED, font = font_2)
b1.grid(row=0, column=2, padx=5, pady=10)

b2 = Button(UI_frame, text="Start Visualization", command=StartAlgorithm, bg='#FFC947',relief=RAISED, font = font_2)
b2.grid(row=0, column=3, padx=5, pady=10)

# Row[1]
speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=180, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]", font = font_2)
speedScale.grid(row=1, column=0)

sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Size of Data", font = font_2)
sizeEntry.grid(row=1, column=1)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value", font = font_2)
minEntry.grid(row=1, column=2, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value", font = font_2)
maxEntry.grid(row=1, column=3, padx=5, pady=5)

# Row[3]
b3 = Button(UI_frame,text="Close the Program",command=window.destroy, bg='#FFC947',relief=RAISED, font = font_2)
b3.grid(row=2,column=3, padx=5, pady=5)

window.mainloop()
