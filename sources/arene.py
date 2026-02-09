from robot import *
from obstacle import *


class Arene:
    def __init__(self, larg:int, haut:int, robot:Robot):
        self.larg = larg
        self.haut = haut
        self.robot = robot
        #self.obstacle=obstacles
        self.img_car = 0
        self.rob_larg = 0
        self.rob_haut = 0