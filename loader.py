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
    textures["board"]=pygame.transform.scale(pygame.image.load("textures/board.png"),(WIDTH,HEIGHT))
    textures["intostartmenu"]=pygame.transform.scale(pygame.image.load("textures/start.png"),(WIDTH//3,HEIGHT//6))
    textures["mainmenu"]=pygame.transform.scale(pygame.image.load("textures/menubackground.png"),(WIDTH,HEIGHT))
    textures["more"]=pygame.transform.scale(pygame.image.load("texture/more.png"),(WIDTH//20,HEIGHT//7))
    textures["less"]=pygame.transform.scale(pygame.image.load("texture/less.png"),(WIDTH//20,HEIGHT//7))
    textures["font"]= pygame.font.SysFont('B', HEIGHT//20)
    for i in range(1,5):
        textures[f"{i}"]=textures["font"].render(f"{i}")
    textures["numplay"]=textures["font"].render("Number of players")
    return textures