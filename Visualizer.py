import tkinter as tk
import random
import time

numberOfBars = 30
bars = [x for x in range(0, numberOfBars * 10, 10)]
updateTime = 0.05


def drawRectangle(x0, y0, x1, y1):
    return canvas.create_rectangle(x0, y0, x1, y1, fill='#00FF00')

def shuffle():
    shuffled = bars
    random.shuffle(shuffled)
    canvas.delete('all')
    global shuffledBars
    shuffledBars = []
    j = 0
    for i in shuffled:
        shuffledBars.append([drawRectangle(j, numberOfBars * 10, j + 10, i), i])
        j += 10


def swap(shuffled, l1, l2):
    l1[1], l2[1] = l2[1], l1[1]
    canvas.delete(l1[0], l2[0])
    i1, i2 = shuffled.index(l1), shuffled.index(l2)
    shuffled[i1] = [drawRectangle(i1 * 10, numberOfBars * 10, i1 * 10 + 10, l1[1]), l1[1]]
    shuffled[i2] = [drawRectangle(i2 * 10, numberOfBars * 10, i2 * 10 + 10, l2[1]), l2[1]]
    root.update_idletasks()
    time.sleep(updateTime)
        

def heapify(shuffled, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and shuffled[i][1] < shuffled[l][1]:
        largest = l
    if r < n and shuffled[largest][1] < shuffled[r][1]:
        largest = r
    if largest != i:
        swap(shuffled, shuffled[i], shuffled[largest])
        heapify(shuffled, n, largest)


def heap_sort(shuffled):
    n = len(shuffled)
    for i in range(n // 2 - 1, -1, -1):
        heapify(shuffled, n, i)
    for i in range(n - 1, 0, -1):
        swap(shuffled, shuffled[i], shuffled[0])
        heapify(shuffled, i, 0)


def partition(shuffled, low, high):
    i = low - 1
    pivot = shuffled[high][1]
    for j in range(low, high):
        if shuffled[j][1] < pivot:
            i += 1
            if i == j: continue
            swap(shuffled, shuffled[i], shuffled[j])
    swap(shuffled, shuffled[i + 1], shuffled[high])
    return i + 1


def quick_sort(shuffled, low, high):
    if low < high:
        pi = partition(shuffled, low, high)
        quick_sort(shuffled, low, pi - 1)
        quick_sort(shuffled, pi + 1, high)


def bubble_sort(shuffled):
    n = len(shuffled)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if shuffled[j][1] > shuffled[j + 1][1]:
                swap(shuffled, shuffled[j], shuffled[j + 1])


def selection_sort(shuffled):
    for i in range(len(shuffled)):
        min_idx = i
        for j in range(i + 1, len(shuffled)):
            if shuffled[min_idx][1] > shuffled[j][1]:
                min_idx = j
        swap(shuffled, shuffled[i], shuffled[min_idx])


def sliderHandle(event):
    global updateTime
    updateTime = updateTimeSlide.get() / 10000


root = tk.Tk()

updateTimeSlide = tk.DoubleVar()

blues = tk.Frame()
blues.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
canvas = tk.Canvas(blues, width=500, height=numberOfBars * 10)
shuffle()
canvas.pack(fill=tk.BOTH, expand=1)

tk.Button(root, text='Heap Sort', command=lambda: heap_sort(shuffledBars), width=20, height=5).grid(row=1, column=0)
tk.Button(root, text='Quick Sort', command=lambda: quick_sort(shuffledBars, 0, len(shuffledBars) - 1), width=20, height=5).grid(row=1, column=1)
tk.Button(root, text='Shuffle', command=shuffle, width=20, height=5).grid(row=1, column=2)
tk.Button(root, text='Bubble Sort', command=lambda: bubble_sort(shuffledBars), width=20, height=5).grid(row=2, column=0, pady=10)
tk.Button(root, text='Selection Sort', command=lambda: selection_sort(shuffledBars), width=20, height=5).grid(row=2, column=1, pady=10)
tk.Label(root, text='Lower number = faster update').grid(row=3, column=2)
tk.Scale(root, from_=1000, to=1, orient='horizontal', variable=updateTimeSlide, command=sliderHandle).grid(row=2, column=2, pady=10)

root.geometry('580x550+300+300')
root.title('Sorting Algorithms')
root.mainloop()
