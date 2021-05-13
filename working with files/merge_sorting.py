from time import time
import numpy as np

simple_list = [5, 1, 3, 8, 4, 7, 2, 9, 0, 6]
np.random.seed(0)
big_list = np.random.permutation(1000)
# big_list = np.random.permutation(100000)
first = simple_list[0]


def strive_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            if l[i] <= l[j]:

                l[i], l[j] = l[j], l[i]

    return l


def buble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j+1] < l[j]:

                l[j], l[j+1] = l[j+1], l[j]
    return l


def partition(l, low, high):

    i = low - 1
    pivot = l[high]

    for j in range(low, high):

        if l[j] < pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[high] = l[high], l[i+1]
    return i+1


def quick_sort(left, right, l):

    if left < right:
        pivot = partition(l, left, right)
        quick_sort(left, pivot-1, l)
        quick_sort(pivot+1, right, l)


def mergeSort(arr):
    if len(arr) > 1:

        r = len(arr)//2
        left = arr[:r]
        right = arr[r:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    sample_list = [5, 1, 3, 8, 4, 7, 2, 9, 0, 6]

    print("Original array")
    display(sample_list)

    mergeSort(sample_list)

    print("MergeSort array")
    display(sample_list)


# bubble sort

# start = time()
# buble_sort(big_list)
# end = time()
# print("Buble took: ", end-start, "s")


# Strive sort

# start = time()
# strive_sort(big_list)
# end = time()
# print("Strive took: ", end-start, "s")


# quick sort

# start = time()
# quick_sort(0, len(big_list)-1,big_list)
# # print(big_list)
# end = time()
# print("QuickSort took: ", end-start, "s")


# merge sort

start = time()
mergeSort(big_list)
end = time()

print("MergeSort took: ", end-start, "s")
