import pygame
import random

pygame.font.init()
# Initializing variables needed for generating array
screen = pygame.display.set_mode((800, 600))


array = [0]*151

arr_clr = [(28, 186, 255)]*151

clr_ind = 0

clr = [(28, 186, 255), (255, 0, 0), (0, 0, 153), (255, 102, 0)]

fnt = pygame.font.SysFont("Times New Roman", 20)
fnt1 = pygame.font.SysFont("Helvetica", 10)


width = 800
length = 600

# Draw the array values


def draw():
    # Text should be rendered
    txt = fnt.render("SORTING VISUALIZER", True, (0, 255, 255))
    # Position where text is placed
    # Blit basically means to draw
    screen.blit(txt, (20, 20))

    txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY", True, (243, 250, 63))
    screen.blit(txt1, (20, 45))

    menu = ["Press:", "'1' for Merge Sort",
            "'2' for Quick Sort", "'3' for Selection Sort", "'4' for Heap Sort", "'5' for bubble sort"]
    lab = []
    idx = 0
    for line in menu:
        lab.append(fnt1.render(line, 1, (243, 250, 63)))
        screen.blit(lab[idx], (550, 15+(idx*15)))
        idx += 1

    element_width = (width-150)//150
    boundry_arr = 800 / 150
    boundry_grp = 600 / 100

    # This is the dividing upper navbar and lower array rep. section position
    pygame.draw.line(screen, (255, 255, 255), (0, 105), (800, 105), 6)

    for i in range(1, 100):
        pygame.draw.line(screen, (0, 24, 224), (0, boundry_grp *
                         i + 110), (800, boundry_grp * i + 110))

    # Drawing the array values as lines
    for i in range(1, 151):
        pygame.draw.line(screen, arr_clr[i], (boundry_arr * i-3, 110),
                         (boundry_arr * i-3, array[i]*boundry_grp + 110), element_width)


# Generate new Array
def generate_arr():
    for i in range(1, 151):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 100)


def refill():
    screen.fill((32, 38, 40))
    draw()
    pygame.display.update()
    pygame.time.delay(20)
