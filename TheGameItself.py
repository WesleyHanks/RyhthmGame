import pygame, random, math, sys
pygame.init()

WIDTH = 1000
HEIGHT = 1000
DISPLAY = pygame.display.set_mode([WIDTH, HEIGHT])

BGGREY = (164,164,164)


def clampVal(min, max, val):
    if val < min:
        return min
    elif val > max:
        return max
    else:
        return val

colorVal1 = 510
colorVal2 = 0
colorVal3 = 0

mode1 = 1
mode2 = 1
mode3 = 0

exitSwitch = False

while not(exitSwitch):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if mode1 == 0:
        colorVal1 += 1
    if mode1 == 1:
        colorVal1 -= 1
    if colorVal1 >= 510:
        mode1 = 1
    if colorVal1 <= -255:
        mode1 = 0
    
    if mode2 == 0:
        colorVal2 += 1
    if mode2 == 1:
        colorVal2 -= 1
    if colorVal2 >= 510:
        mode2 = 1
    if colorVal2 <= -255:
        mode2 = 0

    if mode3 == 0:
        colorVal3 += 1
    if mode3 == 1:
        colorVal3 -= 1
    if colorVal3 >= 510:
        mode3 = 1
    if colorVal3 <= -255:
        mode3 = 0

    

    DISPLAY.fill((clampVal(0, 255, colorVal1), clampVal(0, 255, colorVal2), clampVal(0, 255, colorVal3)))
    print((colorVal1, colorVal2, colorVal3))

    pygame.display.update()