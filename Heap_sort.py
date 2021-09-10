import pygame
from arr_gen import *

generate_arr()

# Heap sort algorithm
def heapSort(array):
    n = len(array)
    for i in range(n//2-1, -1, -1):
        pygame.event.pump()
        heapify(array, i, n)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        arr_clr[i] = clr[1]
        refill()
        heapify(array, 0, i)
    refill()
  
# Helper function
def heapify(array, root, size):
    left = root * 2 + 1
    right = root * 2 + 2
    largest = root
    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != root:
        arr_clr[largest] = clr[2]
        arr_clr[root] = clr[2]
        array[largest],\
        array[root] = array[root],\
        array[largest]
        refill()
        arr_clr[largest] = clr[0]
        arr_clr[root] = clr[0]
        heapify(array, largest, size)
        refill()