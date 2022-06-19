
import matplotlib.pyplot as plot
import numpy as np


def updateVisual(x, list, playbackSpeed):
    plot.bar(x, list, color=(0.6, 0.4, 0.6, 1))
    plot.pause(playbackSpeed)
    plot.clf()

# Python program for implementation of MergeSort
def mergeSort(x, arr, playbackSpeed):
	print(x)
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2


		##updateVisual(x, arr, playbackSpeed)

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]


		# Sorting the first half
		mergeSort(x, L, playbackSpeed)

		# Sorting the second half
		mergeSort(x, R, playbackSpeed)

		merge(x, arr, L, R, playbackSpeed)


def merge(x, arr, L, R, playbackSpeed):
	##updateVisual(len(x), arr, playbackSpeed)

	
	i = j = k = 0

	# Copy data to temp arrays L[] and R[]
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Checking if any element was left
	while i < len(L):
		arr[k] = L[i]
		i += 1
		k += 1

	while j < len(R):
		arr[k] = R[j]
		j += 1
		k += 1

# Code to print the list

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()


def beginMergeSort(x, arr, playbackSpeed):
	global initArr
	initArr = arr
	updateVisual(x, arr, playbackSpeed)
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(x, arr, playbackSpeed)
	print("Sorted array is: ", end="\n")
	printList(arr)
	updateVisual(x, arr, playbackSpeed)
	return

# This code is contributed by Mayank Khanna
