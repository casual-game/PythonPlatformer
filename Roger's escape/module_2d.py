import pygame
from pygame.locals import *
import math


class Sprite_Default(pygame.sprite.Sprite):
    def __init__(self, position,width,height):
        super(Sprite_Default, self).__init__()
        self.size = (width, height)
    def update(self):
        pass
class Sprite_Single(Sprite_Default):
    def __init__(self, position, width, height,sprite):
        super().__init__(position, width, height)
        self.position = position
        self.image = pygame.image.load(sprite)
        self.image.convert()
        # rect 만들기
        self.rect = pygame.Rect(position, self.size)
        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.image = pygame.transform.scale(self.image, self.size)
class Sprite_State(Sprite_Default):
    def __init__(self, position,width,height,*sprites):
        super().__init__(position,width,height)
        self.position = position
        self.speed = 0.2
        self.tick = None
        self.callbacks =[]#[인덱스,콜백함수] 의 리스트로 구성
        self.flipped = False
        self.images = []
        self.flippedImages = []
        self.loop = True
        for spr in sprites:
            img = pygame.image.load(spr)
            img.convert()
            self.images.append(img)
            self.flippedImages.append(pygame.transform.flip(img, True, False))

        # rect 만들기
        self.rect = pygame.Rect(position, self.size)
        # Rect 크기와 Image 크기 맞추기. pygame.transform.scale
        self.images = [pygame.transform.scale(image, self.size) for image in self.images]
        self.flippedImages = [pygame.transform.scale(image, self.size) for image in self.flippedImages]
        # 캐릭터의 첫번째 이미지
        self.index = 0
        self.image = self.images[self.index]  # 'image' is the current image of the animation.
    def Flip(self,flip):
        self.flipped = flip
    def update(self):
        super().update()
        #Tick
        if self.tick !=None: self.tick()
        #Index 콜백함수
        lastindex = self.index
        self.index += self.speed
        for callback in self.callbacks:
            if lastindex< callback[0] <= self.index:
                callback[1]()

        if self.index >= len(self.images):
            if self.loop: self.index = 0
            else: self.index = len(self.images)-1
        if self.flipped: self.image = self.flippedImages[math.floor(self.index)]
        else: self.image = self.images[math.floor(self.index)]

def Lerp(x1,x2,ratio):
    return x1*(1-ratio) + x2*ratio
def Clamp(min,max,value):
    if min>value: return min
    elif max<value: return max
    else: return value