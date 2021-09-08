import pygame
import sys
from arr_gen import *
from Merge_sort import *


# Initializing the pygame
pygame.init()
# pygame.font.init()
# Creating the screen/window 
screen = pygame.display.set_mode((800,600))

# Title and display of the window
pygame.display.set_caption("Sorting visualizer")
icon = pygame.image.load(r'C:\Users\USER\Desktop\def\pygame_T\logo.png')
pygame.display.set_icon(icon)


running = True
# Game Loop
while running:

    # background
    screen.fill((32, 38, 40))

    # Event handler stores all event 
    for event in pygame.event.get():

        # If we click Close button in window
        if event.type == pygame.QUIT:
            sys.exit()
            # running = False
            # break

        if event.type == pygame.KEYDOWN:
            # if event.type == pygame.QUIT:
                # sys.exit() 
                
            if event.key == pygame.K_r:
                generate_arr() 

            if event.key == pygame.K_RETURN:
                mergesort(array, 1, len(array)-1)   

    
    draw()
    pygame.display.update()
      
pygame.QUIT



    # # Screen colour
    # # Tuple => RGB(red,green,blue)
    # screen.fill((10, 5, 56)) #Everytime there is any kind of update on the pygame screen, 
    #                          #i'll have to write update(such as at the end of the loop)
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False
    #         break
    # pygame.display.update()