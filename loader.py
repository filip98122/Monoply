import pygame
import os
import random
import math
import time
import json
import sys
import copy
pygame.init()
pygame.font.init()
mouseState = pygame.mouse.get_pressed()
mousePos = pygame.mouse.get_pos()
WIDTH,HEIGHT=1920,1080
def load():
    textures={}
    textures["board"]=pygame.transform.scale(pygame.image.load("textures/board.png"),(HEIGHT,HEIGHT))
    textures["intostartmenu"]=pygame.transform.scale(pygame.image.load("textures/start.png"),(WIDTH//3,HEIGHT//6))
    textures["mainmenu"]=pygame.transform.scale(pygame.image.load("textures/menubackground.png"),(WIDTH,HEIGHT))
    textures["more"]=pygame.transform.scale(pygame.image.load("textures/more.png"),(WIDTH//25,HEIGHT//9))
    textures["less"]=pygame.transform.scale(pygame.image.load("textures/less.png"),(WIDTH//25,HEIGHT//9))
    textures["font"]= pygame.font.SysFont('B', HEIGHT//6)
    for i in range(1,5):
        textures[f"numofplayers{i}"]=textures["font"].render(f"{i}",False,(0,0,0))
    qq=[textures["font"].render(f"paran",False,(0,0,0)),textures["font"].render(f"neparan",False,(0,0,0))]
    textures["font"]= pygame.font.SysFont('B', int(HEIGHT//12.5))
    textures["numofplayers"]=textures["font"].render("Number of players",False,(0,0,0))
    textures["playerconfig"]=pygame.image.load("textures/empty.png")
    textures[f"playerconfig1"]=pygame.transform.scale(pygame.image.load("textures/boat.png"),(WIDTH//10,HEIGHT//9))
    textures[f"playerconfig2"]=pygame.transform.scale(pygame.image.load("textures/car.png"),(WIDTH// 10,HEIGHT//9))
    textures[f"playerconfig3"]=pygame.transform.scale(pygame.image.load("textures/dog.png"),(WIDTH// 10,HEIGHT//9))
    textures[f"playerconfig4"]=pygame.transform.scale(pygame.image.load("textures/hat.png"),(WIDTH// 10,HEIGHT//9))
    textures[f"playerconfig5"]=pygame.transform.scale(pygame.image.load("textures/shoe.png"),(WIDTH//10,HEIGHT//9))
    return textures