import matplotlib.pyplot as plot
import numpy as np

# Insertion sort code is contributed by Mohit Kumra
# via https://www.geeksforgeeks.org/python-program-for-insertion-sort/

# Modifications to include visualizer
def insertionSort(x, list, playbackSpeed):
 
    # Traverse through 1 to len(list)
    for i in range(1, len(list)):
 
        key = list[i]
 
        # Move elements of list[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < list[j] :
                plot.bar(x, list, color=(.6,.4,.6,1))
                plot.pause(playbackSpeed)
                plot.clf()
                list[j+1] = list[j]
                j -= 1
        list[j+1] = key
    return