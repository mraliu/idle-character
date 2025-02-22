# gap of 6px

import pygame

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Pygame Window")

ryu_surf = pygame.image.load("ryu.gif")
ryu_surf.set_colorkey((112,136,136))
ryu_crop_size = pygame.Rect(6, 18, 43, 81)

ryu_crop = ryu_surf.subsurface(ryu_crop_size)
ryu_crop1 = ryu_surf.subsurface(ryu_crop_size)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    screen.blit(ryu_crop, (w/2, h/2))
    pygame.display.update()

pygame.quit()