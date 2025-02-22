import pygame


class Character():

    def __init__(self, image: str, x: int, y: int, w: int, h: int, scale: int, num_sprites: int, colorkey: tuple):
        self.image = image
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.scale = scale
        self.colorkey = colorkey
        self.surf = pygame.image.load(self.image) # Load the sprite sheet in
        self.surf.set_colorkey(self.colorkey) # Set the transparent colour of the sprite sheet
        self.sprite = []
        self.num_sprites = num_sprites

        for i in range(self.num_sprites):
            sprite = self.surf.subsurface((self.x*(i+1)+(self.w*i), self.y, self.w, self.h))
            self.sprite.append(pygame.transform.scale(sprite, (self.w*self.scale, self.h*self.scale)))