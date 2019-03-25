import pygame

FILL = (255, 255, 255)

spritelist = pygame.sprite.Group()

class Background(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image.fill

class Character(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface([50, 50])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

pygame.init()
screen = pygame.display.set_mode([1000, 600])
pygame.display.set_caption('Game')

background = ("INSERT BACKGROUND IMAGE HERE")
char_1 = Character(FILL, 300, 300)
spritelist.add(char_1)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    spritelist.draw(screen)
    pygame.display.flip()
pygame.quit()