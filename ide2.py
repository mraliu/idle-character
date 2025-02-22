# gap of 6px


import pygame

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Simple Pygame Window")

charx = 6  # gap between the side edge of the sprite to the first sprite x axis
chary = 18 # gap between the top edge of the sprite to the first sprite y axis
charw = 43 # the width of the sprite
charh = 81 # the height of the sprite


ryu_surf = pygame.image.load("ryu.gif") # Load the sprite sheet in
ryu_surf.set_colorkey((112,136,136)) # Set the transparent colour of the sprite sheet

ryu = [] # An array to store the cropped individuals sprites from the sprite sheet

for i in range(4): # Loop to cycle through the first 4 sprites of the sprite sheet cropping and storing them into individual items in array
    ryu.append(ryu_surf.subsurface((charx*(i+1)+(charw*i), chary, charw, charh))) # append the cropped sprite into array

count = 0
fps = 30
clock = pygame.time.Clock() # Setup the clock to use fps 

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

    screen.blit(ryu[count], (w/2, h/2)) # Print out the sprite

    

    clock.tick(fps)
    pygame.display.update()

pygame.quit()