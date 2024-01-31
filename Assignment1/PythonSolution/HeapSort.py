# Reference: followed book pages posted on canvas and lectures/powerpoint
import random
import time

def HeapSort(A):
    steps = 0
    steps += BuildMaxHeap(A)
    A_heapsize = len(A)
    steps += 2
    for i in range(A_heapsize, 1, -1):
        A[i-1], A[0] = A[0], A[i-1]
        A_heapsize = A_heapsize - 1
        steps += MaxHeapify(A, 1, A_heapsize)
        steps += 3
    return steps

def BuildMaxHeap(A):
    A_heapsize = len(A)
    steps = 1
    for i in range(A_heapsize//2, 0, -1):
        steps += MaxHeapify(A, i, A_heapsize)
        steps += 1
    return steps

def MaxHeapify(A, i, heapsize):
    l = Left(i)
    r = Right(i)
    steps = 2
    if l <= heapsize and A[l-1] > A[i-1]:
        largest = l
        steps += 1
    else:
        largest = i
        steps += 1
    if r <= heapsize and A[r-1] > A[largest-1]:
        largest = r
        steps += 1
    if largest != i:
        A[i-1], A[largest-1] = A[largest-1], A[i-1]
        steps += MaxHeapify(A, largest, heapsize)
        steps += 2
    return steps

def Left(i):
    return 2*i

def Right(i):
    return (2*i) + 1


def plotTime(sizes_of_lists):
    for size in sizes_of_lists:
        list_to_be_sorted = [random.randint(0, 1000) for _ in range(size)]
        start_time = time.time()
        HeapSort(list_to_be_sorted)
        endtime = time.time()
        elapsedtime = endtime - start_time
        print("Execution Time for list of size " + str(size) + " : " + str(elapsedtime))


if __name__ == "__main__":
    sizes_of_lists = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    plotTime(sizes_of_lists)