import pygame
#how to use: The script starts with a window, press the left button to start
#recording of the trajectory and click again to stop th recording.

import numpy as np 

bgcolor = 0, 0, 0
blueval = 0
bluedir = 1
x = y = 0
running = 1
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 640
PPM = 100.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pointlist = []
traj_to_save = []
count = 0

start = False

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    
    if pygame.mouse.get_pressed()[0]:
        if not start:
            start = True
        else:
            start = False

    if (event.type == pygame.MOUSEMOTION) and start:
        x, y = event.pos
        if (0 < x < 639) and (0 < y < 399):
            count += 1
            pointlist.append([x,y])
            traj_to_save.append([float(x)/PPM, float(SCREEN_HEIGHT-y)/PPM])

        
    screen.fill(bgcolor)
    pygame.draw.line(screen, (0, 0, blueval), (x, 0), (x, 399))
    pygame.draw.line(screen, (0, 0, blueval), (0, y), (639, y))

    if count > 1:
    #since atleat this function needs two points
        pygame.draw.lines(screen, (255, 0, 0), False, pointlist, 5)
    
    blueval += bluedir
    if blueval == 255 or blueval == 0: bluedir *= -1
    pygame.display.flip()

pointlist = np.asarray(pointlist)
traj_to_save = np.asarray(traj_to_save)
np.savetxt('recorded_trajectory.txt', traj_to_save)