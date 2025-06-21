# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:05:11 2025

@author: hite3
"""

from PlayerClasses import Player, NPC
import time
import random
import pygame, sys
from pygame.locals import *




class Game():
    def __init__(self):
        self.Generation = 1
    
    def Mutate(Character, Image_Path):
        Character.image = pygame.image.load(Image_Path)
        if Character.Cell_Number > 8:
            Character.Organ = Character.Organ + 5
        if Character.Cell_Number > 64:
            Character.Eye = (Character.Eye*random.random())+ random.randint(0,5)
            Character.Social = (Character.Social*random.random())+ random.randint(0,5)
        Character.Cell_Number = Character.Cell_Number * 8
        Character.Energy_Level = Character.Energy_Level + 10
        Character.Life = (Character.Life*random.random())+ random.randint(0,10)
        Character.Mutated = Character.Mutated + 1
        print("A new species!")
    def __Eat__(self, Character1, Character2):
        Character1.Energy_Level = Character1.Energy_Level+ Character2.Energy_Level 
        Character1.Life = Character1.Life + Character2.Life
        Character2.Die()
    
    def Breed(Character1, Character2, NPCCount, PlayerList):
        if Character1.Cell_Number == Character2.Cell_Number:
            if Character1.Cell_Number == 1:
                Image_Path = "Amoeba.png"
            elif Character1.Cell_Number == 8:
                Image_Path = "NPCSmFish.png"
            for players in range(len(PlayerList)-1, (len(PlayerList))):
                players = NPC(Image_Path, "NPC"+str(NPCCount))
                players.Cell_Number = Character1.Cell_Number
                players.Organ = Character1.Organ
                players.Life = Character1.Life * Character2.Life/2
                return(players)
                print("A Successful Mating!")
        else:
            return(None)
            print("Different Species Can Only Be Friends")
            
        
    def __Herd__(self, Character1, Character2):
        print("Join the Pack")
        
    def Interact(self, Character1, Character2):
        dice = random.randint(0, 9)
        if Character1.Cell_Number > Character2.Cell_Number:
            self.__Eat__(Character1, Character2)
        elif Character1.Cell_Number < Character2.Cell_Number:
            self.__Eat__(Character2, Character1)
        else:
            if dice % 3 == 0:
                self.__Breed__(Character1, Character2)
            if dice % 3 == 1:
                self.__Herd__(Character1, Character2)
            if dice % 3 == 2:
                self.__Eat__(Character1, Character2)
            
        