import pygame
from pygame.locals import *
from module_2d import *
import csv
from enemy import*
from blue_bird import*
from pink_star import*
from fierce_tooth import*
from whale import*
class Scene():
    def __init__(self,playerPos, width, height,sprite):
        self._sprite = sprite
        self.image_Platform = Sprite_Single((0,0), width, height,self._sprite+'_Platform.jpg')
        self.position = (0,0)
        self.sprite_Platform = pygame.sprite.Group(self.image_Platform)
        self.playerPos = playerPos
        self.width = width
        self.height = height
        self.padding = 256
        self.deco = {}
        self.platform = []
        self.platform_thin = []
        for i in range(30):
            self.platform.append([])
            self.platform_thin.append([])
            for j in range(20):
                self.platform[i].append(None)
                self.platform_thin[i].append(None)
        self.Init_Deco()
        self.Init_Platform_Thin()
        self.Init_Platform()
        self.Init_Enemy()
    def Init_Deco(self):
        f = open(self._sprite+'_Deco.csv', 'r')
        rdr = csv.reader(f)
        i=-1
        j=-1
        for line in rdr:
            j=-1
            i+=1
            for data in line:
                j+=1
                if data!='-1':
                    if data == '7':
                        self.CreateSprite(i,j,0,96,96,192,0.15,
                        'asset/deco/Chain_Big_01.png',
                        'asset/deco/Chain_Big_02.png',
                        'asset/deco/Chain_Big_03.png',
                        'asset/deco/Chain_Big_04.png',
                        'asset/deco/Chain_Big_05.png',
                        'asset/deco/Chain_Big_06.png',
                        'asset/deco/Chain_Big_07.png',
                        'asset/deco/Chain_Big_08.png')
                    elif data == '8': 
                        self.CreateSprite(i,j,0,0,96,96,0.15,
                        'asset/deco/Chain_Small_01.png',
                        'asset/deco/Chain_Small_02.png',
                        'asset/deco/Chain_Small_03.png',
                        'asset/deco/Chain_Small_04.png',
                        'asset/deco/Chain_Small_05.png',
                        'asset/deco/Chain_Small_06.png',
                        'asset/deco/Chain_Small_07.png',
                        'asset/deco/Chain_Small_08.png')
                    elif data == '10':
                        self.CreateSprite(i,j,0,0,96,96,0.3,
                        'asset/deco/window/01.png',
                        'asset/deco/window/02.png',
                        'asset/deco/window/03.png',
                        'asset/deco/window/04.png',
                        'asset/deco/window/05.png',
                        'asset/deco/window/06.png',
                        'asset/deco/window/07.png',
                        'asset/deco/window/08.png',
                        'asset/deco/window/09.png',
                        'asset/deco/window/10.png',
                        'asset/deco/window/11.png',
                        'asset/deco/window/12.png',
                        'asset/deco/window/13.png',
                        'asset/deco/window/14.png',
                        'asset/deco/window/15.png',
                        'asset/deco/window/16.png',
                        'asset/deco/window/17.png',
                        'asset/deco/window/18.png',
                        'asset/deco/window/19.png',
                        'asset/deco/window/20.png',
                        'asset/deco/window/21.png',
                        'asset/deco/window/22.png',
                        'asset/deco/window/23.png',
                        'asset/deco/window/24.png',
                        'asset/deco/window/25.png',
                        'asset/deco/window/26.png',
                        'asset/deco/window/27.png',
                        'asset/deco/window/28.png',
                        'asset/deco/window/29.png',
                        'asset/deco/window/30.png',
                        'asset/deco/window/31.png',
                        'asset/deco/window/32.png',
                        'asset/deco/window/33.png',
                        'asset/deco/window/34.png',
                        'asset/deco/window/35.png',
                        'asset/deco/window/36.png',
                        'asset/deco/window/37.png',
                        'asset/deco/window/38.png',
                        'asset/deco/window/39.png',
                        'asset/deco/window/40.png',
                        'asset/deco/window/41.png',
                        'asset/deco/window/42.png',
                        'asset/deco/window/43.png',
                        'asset/deco/window/44.png',
                        'asset/deco/window/45.png',
                        'asset/deco/window/46.png',
                        'asset/deco/window/47.png',
                        'asset/deco/window/48.png',
                        'asset/deco/window/49.png',
                        'asset/deco/window/50.png',
                        'asset/deco/window/51.png',
                        'asset/deco/window/52.png',
                        'asset/deco/window/53.png',
                        'asset/deco/window/54.png',
                        'asset/deco/window/55.png',
                        'asset/deco/window/56.png',
                        'asset/deco/window/57.png',
                        'asset/deco/window/58.png',
                        'asset/deco/window/59.png',
                        'asset/deco/window/60.png',
                        'asset/deco/window/61.png',
                        'asset/deco/window/62.png',
                        'asset/deco/window/63.png',
                        'asset/deco/window/64.png',
                        'asset/deco/window/65.png',
                        'asset/deco/window/66.png',
                        'asset/deco/window/67.png',
                        'asset/deco/window/68.png',
                        'asset/deco/window/69.png',
                        'asset/deco/window/70.png',
                        'asset/deco/window/71.png',
                        'asset/deco/window/72.png',
                        'asset/deco/window/73.png',
                        'asset/deco/window/74.png')
                    elif data == '11':
                        self.CreateSprite(i,j,-10,202,288,288,0.15,
                        'asset/deco/window/window_light.png')
                    elif data == '12': 
                        self.CreateSprite(i,j,-0,0,96,96,0.15,
                        'asset/deco/candle/01.png',
                        'asset/deco/candle/02.png',
                        'asset/deco/candle/03.png',
                        'asset/deco/candle/04.png',
                        'asset/deco/candle/05.png',
                        'asset/deco/candle/06.png')
                    elif data == '13':
                        self.CreateSprite(i,j,0,0,96,96,0.15,
                        'asset/deco/Barrels_2.png')
                    elif data == '14':
                        self.CreateSprite(i,j,0,0,96,96,0.15,
                        'asset/deco/Bottle_1.png')
                    elif data == '15':
                        self.CreateSprite(i,j,0,0,96,96,0.15,
                        'asset/deco/Bottle_2.png')
                    elif data == '16': 
                        self.CreateSprite(i,j,0,0,96,96,0.15,
                        'asset/deco/Bottle_3.png')
                    elif data == '17': 
                        self.CreateSprite(i,j,0,0,96,96,0.15,
                        'asset/deco/Bottle_4.png')
                    elif data == '18':
                        self.CreateSprite(i,j,0,0,96,96,0.15,
                        'asset/deco/Barrels_1.png')
        f.close()  
    def Init_Platform_Thin(self):
        f = open(self._sprite+'_Platform_Thin.csv', 'r')
        rdr = csv.reader(f)
        i=-1
        j=-1
        for line in rdr:
            j=-1
            i+=1
            for data in line:
                j+=1
                if data!='-1':
                    self.CreatePlatform_Thin(i,j,True)
                    if data == '7':
                        self.CreateSprite(i,j,0,0,96,96,0,'asset/deco/thin/7.png')
                    elif data == '9':
                        self.CreateSprite(i,j,0,0,96,96,0,'asset/deco/thin/9.png')
                    elif data == '13':
                        self.CreateSprite(i,j,0,0,96,96,0,'asset/deco/thin/13.png')
                    elif data == '14':
                        self.CreateSprite(i,j,0,0,96,96,0,'asset/deco/thin/14.png')
                    elif data == '15':
                        self.CreateSprite(i,j,0,0,96,96,0,'asset/deco/thin/15.png')
        f.close()
    def Init_Platform(self):
        f = open(self._sprite+'_Platform.csv', 'r')
        rdr = csv.reader(f)
        i=-1
        j=-1
        for line in rdr:
            j=-1
            i+=1
            for data in line:
                j+=1
                if data!='-1' and data!= '40':
                    self.CreatePlatform(i,j,False)
        f.close()
    def Init_Enemy(self):
        f = open(self._sprite+'_Enemy.csv', 'r')
        rdr = csv.reader(f)
        i=-1
        j=-1
        for line in rdr:
            j=-1
            i+=1
            for data in line:
                j+=1
                if data!='-1':
                    if data == '1': 
                        Fierce_Tooth((j*-96,i*-96),self.platform,self.platform_thin,(102,90),(0,-10))
                    elif data == '2': 
                        Pink_Star((j*-96,i*-96),self.platform,self.platform_thin,(102,90),(0,-10))
        f.close()  
    def Update(self,screen,camPos):
        self.image_Platform.rect.x = camPos[0]-self.position[0]
        self.image_Platform.rect.y = camPos[1]-self.position[1]
        self.sprite_Platform.draw(screen)
        for _deco in self.deco.values():
            _deco[0].rect.x = camPos[0]-_deco[0].position[0]
            _deco[0].rect.y = camPos[1]-_deco[0].position[1]
            _deco[1].update()
            _deco[1].draw(screen)
        

    def CreateSprite(self,i,j,addX,addY,width,height,speed,*paths):
        if(len(paths)>0):
            state = Sprite_State((j*-96+addX,i*-96+addY),width,height,*paths)
            state.speed = speed
            self.deco[(i,j)] = [state,pygame.sprite.Group(state)]
        else: 
            state = Sprite_Single((j*-96+addX,i*-96+addY),width,height,paths[0])
            self.deco[(i,j)] =  [state,pygame.sprite.Group(state)]
    def CreatePlatform(self,i,j,canPass=False):
        self.platform[j][i]= [Rect(j*-96,i*-96,96,96),j*-96,i*-96]
    def CreatePlatform_Thin(self,i,j,canPass=False):
        self.platform_thin[j][i]= [Rect(j*-96,i*-96,96,96),j*-96,i*-96]
    def Destroy(self):
        self.platform.clear()
        self.platform_thin.clear()
        for deco in self.deco.values():
            deco[0].kill()
        self.deco.clear()
        del(self)

        