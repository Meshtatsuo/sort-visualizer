import sys
import time
from tracemalloc import start

from algorithms.bubble import *
from algorithms.insertion import *

dataSize = int(sys.argv[2])
playbackSpeed = .1
sortType = str(sys.argv[1])
sortType = sortType.lower()

list= np.random.randint(0, 100, dataSize)
x = np.arange(0,dataSize,1)

def calculateAndDisplayTime():
    elapsed = endTime - startTime
    
    return


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
        print("- bubble")
        return
    

print("Launching visualizer for sorting with type: ", sortType)
elapsed = beginSort()
print("Finished!")
print("Sorting using ", sortType, " took: ", elapsed, " seconds.")
plot.show()
