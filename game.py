import pygame
from player import Player
from game_platform import Platform

class Game:
    def __init__(self, window):
        self.window = window
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.player = Player(100, 100)
        self.all_sprites.add(self.player)

        self.platform = Platform(200, 400, 200, 20)
        self.all_sprites.add(self.platform)
        self.platforms.add(self.platform)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.handle_input()
            self.update()
            self.render()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.velocity_x = -5
        elif keys[pygame.K_RIGHT]:
            self.player.velocity_x = 5
        else:
            self.player.velocity_x = 0

    def update(self):
        self.all_sprites.update()
        self.check_collisions()

    def check_collisions(self):
        # Check collision between player and platforms
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.rect.y = hits[0].rect.y - self.player.rect.height
            self.player.velocity_y = 0

    def render(self):
        self.window.fill((0, 0, 0))  # Clear the screen

        self.all_sprites.draw(self.window)

        pygame.display.flip()
