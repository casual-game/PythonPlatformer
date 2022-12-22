import pygame
from pygame.locals import *
from module_2d import *
from rigidbody import *
from enemy import*
from effect_manager import *
class Player(Rigidbody):
    def __init__(self,screen,camera,effect_manager,startPos,platform,thin,rectSize,rectLocalPos):
        super().__init__(startPos,platform,thin,rectSize,rectLocalPos)
        self.tick = None
        self.dt = 0.03
        self.effect_manager = effect_manager
        self.screen = screen
        self.camera = camera
        self.time = 0.0
        #중력 변수
        self.jumpSpeed = 700
        self.attackSpeed = 500
        self.gravity = 0
        self.jumped = False
        #이동 변수
        self.moveSpeed = None
        self.maxSpeed = 450
        self.accelerattion =15
        self.deceleration = 17.5
        self.minSpeed=10
        self.isGrounded = False
        self.releasedSpace = False
        self.death = False
        self.fin = False
        self.sfx_run = pygame.mixer.Sound('asset/scene/sfx_run.wav')
        self.sfx_run.set_volume(0.5)
        self.sfx_jump = pygame.mixer.Sound('asset/scene/sfx_jump.wav')
        self.sfx_swing = pygame.mixer.Sound('asset/scene/sfx_swing.wav')
        self.sfx_death =  pygame.mixer.Sound('asset/scene/sfx_playerdeath.wav')
        #애니메이션
        self.idle = Sprite_State(self.position,192,120,
        'asset/player/idle/Idle Sword 01.png',
        'asset/player/idle/Idle Sword 02.png',
        'asset/player/idle/Idle Sword 03.png',
        'asset/player/idle/Idle Sword 04.png',
        'asset/player/idle/Idle Sword 05.png')
        self.idle.speed = 0.15
        self.hit = Sprite_State(self.position,192,120,
        'asset/player/hit/1.png',
        'asset/player/hit/2.png',
        'asset/player/hit/3.png',
        'asset/player/hit/4.png')
        self.move = Sprite_State(self.position,192,120,
        'asset/player/move/Run Sword 01.png',
        'asset/player/move/Run Sword 02.png',
        'asset/player/move/Run Sword 03.png',
        'asset/player/move/Run Sword 04.png',
        'asset/player/move/Run Sword 05.png',
        'asset/player/move/Run Sword 06.png')
        self.move.callbacks.append([2,self.PlayMove])
        self.move.callbacks.append([5,self.PlayMove])
        self.jump = Sprite_State(self.position,192,120,
        'asset/player/jump/1.png',
        'asset/player/jump/2.png',
        'asset/player/jump/3.png',
        'asset/player/jump/4.png')
        self.jump.speed = 0.2
        self.jump.loop = False
        self.attack_1 = Sprite_State(self.position,192,120,
        'asset/player/attack_1/1.png',
        'asset/player/attack_1/2.png',
        'asset/player/attack_1/3.png')
        self.attack_1.loop = False
        self.attack_2 = Sprite_State(self.position,192,120,
        'asset/player/attack_2/1.png',
        'asset/player/attack_2/2.png',
        'asset/player/attack_2/3.png')
        self.attack_2.loop = False
        self.state = self.idle
        self.ChangeState(self.idle,self.Update_Ilde)
    def ChangeState(self,state,tick=None):
        self.state = state
        self.state.index = 0
        self.all_sprites = pygame.sprite.Group(state)
        self.tick = tick
    def PlayMove(self):
        self.sfx_run.play()
    def _update_checkdeath(self):
        for enemy in Enemy.enemies:
                if enemy!=None and not enemy.death  and enemy.state.rect.colliderect(self.rect):
                    self.death = True
        if self.position[1]<-2500:
            self.death = True
        if self.death:
            self.gravity = 500
            self.sfx_death.play()
            self.ChangeState(self.hit,self.Update_Hit)
    def Update_Ilde(self):
        self._update_checkdeath()
        pressed = pygame.key.get_pressed()
        if not pressed[K_SPACE]: self.releasedSpace = True
        if self.moveSpeed!=None: 
            if self.moveSpeed!=None: self.moveSpeed*=Clamp(0,1,1-self.deceleration*self.dt)
            if abs(self.moveSpeed) < self.minSpeed*self.dt: self.moveSpeed = None
        if pressed[K_SPACE] and self.releasedSpace:
            self.gravity = self.jumpSpeed
            self.jumped = True
            self.releasedSpace = False
            self.sfx_jump.play()
            self.ChangeState(self.jump,self.Update_Jump)
        if pressed[K_a]:
            self.state.Flip(True)
            self.ChangeState(self.move,self.Update_Move)
        if pressed[K_d]:
            self.state.Flip(False)
            self.ChangeState(self.move,self.Update_Move)
    def Update_Move(self):
        self._update_checkdeath()
        pressed = pygame.key.get_pressed()
        if not pressed[K_SPACE]: self.releasedSpace = True
        if pressed[K_SPACE] and self.releasedSpace:
            self.gravity = self.jumpSpeed
            self.jumped = True
            self.releasedSpace = False
            self.sfx_jump.play()
            self.ChangeState(self.jump,self.Update_Jump)
        if pressed[K_a]:
            self.state.Flip(True)
            if self.moveSpeed==None: self.moveSpeed =0
            elif self.moveSpeed<0:
                if self.moveSpeed!=None: self.moveSpeed*=Clamp(0,1,1-self.deceleration*self.dt)
                if abs(self.moveSpeed) < self.minSpeed*self.dt: self.moveSpeed = None
            else:
                self.moveSpeed = Clamp(-self.maxSpeed*self.dt,self.maxSpeed*self.dt,self.moveSpeed+self.accelerattion*self.dt)
        if pressed[K_d]:
            if self.moveSpeed==None: self.moveSpeed =0
            elif self.moveSpeed>0:
                if self.moveSpeed!=None: self.moveSpeed*=Clamp(0,1,1-self.deceleration*self.dt)
                if abs(self.moveSpeed) < self.minSpeed*self.dt: self.moveSpeed = None
            else:
                self.moveSpeed = Clamp(-self.maxSpeed*self.dt,self.maxSpeed*self.dt,self.moveSpeed-self.accelerattion*self.dt)
            self.state.Flip(False)
        if not pressed[K_d] and not pressed[K_a]:
            if self.moveSpeed!=None: 
                self.moveSpeed*=Clamp(0,1,1-self.deceleration*self.dt)
                if abs(self.moveSpeed) < self.minSpeed*self.dt: self.moveSpeed = None
            if self.isGrounded and self.state != self.idle: self.ChangeState(self.idle,self.Update_Ilde)
    def _update_jump(self,pressed):
        if not pressed[K_SPACE]: self.releasedSpace = True
        if pressed[K_a]:
            self.state.Flip(True)
            if self.moveSpeed==None: self.moveSpeed =0
            elif self.moveSpeed<0:
                self.moveSpeed*=Clamp(0,1,1-self.deceleration*self.dt)
                if abs(self.moveSpeed) < self.minSpeed*self.dt: self.moveSpeed = None
            else:
                self.moveSpeed = Clamp(-self.maxSpeed*self.dt,self.maxSpeed*self.dt,self.moveSpeed+self.accelerattion*self.dt)
        if pressed[K_d]:
            self.state.Flip(False)
            if self.moveSpeed==None: self.moveSpeed =0
            elif self.moveSpeed>0:
                if self.moveSpeed!=None: self.moveSpeed*=Clamp(0,1,1-self.deceleration*self.dt)
                if abs(self.moveSpeed) < self.minSpeed*self.dt: self.moveSpeed = None
            else:
                self.moveSpeed = Clamp(-self.maxSpeed*self.dt,self.maxSpeed*self.dt,self.moveSpeed-self.accelerattion*self.dt)
                
        if not pressed[K_d] and not pressed[K_a]:
            if self.moveSpeed!=None: 
                if self.moveSpeed!=None: self.moveSpeed*=Clamp(0,1,1-self.deceleration*self.dt)
                if abs(self.moveSpeed) < self.minSpeed*self.dt: self.moveSpeed = None
            if self.isGrounded and self.state != self.idle: self.ChangeState(self.idle,self.Update_Ilde)
        elif self.isGrounded and self.state != self.move: self.ChangeState(self.move,self.Update_Move)
    def Update_Jump(self):
        pressed = pygame.key.get_pressed()
        self._update_jump(pressed)
        if pressed[K_SPACE] and not self.isGrounded and self.releasedSpace:
            self.gravity = self.attackSpeed
            if self.moveSpeed!=None: self.moveSpeed*=0.25
            self.releasedSpace = False
            self.sfx_swing.play()
            self.ChangeState(self.attack_2,self.Update_Attack2)
            for enemy in Enemy.enemies:
                if enemy!=None and not enemy.death  and  enemy.state.rect.colliderect(self.rect):
                    enemy.death = True
                    self.effect_manager.AddEffect(enemy.position,self.time)
                    self.camera.Shake()
    def Update_Attack1(self):
        pressed = pygame.key.get_pressed()
        self._update_jump(pressed)
        if False and pressed[K_SPACE] and not self.isGrounded and self.releasedSpace and self.attack_1.index>len(self.attack_1.images)-1.1:
            self.gravity = self.attackSpeed
            if self.moveSpeed!=None: self.moveSpeed*=0.25
            self.releasedSpace = False
            self.ChangeState(self.attack_2,self.Update_Attack2)
    def Update_Attack2(self):
        pressed = pygame.key.get_pressed()
        self._update_jump(pressed)
        if pressed[K_SPACE] and not self.isGrounded and self.releasedSpace and self.attack_2.index>len(self.attack_2.images)-1.1:
            self.gravity = self.attackSpeed
            if self.moveSpeed!=None: self.moveSpeed*=0.25
            self.releasedSpace = False
            self.sfx_swing.play()
            
            self.ChangeState(self.attack_1,self.Update_Attack1)
            for enemy in Enemy.enemies:
                if  enemy!=None and not enemy.death and enemy.state.rect.colliderect(self.rect):
                    enemy.death = True
                    self.effect_manager.AddEffect(enemy.position,self.time)
                    self.camera.Shake()
    def Update(self,screen,camPos,time,dt):
        self.time = time
        #중력 적용
        self.dt = dt
        self.gravity-=2000*dt
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
        if self.position[1]<-2500 and not self.death:
            self.death = True
            self.sfx_death.play()
            self.ChangeState(self.hit,self.Update_Hit)
        #최종 범위 설정
        self.state.rect.y = camPos[1]-self.position[1]
        self.rect.y = self.state.rect.y+self.state.rect.height*0.5-self.rect.height*0.5+self.rectLocalPos[1]
        self.state.rect.x = camPos[0]-self.position[0]
        self.rect.x = self.state.rect.x+self.state.rect.width*0.5-self.rect.width*0.5+self.rectLocalPos[0]
        
        self.all_sprites.update()
        self.all_sprites.draw(screen)
    def Destroy(self):
        self.idle.kill()
        self.hit.kill()
        self.move.kill()
        self.attack_1.kill()
        self.attack_2.kill()
        self.jump.kill()
        del(self)
    def Update_Hit(self):
        if self.position[1]<-2500 and not self.fin:
            self.fin = True
        
        
