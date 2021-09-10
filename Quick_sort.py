import pygame
from arr_gen import *

# Importing the random array
generate_arr() 

# Quick sort main function
def quicksort(array, l, r):
    if l<r:
        pi = partition(array, l, r)
        quicksort(array, l, pi-1)
        refill()
        for i in range(0, pi + 1):
            arr_clr[i]= clr[3]
        quicksort(array, pi + 1, r)
          
# Function to partition the array
def partition(array, low, high):
    pygame.event.pump() 
    pivot = array[high]
    arr_clr[high]= clr[2]
    i = low-1
    for j in range(low, high):
        arr_clr[j]= clr[1]
        refill()
        arr_clr[high]= clr[2]
        arr_clr[j]= clr[0]
        arr_clr[i]= clr[0]
        if array[j]<pivot:
            i = i + 1
            arr_clr[i]= clr[1]
            array[i], array[j]= array[j], array[i]
    refill()
    arr_clr[i]= clr[0]
    arr_clr[high]= clr[0]
    array[i + 1], array[high] = array[high], array[i + 1] 
      
    return ( i + 1 )