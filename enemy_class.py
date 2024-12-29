import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.w, self.h = w, h
        self.image = pygame.image.load(f'image/Bullet.png')  # импортируе картику
        self.image = pygame.transform.rotozoom(self.image, 1, 0.1)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 100
        self.speedy = 10

    def update(self):
        self.move()
        if self.rect.bottom > self.h:
            self.kill()

    def move(self):
        self.rect.y += self.speedy
