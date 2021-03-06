import sys
import time
from tracemalloc import start

from algorithms.bubble import *
from algorithms.insertion import *

def determinePlaybackSpeed(val):
    if val == "slowest":
        return .05
    if val == "slow":
        return .01
    if val == "normal":
        return .005
    if val == "fast":
        return .001
    if val == "fastest":
        return .0001
    else:
        return .005


dataSize = int(sys.argv[2])
playbackSpeed = determinePlaybackSpeed(sys.argv[3])
sortType = str(sys.argv[1])
sortType = sortType.lower()

list= np.random.randint(0, 100, dataSize)
x = np.arange(0,dataSize,1)


def beginSort():
    # bubble sort
    if sortType == "bubble":
        startTime = time.time()
        bubbleSort(x,list, playbackSpeed)
        endTime = time.time()
        duration = endTime - startTime
        return duration
    if sortType == "insertion":
        startTime = time.time()
        insertionSort(x, list, playbackSpeed)
        endTime = time.time()
        duration = endTime - startTime
        return duration
    else:
        print("Please enter a valid sort algorithm, We currently support:")
        print("- Bubble")
        print("- Insertion")
        return
    

print("Launching visualizer for sorting with type: ", sortType)
elapsed = beginSort()
print("Finished!")
print("Sorting using ", sortType, " took: ", elapsed, " seconds.")
plot.show()
