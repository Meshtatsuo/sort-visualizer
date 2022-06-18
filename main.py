import matplotlib.pyplot as plot
import numpy as np
import sys

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
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            plot.bar(x,list, color=(0.6, 0.4, 0.6, 1))
            plot.pause(playbackSpeed)
            
            plot.clf()
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
else:
    print("Please enter a valid sort algorithm, We currently support:")
    print("- bubble")
    

print("Finished!")
plot.show()
