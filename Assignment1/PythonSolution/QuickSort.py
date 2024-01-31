# Reference: followed book pages posted on canvas and lectures/powerpoint
import matplotlib.pyplot as plt
import random


def QuickSort(A, p, r):
    steps = 0
    if p < r:
        q, steps_from = Partition(A, p, r)
        steps += steps_from
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
        steps += 3
    return steps

def Partition(A, p, r):
    x = A[r]
    i = p-1
    steps = 2
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            steps += 2
    A[i+1], A[r] = A[r], A[i+1]
    steps += 1
    return i+1, steps

