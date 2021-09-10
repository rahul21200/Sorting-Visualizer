import pygame
from arr_gen import *

#Generate random array
generate_arr()

def bubble(array):
    pygame.event.pump()

    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            arr_clr[j] = clr[2]
            if array[j] > array[j+1] :
                arr_clr[i] = clr[1]
                arr_clr[j] = clr[1]
                refill()
                arr_clr[i]= clr[0]
                arr_clr[j]= clr[0]
                min_idx = j 
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            arr_clr[j] = clr[0]
        if swapped == False:
            break
        for k in range(i+1):
            arr_clr[k] = clr[3]
    for i in range(len(array)):
        arr_clr[i] = (0,255,0)
    refill()


    # # min_idx = i
    # for i in range(len(array)):
    #     min_idx = i
    #     for j in range(i+1, len(array)):
    #         arr_clr[j] = clr[2]
    #         if array[min_idx] > array[j]:
    #             arr_clr[i] = clr[1]
    #             arr_clr[j] = clr[1]
    #             refill()
    #             arr_clr[i]= clr[0]
    #             arr_clr[j]= clr[0]
    #             min_idx = j   
    #         arr_clr[j] = clr[0]
    #     array[i], array[min_idx] = array[min_idx], array[i]

    #     for k in range(i+1):
    #         arr_clr[k] = clr[3]

    # for i in range(len(array)):
    #     arr_clr[i] = (0,255,0)
    # refill()
