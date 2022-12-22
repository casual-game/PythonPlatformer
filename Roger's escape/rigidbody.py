import pygame
from pygame.locals import *
from module_2d import *
class Rigidbody():
    def __init__(self,startPos,platform,thin,rectSize,rectLocalPos):
        self.position = startPos
        self.platform = platform
        self.thin = thin
        self._delta = (0,0)
        self.rect = Rect((startPos[0]+rectSize[0]*0.5+rectLocalPos[0],startPos[1]+rectSize[1]*0.5+rectLocalPos[1]),rectSize)
        self.rectLocalPos = rectLocalPos
    def Move(self,screen,camPos,delta,rect):
        detected_X = False
        detected_Y = False
        self._delta = delta
        if delta[1]!=None: detected_Y = self.Move_V(screen,camPos,delta[1],rect)
        if delta[0]!=None: detected_X = self.Move_H(screen,camPos,delta[0],rect)
        return (detected_X,detected_Y)
            
  
    def Move_V(self,screen,camPos,delta,rect):
        self.position = (self.position[0],self.position[1]+delta)
        _x = abs((self.position[0]+rect.width*0.5)//96 -1)
        _y = abs((self.position[1]+delta+rect.height*0.5)//96 -1)
        colX = rect.width*0.5-self.rect.width*0.5
        colY = rect.height*0.5-self.rect.height*0.5
        detected = None
        while True:
            
            range_X = range(int(Clamp(0,30,_x-1)),int(Clamp(0,30,_x+2)))
            range_Y = range(int(Clamp(0,20,_y-2)),int(Clamp(0,20,_y+1)))
            if self.DetectCollision(screen,camPos,range_X,range_Y,colX,colY):
                detected = delta
                if delta>0:
                    self.position = (self.position[0],self.position[1]-1)
                elif delta<0:
                    self.position = (self.position[0],self.position[1]+1)
            else:
                break
        return detected
    def Move_H(self,screen,camPos,delta,rect):
        self.position = (self.position[0]+delta,self.position[1])
        _x = abs((self.position[0]+rect.width*0.5)//96 -1)
        _y = abs((self.position[1]+delta+rect.height*0.5)//96 -1)
        colX = rect.width*0.5-self.rect.width*0.5
        colY = rect.height*0.5-self.rect.height*0.5
        detected = None
        while True:
            range_X = range(int(Clamp(0,30,_x-1)),int(Clamp(0,30,_x+2)))
            range_Y = range(int(Clamp(0,20,_y-2)),int(Clamp(0,20,_y+1)))
            if self.DetectCollision(screen,camPos,range_X,range_Y,colX,colY):
                detected = delta
                if delta>0:
                    self.position = (self.position[0]-1,self.position[1])
                elif delta<0:
                    self.position = (self.position[0]+1,self.position[1])
            else:
                break
        return detected
    def DetectCollision(self,screen,camPos,range_X,range_Y,colX,colY):
        #pygame.draw.rect(screen,(0,255,0),self.rect)
        for i in range_X:
            for j in range_Y:
                p = self.platform[i][j]
                pt = self.thin[i][j]
                if p!=None:
                    #visualRect = Rect(camPos[0]-p[1],camPos[1]-p[2],96,96)
                    collisionRect = Rect(p[1],p[2],96,96)
                    #currentRect = Rect(self.position[0]-colX*0.5,self.position[1]-colY*0.5,self.rect.width,self.rect.height)
                    currentRect = Rect(self.position[0]-colX*0.5-self.rectLocalPos[0],self.position[1]-colY*0.5-self.rectLocalPos[1],self.rect.width,self.rect.height)
                    #pygame.draw.rect(screen,(0,0,0),visualRect)
                    if currentRect.colliderect(collisionRect): return True
                if pt!=None:
                    collisionRect = Rect(pt[1],pt[2],96,96)
                    beforeRect = Rect(self.position[0]-colX*0.5-self.rectLocalPos[0],self.position[1]-self._delta[1]-colY*0.5-self.rectLocalPos[1],self.rect.width,self.rect.height)
                    currentRect = Rect(self.position[0]-colX*0.5-self.rectLocalPos[0],self.position[1]-colY*0.5-self.rectLocalPos[1],self.rect.width,self.rect.height)
                    if currentRect.colliderect(collisionRect):
                        if self._delta[1]<0:
                            if not beforeRect.colliderect(collisionRect):
                                return True
        return False

        