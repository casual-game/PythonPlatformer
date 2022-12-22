import math
import pygame
import pygame.draw
from pygame.locals import *
import random
class effect_manager():
    
    def __init__(self,screen):
        self.effects = [] #[position,degree,createdTime]
        self.time=0
        self.screen = screen
    def draw_rectangle(self,screen,x, y, width, height, rotation=0):
        points = []
        radius = math.sqrt((height / 2)**2 + (width / 2)**2)
        angle = math.atan2(height / 2, width / 2)
        angles = [angle, -angle + math.pi, angle + math.pi, -angle]
        rot_radians = (math.pi / 180) * rotation
        for angle in angles:
            y_offset = -1 * radius * math.sin(angle + rot_radians)
            x_offset = radius * math.cos(angle + rot_radians)
            points.append((x + x_offset, y + y_offset))

        pygame.draw.polygon(screen, pygame.Color(240,240,240), points)
    def AddEffect(self,pos,currentTime):
        deg = random.randrange(45,135)
        self.effects.append([pos,deg,currentTime])
        pass
    def Update(self,screen,camPos,_time):
        self.time = _time
        delCount = []
        for i in range(len(self.effects)):
            duration = 0.25
            ratio = (self.effects[i][2]+duration-self.time)/duration
            if ratio<0:
                delCount.append(i)
                continue
            else:
                pos = self.effects[i][0]
                deg = self.effects[i][1]
                self.draw_rectangle(screen,camPos[0]-pos[0],camPos[1]-pos[1],15*ratio,5000,deg)
        delCount.sort(reverse=True)
        for i in delCount:
            self.effects.remove(self.effects[i])