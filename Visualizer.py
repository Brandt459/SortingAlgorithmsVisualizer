import tkinter as tk
import random
import time


bars = [x for x in range(200) if x % 10 == 0]
updateTime = .1


def shuffle():
    rectangles = []
    shuffled = bars
    random.shuffle(shuffled)
    canvas.delete('all')
    j = 0
    for i in shuffled:
        rectangles.append(canvas.create_rectangle(
            j, 200, j + 10, i, fill='#00FF00'))
        j += 10
    global zipped
    zipped = list(zip(rectangles, bars))


def swap(shuffled, l1, l2):
    canvas.delete(l1[0], l2[0])
    i1 = shuffled.index(l1)
    i2 = shuffled.index(l2)
    shuffled[i1] = canvas.create_rectangle(
        i1 * 10, 200, i1 * 10 + 10, l1[1], fill='#00FF00'), l1[1]
    shuffled[i2] = canvas.create_rectangle(
        i2 * 10, 200, i2 * 10 + 10, l2[1], fill='#00FF00'), l2[1]


def heapify(shuffled, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and shuffled[i][1] < shuffled[l][1]:
        largest = l
    if r < n and shuffled[largest][1] < shuffled[r][1]:
        largest = r
    if largest != i:
        shuffled[i], shuffled[largest] = list(
            shuffled[i]), list(shuffled[largest])
        shuffled[i][1], shuffled[largest][1] = shuffled[largest][1], shuffled[i][1]
        swap(shuffled, shuffled[i], shuffled[largest])
        root.update_idletasks()
        time.sleep(updateTime)
        heapify(shuffled, n, largest)


def heap_sort(shuffled):
    n = len(shuffled)
    for i in range(n // 2 - 1, -1, -1):
        heapify(shuffled, n, i)
    for i in range(n - 1, 0, -1):
        shuffled[i], shuffled[0] = list(shuffled[i]), list(shuffled[0])
        shuffled[i][1], shuffled[0][1] = shuffled[0][1], shuffled[i][1]
        swap(shuffled, shuffled[i], shuffled[0])
        root.update_idletasks()
        heapify(shuffled, i, 0)


def partition(shuffled, low, high):
    i = low - 1
    pivot = shuffled[high][1]
    for j in range(low, high):
        if shuffled[j][1] <= pivot:
            i += 1
            shuffled[i], shuffled[j] = list(shuffled[i]), list(shuffled[j])
            shuffled[i][1], shuffled[j][1] = shuffled[j][1], shuffled[i][1]
            canvas.delete(shuffled[i][0])
            shuffled[i] = canvas.create_rectangle(
                shuffled.index(shuffled[i]) * 10, 200, shuffled.index(shuffled[i]) * 10 + 10, shuffled[i][1], fill='#00FF00'), shuffled[i][1]
            canvas.delete(shuffled[j][0])
            shuffled[j] = canvas.create_rectangle(
                shuffled.index(shuffled[j]) * 10, 200, shuffled.index(shuffled[j]) * 10 + 10, shuffled[j][1], fill='#00FF00'), shuffled[j][1]
            root.update_idletasks()
            time.sleep(updateTime)
    shuffled[i +
             1], shuffled[high] = list(shuffled[i + 1]), list(shuffled[high])
    shuffled[i + 1][1], shuffled[high][1] = shuffled[high][1], shuffled[i + 1][1]
    canvas.delete(shuffled[i + 1][0])
    canvas.delete(shuffled[high][0])
    shuffled[i + 1] = canvas.create_rectangle(
        shuffled.index(shuffled[i + 1]) * 10, 200, shuffled.index(shuffled[i + 1]) * 10 + 10, shuffled[i + 1][1], fill='#00FF00'), shuffled[i + 1][1]
    shuffled[high] = canvas.create_rectangle(
        shuffled.index(shuffled[high]) * 10, 200, shuffled.index(shuffled[high]) * 10 + 10, shuffled[high][1], fill='#00FF00'), shuffled[high][1]
    root.update_idletasks()
    time.sleep(updateTime)
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
                shuffled[j], shuffled[j +
                                      1] = list(shuffled[j]), list(shuffled[j + 1])
                shuffled[j][1], shuffled[j +
                                         1][1] = shuffled[j + 1][1], shuffled[j][1]
                canvas.delete(shuffled[j][0])
                shuffled[j] = canvas.create_rectangle(
                    shuffled.index(shuffled[j]) * 10, 200, shuffled.index(shuffled[j]) * 10 + 10, shuffled[j][1], fill='#00FF00'), shuffled[j][1]
                canvas.delete(shuffled[j + 1][0])
                shuffled[j + 1] = canvas.create_rectangle(
                    shuffled.index(shuffled[j + 1]) * 10, 200, shuffled.index(shuffled[j + 1]) * 10 + 10, shuffled[j + 1][1], fill='#00FF00'), shuffled[j + 1][1]
                root.update_idletasks()
                time.sleep(updateTime)


def selection_sort(shuffled):
    for i in range(len(shuffled)):
        min_idx = i
        for j in range(i + 1, len(shuffled)):
            if shuffled[min_idx][1] > shuffled[j][1]:
                min_idx = j
        shuffled[i], shuffled[min_idx] = list(
            shuffled[i]), list(shuffled[min_idx])
        shuffled[i][1], shuffled[min_idx][1] = shuffled[min_idx][1], shuffled[i][1]
        canvas.delete(shuffled[i][0])
        shuffled[i] = canvas.create_rectangle(
            shuffled.index(shuffled[i]) * 10, 200, shuffled.index(shuffled[i]) * 10 + 10, shuffled[i][1], fill='#00FF00'), shuffled[i][1]
        canvas.delete(shuffled[min_idx][0])
        shuffled[min_idx] = canvas.create_rectangle(
            shuffled.index(shuffled[min_idx]) * 10, 200, shuffled.index(shuffled[min_idx]) * 10 + 10, shuffled[min_idx][1], fill='#00FF00'), shuffled[min_idx][1]
        root.update_idletasks()
        time.sleep(updateTime)


root = tk.Tk()

blues = tk.Frame()
blues.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
canvas = tk.Canvas(blues, width=500, height=200)
shuffle()
canvas.pack(fill=tk.BOTH, expand=1)

tk.Button(root, text='Heap Sort', command=lambda: heap_sort(zipped),
          width=20, height=5).grid(row=1, column=0)
tk.Button(root, text='Quick Sort', command=lambda: quick_sort(
    zipped, 0, len(zipped) - 1), width=20, height=5).grid(row=1, column=1)
tk.Button(root, text='Shuffle', command=shuffle,
          width=20, height=5).grid(row=1, column=3)
tk.Button(root, text='Bubble Sort', command=lambda: bubble_sort(zipped),
          width=20, height=5).grid(row=2, column=0, pady=10)
tk.Button(root, text='Selection Sort', command=lambda: selection_sort(
    zipped), width=20, height=5).grid(row=2, column=1, pady=10)

root.geometry('500x420+300+300')
root.title('Sorting Algorithms')
root.mainloop()
