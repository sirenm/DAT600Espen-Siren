# Reference: followed book pages posted on canvas and lectures/powerpoint
import matplotlib.pyplot as plt
import random
import time

def InsertionSort(A):
    steps = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        steps += 2
        while j > -1 and A[j] > key:
            A[j + 1] = A[j]
            j = j-1
            steps += 2
        A[j + 1] = key
        steps += 1
    return steps

def plotTime(sizes_of_lists):
    for size in sizes_of_lists:
        list_to_be_sorted = [random.randint(0, 1000) for _ in range(size)]
        start_time = time.time()
        InsertionSort(list_to_be_sorted)
        endtime = time.time()
        elapsedtime = endtime - start_time
        print("Execution Time for list of size " + str(size) + " : " + str(elapsedtime))


if __name__ == "__main__":
    sizes_of_lists = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    plotTime(sizes_of_lists)

