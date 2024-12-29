import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(f'image/Bullet.png')  # импортируе картику
        self.image = pygame.transform.rotozoom(self.image, 1, 0.1)
        self.rect = self.image.get_rect()
        self.rect.centery = y
        self.rect.centerx = x
        self.speed = 10

    def update(self):
        self.move()
        if self.rect.bottom < 0:
            self.kill()

    def move(self):
        self.rect.y -= self.speed
