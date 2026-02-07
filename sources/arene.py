import math 
from pygame import gfxdraw
import pygame
from class_robot import *
from obstacle import *


class Arene:
    def __init__(self, larg:int, haut:int, robot:Robot, obstacles:list[Obstacle]):
        self.larg=larg
        self.haut=haut
        self.robot=robot
        self.obstacle=obstacles