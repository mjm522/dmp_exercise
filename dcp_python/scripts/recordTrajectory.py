import pygame

bgcolor = 0, 0, 0
blueval = 0
bluedir = 1
x = y = 0
running = 1
screen = pygame.display.set_mode((640, 400))

pointlist = []
count = 0

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
        count += 1
        pointlist.append([x,y])
        
 
    screen.fill(bgcolor)
    pygame.draw.line(screen, (0, 0, blueval), (x, 0), (x, 399))
    pygame.draw.line(screen, (0, 0, blueval), (0, y), (639, y))

    if count > 1:
    #since atleat this function needs two points
        pygame.draw.lines(screen, (255, 0, 0), False, pointlist, 5)
    
    blueval += bluedir
    if blueval == 255 or blueval == 0: bluedir *= -1
    pygame.display.flip()