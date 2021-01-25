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
NUM_RECT = 4


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/link.png")

        self.image = pygame.transform.scale(self.image, (32,44))

        self.rect = self.image.get_rect()


    def update(self):
        """Move the player with the mouse"""
        self.rect.center = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/wall.png")

        self.image = pygame.transform.scale(self.image, (155, 41))
        self.rect = self.image.get_rect()


        self.x_vel = 3

    def update(self):
        """Move rectangle side to side"""
        self.rect.x += self.x_vel

        # keep enemy in the screen
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_vel *= -1

class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((35,20))
        self.image.fill((100, 255, 100))

        self.rect = self.image.get_rect()


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
    enemy_group = pygame.sprite.Group()
    jewel_group = pygame.sprite.Group()

    # enemy creation
    for i in range(NUM_RECT):
        enemy = Enemy()
        enemy.rect.x = random.randrange(WIDTH - enemy.rect.width)
        enemy.rect.y = random.randrange(HEIGHT - enemy.rect.height)
        all_sprites.add(enemy)
        enemy_group.add(enemy)

    # --- player
    player = Player()
    all_sprites.add(player)

    # --- jewel
    jewel = Jewel()
    all_sprites.add(jewel)
    jewel_group.add(jewel)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()

        # player collides with enemy
        enemy_hit = pygame.sprite.spritecollide(player, enemy_group, False)
        if len(enemy_hit) > 0:
            player.kill()

        # player collide with jewel
        jewel_collected = pygame.sprite.spritecollide(player, jewel_group, True)

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()