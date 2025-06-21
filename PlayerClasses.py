# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 10:39:14 2025

@author: hite3

pygame.sprite.Sprite, Image_Path
"""
import pygame, sys
from pygame.locals import *
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, Image_Path):
        super().__init__()
        self.image = pygame.image.load(Image_Path)
        self.rect = self.image.get_rect()
        self.rect.center = (10, 250)
        self.Cell_Number = 1
        self.Energy_Level = 10
        self.Life = 20
        self.Eye = 0
        self.Organ = 0
        self.Social = 0
        self.Name = "Steve"
        self.Mutated = 0
    def Move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 5:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < 595:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.left > 5:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 995:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def Age(self):
        self.Life = self.Life - 1
        self.Energy_Level = self.Energy_Level - 5

    
    def Die(self):
        self.Life = 0
        
        
class NPC(pygame.sprite.Sprite):
    def __init__(self, Image_Path, Name):
        super().__init__()
        self.image = pygame.image.load(Image_Path)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 1000), random.randint(0,600))
        self.Cell_Number = 1
        self.Energy_Level = 10
        self.Life = random.randint(20, 50)
        self.Eye = 0
        self.Organ = 0
        self.Social = 0
        self.XCoord = random.randint(-1, 1)
        self.YCoord = random.randint(-1, 1)
        self.Name = Name
        self.Mutated = 0
   
    def DirChange(self):
        self.XCoord =  random.randint(-3, 3)
        self.YCoord =  random.randint(-3, 3)

            

    def Move(self):
        if self.XCoord == 0 and self.YCoord == 0:
            self.DirChange()
        if self.rect.left < 5: 
            self.rect.move_ip(5, 0)
            self.DirChange()
        if self.rect.right > 995:
            self.rect.move_ip(-5, 0)
            self.DirChange()
        if self.rect.top < 5:
            self.rect.move_ip(0, 5)
            self.DirChange()
        if self.rect.bottom > 595:
            self.rect.move_ip(0, -5)
            self.DirChange()
        else:
            self.rect.move_ip(self.XCoord, self.YCoord)
            
        """    
        if dice == 0 and self.rect.left > 0:
            self.rect.move_ip(random.randint(-3, 3), random.randint(-3, 3))
        elif dice == 1 and self.rect.right < 1000:
            self.rect.move_ip(random.randint(-3, 3), random.randint(-3, 3))
        elif dice == 2 and self.rect.bottom < 600:
            self.rect.move_ip(random.randint(-3, 3), random.randint(-3, 3))
        elif dice == 3 and self.rect.top > 0:
            self.rect.move_ip(random.randint(-3, 3), random.randint(-3, 3))
         """   
    def Age(self):
        self.Life = self.Life - 1
        self.Energy_Level = self.Energy_Level - 5
    def Die(self):
        self.Life = 0
        

        
            
        
        
    
    
