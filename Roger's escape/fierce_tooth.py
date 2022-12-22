import pygame
from pygame.locals import *
from module_2d import *
from rigidbody import *
from enemy import *
class Fierce_Tooth(Enemy):
    def __init__(self, startPos, platform,thin, rectSize, rectLocalPos):
        idle = Sprite_State(startPos,102,90,
        'asset/enemy/fierce_tooth/idle/1.png',
        'asset/enemy/fierce_tooth/idle/2.png',
        'asset/enemy/fierce_tooth/idle/3.png',
        'asset/enemy/fierce_tooth/idle/4.png',
        'asset/enemy/fierce_tooth/idle/5.png',
        'asset/enemy/fierce_tooth/idle/6.png',
        'asset/enemy/fierce_tooth/idle/7.png',
        'asset/enemy/fierce_tooth/idle/8.png')
        run = Sprite_State(startPos,102,90,
        'asset/enemy/fierce_tooth/run/1.png',
        'asset/enemy/fierce_tooth/run/2.png',
        'asset/enemy/fierce_tooth/run/3.png',
        'asset/enemy/fierce_tooth/run/4.png',
        'asset/enemy/fierce_tooth/run/5.png',
        'asset/enemy/fierce_tooth/run/6.png')
        hit = Sprite_State(startPos,102,90,
        'asset/enemy/fierce_tooth/hit/1.png',
        'asset/enemy/fierce_tooth/hit/2.png',
        'asset/enemy/fierce_tooth/hit/3.png',
        'asset/enemy/fierce_tooth/hit/4.png')
        super().__init__(startPos, platform,thin, rectSize, rectLocalPos, idle,run, hit)