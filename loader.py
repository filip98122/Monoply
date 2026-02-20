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
    textures["board"]=pygame.transform.scale(pygame.image.load("textures/brick.png"),(WIDTH,HEIGHT))
    textures["font"]= pygame.font.SysFont('B', HEIGHT//5)
    return textures