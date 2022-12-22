import pygame
from pygame.locals import *
from module_2d import *
from rigidbody import *
from enemy import *
class Blue_Bird(Enemy):
    def __init__(self, startPos, platform,thin, rectSize, rectLocalPos):
        idle = Sprite_State(startPos,96,96,
        'asset/enemy/blue_bird/idle/1.png',
        'asset/enemy/blue_bird/idle/2.png',
        'asset/enemy/blue_bird/idle/3.png',
        'asset/enemy/blue_bird/idle/4.png',
        'asset/enemy/blue_bird/idle/5.png',
        'asset/enemy/blue_bird/idle/6.png',
        'asset/enemy/blue_bird/idle/7.png',
        'asset/enemy/blue_bird/idle/8.png')
        hit = Sprite_State(startPos,96,96,
        'asset/enemy/blue_bird/hit/1.png',
        'asset/enemy/blue_bird/hit/2.png',
        'asset/enemy/blue_bird/hit/3.png',
        'asset/enemy/blue_bird/hit/4.png')
        super().__init__(startPos, platform,thin, rectSize, rectLocalPos, idle, hit)