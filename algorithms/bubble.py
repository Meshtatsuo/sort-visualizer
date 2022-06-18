import matplotlib.pyplot as plot
import numpy as np


def bubbleSort(x,list, playbackSpeed):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            plot.bar(x,list, color=(0.6, 0.4, 0.6, 1))
            plot.pause(playbackSpeed)
            plot.clf()
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return