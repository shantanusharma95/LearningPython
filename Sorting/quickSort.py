import math
import sys
import time

def partition(arr,start,end):
    pivot = arr[end]
    p_index = start
    for i in range(start,end):
        if arr[i]<=pivot:
            arr[i],arr[p_index] = arr[p_index],arr[i]
            p_index += 1
    arr[p_index],arr[end]=arr[end],arr[p_index]
    return p_index

def quickSort(arr,start,end):
    if start<end:
        p_index = partition(arr,start,end)
        quickSort(arr,start,p_index-1)
        quickSort(arr,p_index,end)

def main():
    print("Welcome to Quick sort!/nEnter elements to be sorted separated by a space, and press enter to sort.")
    #arr = list(map(int, input().split()))
    arr = [7,2,1,6,8,5,3,4]

    start_time = time.perf_counter()
    quickSort(arr,0,len(arr)-1)
    stop_time = time.perf_counter()
    
    print("\n\nAfter sorting - \n\n")
    print(arr)
    print("\n\n Sorted in time - ", start_time-stop_time)

if __name__=='__main__':
    main()
