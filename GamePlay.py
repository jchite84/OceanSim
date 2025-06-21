# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 22:04:18 2025

@author: hite3

Bug fix - slow down breeding and increase eating
Add error handling for empty range

"""

#Imports
import pygame, sys
from pygame.locals import *
import random, time
from PlayerClasses import Player, NPC
from GameClass import Game

#Initialize All Classes
pygame.init()
Player = Player("Amoeba1.png")
GameFunctions = Game()
NPCCount = 0

#Create NPC List
PlayerList = []

for i in range(20):
    PlayerList.append("NPC"+str(NPCCount))
    NPCCount = NPCCount + 1
    
all_sprites = pygame.sprite.Group()
all_sprites.add(Player)

npc = pygame.sprite.Group()


for players in PlayerList:
    players = NPC("Amoeba.png", players)
    all_sprites.add(players)
    npc.add(players)

 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SPEED = 5
YEAR = 0

DISPLAYSURF = pygame.display.set_mode((1000,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
background = pygame.image.load("Ocean.png")

font_small = pygame.font.SysFont("Verdana", 20)



Age = pygame.USEREVENT + 1
pygame.time.set_timer(Age, 60000)

Breed = pygame.USEREVENT + 1
pygame.time.set_timer(Breed, random.randint(5000, 20000))

Eat = pygame.USEREVENT + 1
pygame.time.set_timer(Eat, 10000)



#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.blit(background, (0,0))
    years = font_small.render(str(YEAR), True, BLACK)
    DISPLAYSURF.blit(years, (10,10))
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.Move()
        if entity.Energy_Level > 2500 and entity.Mutated == 0  and entity.Name == 'Steve':
            Game.Mutate(entity, 'SmFish.png')
        elif entity.Energy_Level > 2500 and entity.Mutated == 0 and entity.Name != 'Steve' and random.randint(0,4)==4:
            Game.Mutate(entity, 'NPCSmFish.png')

            
        
    collided_sprites = pygame.sprite.spritecollide(Player, npc, False)
    if collided_sprites: # Check if the list is not empty
        dice = random.randint(0, 1)
        print(str(dice))
        if dice == 1:
            
            #Breed
            """
            NPCCount = NPCCount +1
            PlayerList.append("NPC"+str(NPCCount))
            for players in range(len(PlayerList)-1, (len(PlayerList))):
                players = NPC("Amoeba.png", "NPC"+str(NPCCount))
                all_sprites.add(players)
                npc.add(players)
                """
            for sprite in collided_sprites:
                NPCCount = NPCCount +1
                PlayerList.append("NPC"+str(NPCCount))
                if Player.Cell_Number == sprite.Cell_Number:
                    if Player.Cell_Number == 1:
                        Image_Path = "Amoeba.png"
                        NewLife = random.randint(5, 20)
                    elif Player.Cell_Number == 8:
                        Image_Path = "NPCSmFish.png"
                        NewLife = random.randint(20, 50)
                    for players in range(len(PlayerList)-1, (len(PlayerList))):
                        players = NPC(Image_Path, "NPC"+str(NPCCount))
                        players.Cell_Number = Player.Cell_Number
                        players.Organ = Player.Organ
                        players.Life = NewLife
                        all_sprites.add(players)
                        npc.add(players)
                        print("A Successful Mating!")
                else:

                    print("Different Species Can Only Be Friends")
        else:
            #Eat
            for sprite in collided_sprites:
                Player.Energy_Level = Player.Energy_Level+ sprite.Energy_Level
                sprite.Life = 0
                try:
                    PlayerList.remove(entity.Name)
                    print(entity.Name + " has been eaten!")
                except ValueError:
                    continue
              

    for entity in npc:
        if event.type == Age:
            entity.Age()
            YEAR = YEAR + 1
           
        if event.type == Eat:
            if len (PlayerList) > 75:
                try:
                    predator = random.randint(0, len(npc.sprites())-2)
                    prey = random.randint(0, len(npc.sprites())-1)
                    if predator == prey and predator != 0:
                        predator = predator - 1
                    else:
                        predator = predator + 1
                    if  npc.sprites()[predator].Cell_Number ==  npc.sprites()[prey].Cell_Number:
                        npc.sprites()[predator].Energy_Level = npc.sprites()[predator].Energy_Level + npc.sprites()[prey].Energy_Level
                        npc.sprites()[prey].Life = 0
                    try:
                        PlayerList.remove(npc.sprites()[prey].Name)
                    except ValueError:
                        continue
                except ValueError:
                    continue
        
        if event.type == Breed:
            dice = random.randint(0, 1)
            if len(PlayerList) < 500:
                try:
                    NPC1 = random.randint(0, len(npc.sprites())-2)
                    NPC2 = random.randint(0, len(npc.sprites())-1)
                    if NPC1 == NPC2 and NPC2 != 0:
                        NPC1 = NPC1 - 1
                    else:
                        NPC1 = NPC1 + 1
                except ValueError:
                    continue
                if npc.sprites()[NPC1].Cell_Number == npc.sprites()[NPC2].Cell_Number and dice == 1:
                    NPC1 = npc.sprites()[NPC1]
                    NPC2 = npc.sprites()[NPC2]
                    NPCCount = NPCCount +1
                    PlayerList.append("NPC"+str(NPCCount))
                    if Player.Cell_Number == 1:
                        Image_Path = "Amoeba.png"
                        NewLife = random.randint(5, 20)
                    elif Player.Cell_Number == 8:
                        Image_Path = "NPCSmFish.png"
                        NewLife = random.randint(20, 50)
                    for players in range(len(PlayerList)-1, (len(PlayerList))):
                        players = NPC(Image_Path, "NPC"+str(NPCCount))
                        players.Cell_Number = NPC1.Cell_Number
                        players.Organ = NPC1.Organ
                        players.Life = NewLife
                        all_sprites.add(players)
                        npc.add(players)
                        print("A Successful Mating!")
                else: 
                    print("Maybe Next Time")
                 
            else:
                print("Population Density too high" + str(len(PlayerList)))   
          
            
    for entity in npc:
        if entity.Life <= 0:
            entity.kill()
            try:
                PlayerList.remove(entity.Name)
            except ValueError:
                continue
            
            
            
    pygame.display.update()
    FramePerSec.tick(FPS)
