import sys
import math
import pygame
import pygame.draw
from pygame.locals import *
#-------------------------------------
from player import *
from scene import *
from camera import *
from module_2d import *
from effect_manager import *
class Game(object):
    def __init__(self, width=1280, height=720):
        self.title = "Roger's escape"
        self.fps = 60
        self.width = width
        self.height = height
        self.circle_pos = width/2, height/2
        self.camPos = (0,0)
        self.platform = []
        self.platform_thin = []
        self.alpha = 0
        self.loadState = 2
       
        self.scene = None
        self.player =None
        self.camera =None
        self.restart = False
        self.scenes = ['asset/scene/map_0','asset/scene/map_1','asset/scene/map_2']
        self.sceneIndex= 0
        self.lastsceneIndex = 2
        self.time=0
        self.bgm = False
        
    
        
    def CreateMap(self,screen,playerPos,width,height):
        self.sfx_spawn.play()
        #맵 생성
        self.sceneIndex = self.sceneIndex%len(self.scenes)
        self.scene = Scene(playerPos,width,height,self.scenes[self.sceneIndex]) 
        self.platform = self.scene.platform
        self.platform_thin = self.scene.platform_thin
        self.player = Player(screen,self.camera,self.effect_manager,playerPos,self.platform,self.platform_thin,(64,96),(0,-10))
    def UpdateMap(self,screen,dt):
        if self.scene!=None: self.scene.Update(screen,self.camPos)
        if self.player!=None: self.player.Update(screen,self.camPos,self.time,dt)
        for enemy in Enemy.enemies:
            if  enemy!=None: enemy.Update(screen,self.camPos,dt)
        self.camPos = (-400,-1200)
        if self.camera!=None and self.player!=None: self.camPos = self.camera.Update(self.player.position,self.time,dt)

        if self.loadState ==0:
            self.alpha  = Clamp(0,255,self.alpha+200*dt)
            if self.alpha>250: self.loadState =1
        elif self.loadState == 1:
            
            
            #기존 맵 삭제
            self.bgm = False
            if self.scene!=None: self.scene.Destroy()
            if self.player!=None: self.player.Destroy()
            for enemy in Enemy.enemies:
                if  enemy!=None: enemy.Destroy()
            Enemy.enemies.clear()
            
            self.alpha = 255
            self.sceneIndex+=1
            self.CreateMap(screen,(-200,-1720),2880,1920)
            self.camera.MoveTo((-200,-1720))
            self.loadState =2
        else:
            if not self.bgm:
                if self.lastsceneIndex!= self.sceneIndex:
                    self.bgm = True
                    if self.sceneIndex==0: 
                        pygame.mixer.music.load('asset/scene/music_0.wav')
                        pygame.mixer.music.set_volume(0.5)
                    elif self.sceneIndex==1: 
                        pygame.mixer.music.load('asset/scene/music_1.wav')
                        pygame.mixer.music.set_volume(0.35)
                    else : 
                        pygame.mixer.music.load('asset/scene/music_2.wav')
                        pygame.mixer.music.set_volume(0.35)
                    
                    pygame.mixer.music.play(-1)
                self.lastsceneIndex = self.sceneIndex
            if self.player!=None and self.scene!=None and self.camera!= None:
                self.alpha = Clamp(0,255,self.alpha-200*dt)
                if self.player.death or self.player.fin:
                    self.sceneIndex-=1
                    self.sfx_gameover.play()
                    self.loadState=0
                count=0
                for enemy in Enemy.enemies:
                    if  enemy!=None: count+=1
                if count==0:
                    self.sfx_gameclear.play()
                    self.loadState=0
        s = pygame.Surface((1280,720))
        s.set_alpha(self.alpha)               
        s.fill((0,0,0))           
        screen.blit(s, (0,0))
    def start(self):
        pygame.init()
        size = (self.width, self.height)
        screen = pygame.display.set_mode(size, DOUBLEBUF)
        self.camera = Camera((-200,-1720),5,2880,1920)
        self.effect_manager = effect_manager(screen)
        pygame.display.set_caption(self.title)
        clock = pygame.time.Clock()
        self.sfx_gameover = pygame.mixer.Sound('asset/scene/sfx_gameover.wav')
        self.sfx_gameclear = pygame.mixer.Sound('asset/scene/sfx_gameclear.wav')
        self.sfx_spawn = pygame.mixer.Sound('asset/scene/sfx_spawn.wav')
        self.CreateMap(screen,(-200,-1720),2880,1920)
        while True:
            
            dt = clock.tick(self.fps)
            self.time +=dt*0.001
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((51, 50, 61))
            self.UpdateMap(screen,dt*0.001)
            self.effect_manager.Update(screen,self.camPos,self.time)
            pygame.display.update()
            pygame.display.flip()
    
if __name__ == '__main__':
    app = Game()
    app.start()

