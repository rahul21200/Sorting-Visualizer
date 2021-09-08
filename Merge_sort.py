import pygame
from arr_gen import *

# Importing the random array
generate_arr() 

# Main Recursive function 
def mergesort(array, l, r):
    mid =(l + r)//2
    if l<r:
        mergesort(array, l, mid)
        mergesort(array, mid + 1, r)
        merge(array, l, mid, mid + 1, r)


# Helper function(Insort is taking place)
def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp =[]
    # pygame.event.pump()
    # For each frame of your game, you will need to make some sort of call to the event queue.
    # This ensures your program can internally interact with the rest of the operating system.
    pygame.event.pump() 

    ################# Merging 2 sorted arrays ######################## 
    while i<= y1 and j<= y2:
        arr_clr[i]= clr[1]
        arr_clr[j]= clr[1]
        refill()
        arr_clr[i]= clr[0]
        arr_clr[j]= clr[0]
        if array[i]<array[j]:
                temp.append(array[i])
                i+= 1
        else:
                temp.append(array[j])
                j+= 1

    while i<= y1:
        arr_clr[i]= clr[1]
        refill()
        arr_clr[i]= clr[0]
        temp.append(array[i])
        i+= 1

    while j<= y2:
        arr_clr[j]= clr[1]
        refill()
        arr_clr[j]= clr[0]
        temp.append(array[j])
        j+= 1
    #####################################################################

    j = 0    
    for i in range(x1, y2 + 1): 
        pygame.event.pump() 
        array[i]= temp[j]
        j+= 1
        arr_clr[i]= clr[2]
        refill()
        if y2-x1 == len(array)-2:
            arr_clr[i]= clr[3]
        else: 
            arr_clr[i]= clr[0]
