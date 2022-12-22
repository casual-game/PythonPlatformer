import pygame
from pygame.locals import *
from module_2d import *
from rigidbody import *
import random
class Enemy(Rigidbody):
    enemies = []
    def __init__(self,startPos,platform,thin,rectSize,rectLocalPos,state_Idle,state_Run,state_Hit):
        super().__init__(startPos,platform,thin,rectSize,rectLocalPos)
        Enemy.enemies.append(self)
        self.death = False
        self.tick = None
        self.dt = 0.03
        #중력 변수
        self.jumpSpeed = 800
        self.gravity = 0
        self.jumped = False
        #이동 변수
        self.moveRange = (int(startPos[0]-96),int(startPos[0]+96*2))
        self.movePoint = 0
        self.moveSpeed = None
        self.maxSpeed = 450
        self.accelerattion =15
        self.deceleration = 17.5
        self.minSpeed=10
        self.isGrounded = False
        self.releasedSpace = False
        #애니메이션
        self.idle = state_Idle
        self.idle.speed = 0.15
        self.hit = state_Hit
        self.hit.loop = False
        self.run = state_Run
        self.state = self.idle
        self.fin = False
        self.ChangeState(self.idle,self.Update_Idle)
        self.sfx_death = pygame.mixer.Sound('asset/scene/sfx_death.wav')
    def Update_Idle(self):
        if self.death:
            self.gravity = 500
            self.sfx_death.play()
            self.ChangeState(self.hit,self.Update_Hit)
        if random.random()<0.015:
            if self.position[0]>self.moveRange[0]*0.5 + self.moveRange[1]*0.5:
                self.movePoint = random.randint(self.moveRange[0],self.moveRange[0]*0.5 + self.moveRange[1]*0.5)
            else:
                self.movePoint = random.randint(self.moveRange[0]*0.5 + self.moveRange[1]*0.5,self.moveRange[1])
           
            self.ChangeState(self.run,self.Update_Run)
            self.state.Flip(self.position[0]>self.movePoint)
        
    def Update_Run(self):
        if self.death:
            self.gravity = 500
            self.sfx_death.play()
            self.ChangeState(self.hit,self.Update_Hit)
        if abs(self.movePoint-self.position[0])>5:
            dir = (self.movePoint-self.position[0])/abs(self.movePoint-self.position[0])
            self.position = (self.position[0]+dir*100*self.dt,self.position[1])
        else:
            self.ChangeState(self.idle,self.Update_Idle)
        
    def Update_Hit(self):
        if self.position[1]<-2500 and not self.fin:
            self.fin = True
            self.Destroy()
    def Update(self,screen,camPos,dt):
        #중력 적용
        self.dt = dt
        self.gravity-=2500*dt
        if not self.death:
            gravityResult = self.Move(screen,camPos,(0,self.gravity*dt),self.state.rect)[1]
            self.isGrounded = gravityResult!=None and gravityResult<0
            if self.isGrounded: 
                self.gravity =0
                self.jumped = False
        if self.tick!=None: self.tick()
        if not self.death:
            moveResult = self.Move(screen,camPos,(self.moveSpeed,0),self.state.rect)
            if moveResult[0] !=None: self.moveSpeed=None
        else:
            self.position = (self.position[0],self.position[1]+self.gravity*dt)
        

        #최종 범위 설정
        self.state.rect.y = camPos[1]-self.position[1]
        self.rect.y = self.state.rect.y+self.state.rect.height*0.5-self.rect.height*0.5+self.rectLocalPos[1]
        self.state.rect.x = camPos[0]-self.position[0]
        self.rect.x = self.state.rect.x+self.state.rect.width*0.5-self.rect.width*0.5+self.rectLocalPos[0]
        
        self.all_sprites.update()
        self.all_sprites.draw(screen)
    def ChangeState(self,state,tick=None):
        self.state = state
        self.state.index = 0
        self.all_sprites = pygame.sprite.Group(state)
        self.tick = tick
    def Destroy(self):
        Enemy.enemies[Enemy.enemies.index(self)] = None
        self.idle.kill()
        self.run.kill()
        self.hit.kill()
        del(self)
    