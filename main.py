# main.py

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Final game"
NUM_RECT = 3

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/link.png")

        self.rect = self.image.get_rect()

    def update(self):
        """Move the player with the mouse"""
        self.rect.center = pygame.mouse.get_pos()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/wall.png")

        self.rect = self.image.get_rect()

        self.x_vel = 3

    def update(self):
        """Move rectangle side to side"""
        self.rect.x += self.x_vel

        # keep enemy in the screen
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_vel *= -1


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprites = pygame.sprite.RenderUpdates()

    # --- enemy
    enemy = Enemy()
    all_sprites.add(enemy)

    # --- player
    player = Player()
    all_sprites.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)


        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()