import math 
from pygame import gfxdraw
import pygame

class obstacle:
    def __init__(self, px:int, py:int, larg:int, haut:int):
        self.px=px
        self.py=py
        self.larg=larg
        self.haut=haut
