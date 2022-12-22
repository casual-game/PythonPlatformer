import pygame
from pygame.locals import *
from module_2d import *
from rigidbody import *
from enemy import *
class Pink_Star(Enemy):
    def __init__(self, startPos, platform,thin, rectSize, rectLocalPos):
        idle = Sprite_State(startPos,102,90,
        'asset/enemy/pink_star/idle/1.png',
        'asset/enemy/pink_star/idle/2.png',
        'asset/enemy/pink_star/idle/3.png',
        'asset/enemy/pink_star/idle/4.png',
        'asset/enemy/pink_star/idle/5.png',
        'asset/enemy/pink_star/idle/6.png',
        'asset/enemy/pink_star/idle/7.png',
        'asset/enemy/pink_star/idle/8.png')
        run = Sprite_State(startPos,102,90,
        'asset/enemy/pink_star/run/1.png',
        'asset/enemy/pink_star/run/2.png',
        'asset/enemy/pink_star/run/3.png',
        'asset/enemy/pink_star/run/4.png',
        'asset/enemy/pink_star/run/5.png',
        'asset/enemy/pink_star/run/6.png')
        hit = Sprite_State(startPos,102,90,
        'asset/enemy/pink_star/hit/1.png',
        'asset/enemy/pink_star/hit/2.png',
        'asset/enemy/pink_star/hit/3.png',
        'asset/enemy/pink_star/hit/4.png')
        super().__init__(startPos, platform,thin, rectSize, rectLocalPos, idle,run, hit)