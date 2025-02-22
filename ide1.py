# gap of 6px

charx = 6
chary = 18
charw = 43
charh = 81

import pygame

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Pygame Window")

ryu_surf = pygame.image.load("ryu.gif")
ryu_surf.set_colorkey((112,136,136))


ryu = []
for i in range(4):
    ryu.append(ryu_surf.subsurface((charx*(i+1)+(charw*i), chary, charw, charh)))




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for idx, y in enumerate(ryu):
        screen.blit(y, ((w/2)+idx*charw, h/2))


    # screen.blit(ryu[3], (w/2, h/2))
    pygame.display.update()

pygame.quit()