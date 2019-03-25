import pygame
from random import *
FILL = (255, 255, 255)
FILL_1 = (255, 0 , 0)

spritelist = pygame.sprite.Group()
sprite = []

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Character(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

pygame.init()
screen = pygame.display.set_mode([875, 525])
pygame.display.set_caption('Game')

background = Background("background_initial.png", [0,0])
x = 200
y = 300
char_1 = Character(FILL, x, y)
spritelist.add(char_1)
sprite.append(char_1)

enemy_1 = Character(FILL_1, 100, 100)
spritelist.add(enemy_1)

clock = pygame.time.Clock()
done = False
while not done:
    x_change = 0
    y_change = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -5
            y_change = 0
        if event.key == pygame.K_RIGHT:
            x_change = 5
            y_change = 0
        if event.key == pygame.K_UP:
            x_change = 0
            y_change = -5
        if event.key == pygame.K_DOWN:
            x_change = 0
            y_change = 5

    old_sprite = sprite.pop()
    spritelist.remove(old_sprite)
    x = x + x_change
    y = y + y_change
    char_1 = Character(FILL, x, y)
    sprite.append(char_1)
    spritelist.add(char_1)

    screen.fill([255, 255, 255])
    screen.blit(background.image, background.rect)
    spritelist.draw(screen)
    pygame.display.flip()
pygame.quit()