# Overview

This program showcases the functionality of four sorting algorithms: heap sort, quick sort, bubble sort, and selection sort. Users can control the animation speed of the sorting process by adjusting the speed slider. Before starting the sorting, the user can shuffle the bars to observe different sorting results.
# Problems Faced

When implementing the quick sort algorithm, I faced a challenge with overlapping bars in the program's visualization. The issue arose due to the way the program was designed to handle bar swaps visually. The program was designed to delete bar A from the screen, followed by bar B, and then redraw each bar in the other bar's previous spot. If a swap occurred with just one bar, that bar would be deleted twice and then redrawn twice, causing a duplicate on the screen.

After a thorough inspection, I realized that the problem was sometimes the algorithm was swapping a bar with itself, which would result in a duplicate bar. To resolve this issue, I added a check to the program to ensure that before making a swap, the bars being swapped were evaluated to not be the same. This simple addition significantly improved the visual representation of the quick sort algorithm and eliminated any overlapping bar issues.
# Learning Outcomes

I gained a deeper understanding of different sorting algorithms and the process of implementing them in a program. Additionally, I learned how to use the Python tkinter GUI library and update the user interface while executing algorithms. 
