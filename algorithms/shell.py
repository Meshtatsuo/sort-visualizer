import matplotlib.pyplot as plot
import numpy as np

# Algorithm from tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
# Modified to add the visualization

def shellSort(x, list, playbackSpeed):

    gap = len(list) // 2
    while gap > 0:
        plot.bar(x,list, color=(0.6, 0.4, 0.6, 1))
        plot.pause(playbackSpeed)
        plot.clf()
        for i in range(gap, len(list)):
            temp = list[i]
            j = i

# Sort sub list for gap
    while j >= gap and list[j-gap] > temp:
        list[j] = list[j-gap]
        j = j-gap
        list[j] = temp
        plot.bar(x,list, color=(0.6, 0.4, 0.6, 1))
        plot.pause(playbackSpeed)
        plot.clf()
# Reduce the gap for the next element
    gap = gap//2
    return