import pygame
from Character import Character

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Sprite")

count = 0
fps = 30
clock = pygame.time.Clock() # Setup the clock to use fps 

ryu = Character("ryu.gif", 6, 18, 43, 81, 2, 4, (112,136,136))

running = True
while running:
    ticks = pygame.time.get_ticks() # Get the frames count
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    if (ticks // fps) % 3 == 0: # Divide the frames by 3 so each 3 second the sprite changes
        if count == 3: # If reaches last array item then reset to 0
            count = 0
        else:
            count+=1 # Increase when not at the end of array

    screen.blit(ryu.sprite[count], (w/2, h/2)) # Print out the sprite

    

    clock.tick(fps)
    pygame.display.update()

pygame.quit()