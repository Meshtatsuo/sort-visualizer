import sys

from algorithms.bubble import *

dataSize = int(sys.argv[2])
playbackSpeed = .001
sortType = str(sys.argv[1])
sortType = sortType.lower()
print(sortType)

list= np.random.randint(0, 100, dataSize)
x = np.arange(0,dataSize,1)

print("Launching visualizer for sorting with type: ", sortType)

# bubble sort
if sortType == "bubble":
    bubbleSort(x,list, playbackSpeed)
    
else:
    print("Please enter a valid sort algorithm, We currently support:")
    print("- bubble")
    

print("Finished!")
plot.show()
