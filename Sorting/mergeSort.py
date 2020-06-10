import math
import sys
import time
from queue import Queue

def mergeSort(arr):
    if len(arr)>1:
        mid = math.floor(len(arr)/2)   

        #sorting the left and right halves after division at mid
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        #ensuring no element is left in each sub list
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def main():
    print("Welcome to Merge sort!/nEnter elements to be sorter separated by a space, and press enter to sort.")
    arr = list(map(int, input().split()))

    start_time = time.perf_counter()
    mergeSort(arr)
    stop_time = time.perf_counter()
    
    print("\n\nAfter sorting - \n\n")
    print(arr)
    print("\n\n Sorted in time - ", start_time-stop_time)
    
if __name__=='__main__':
    main()
