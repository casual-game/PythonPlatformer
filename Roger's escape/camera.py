import pygame
import random
from pygame.locals import *
from module_2d import *

class Camera():
    def __init__(self,startPos,speed,screenWidth,screenHeight):
        self.x=startPos[0]
        self.y=startPos[1]
        self.speed = speed
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.time =0
        self.shakeTime = 0
    def Shake(self):
        self.shakeTime = self.time + 0.2
    def MoveTo(self,position):
        self.x = Clamp(-self.screenWidth+1280,0,position[0]+640-96)
        self.y = Clamp(-self.screenHeight+720,0,position[1]+360+32)
    def Update(self,position,time,deltaTime):
        self.time = time
        moveSpeed = self.speed*deltaTime
        self.x = Lerp(self.x,position[0]+640-96,moveSpeed)
        self.y = Lerp(self.y,position[1]+360+32,moveSpeed)
        self.x = Clamp(-self.screenWidth+1280,0,self.x)
        self.y = Clamp(-self.screenHeight+720,0,self.y)
        if self.shakeTime>self.time: return  (self.x+random.randrange(-10,10),self.y+random.randrange(-10,10))
        else: return  (self.x,self.y)
