from obstacle import *


class Arene:
    def __init__(self, larg : int, haut : int, robot : "Robot"):
        self.larg = larg
        self.haut = haut
        self.robot = robot
        #self.obstacle=obstacles