import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))  # Placeholder image
        self.image.fill((255, 0, 0))  # Red color for the player
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.5

    def update(self):
        self.apply_gravity()
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

    def apply_gravity(self):
        self.velocity_y += self.gravity
