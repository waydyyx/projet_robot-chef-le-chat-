from modele.robot import Robot
from multiprocessing import RLock
import random
import math

class Obstacle:
    def __init__(self, px:int, py:int, larg:int, haut:int):
        self.px=px
        self.py=py
        self.larg=larg
        self.haut=haut

class Arene:
    def __init__(self, larg : int, haut : int, robot1 : Robot, robot2:Robot):
        self.larg = larg
        self.haut = haut
        self.robot = [robot1,robot2]
        # self.obstacles = []
        self.obstacles=[]#[Obstacle(int(self.larg/2)-50,int(self.haut/2)-50,100,100),Obstacle(int(self.larg/2-50),0,100,100),Obstacle(int(self.larg/2)-50,self.haut-100,100,100)] #Q1.1
        self.stop = 0
        self.stop_lock = RLock()
    
    def collision_bord(self,robot):
        #avancer
        if (robot.px < 0 or robot.px > self.larg - robot.size or robot.py < 0 or robot.py > self.haut - robot.size):
            return (1)
        return (0)
    

    def collision_obstacle(self,robot):
        """test la collision sur x
        test la collision sur y 
        si les deux soon vraie return true sinon false 
        robot ,obstacle -> bool""" 
        for obstacle in self.obstacles:
            if(robot.px + robot.size > obstacle.px and robot.px < obstacle.px + obstacle.larg and robot.py + robot.size > obstacle.py and robot.py < obstacle.py + obstacle.haut) :
                return True
        return False 
    
    
    def detection_obstacle(self,robot):
        """
        Detecte un obstacle 
        """
        centre = robot.size / 2
        i = 0
        angle =- robot.angle
        while not(self.collision_point(int(robot.px + math.cos(-angle) * i + centre), int(robot.py + math.sin(-angle) * i + centre))):
            i += 1
        # print(f"{round(((i-25)*17/50) / 100, 2)}m")
        return i 
    
    def collision_point(self,x,y):
        if not ((x>0 and x<self.larg)and(y>0 and y<self.haut)):
            return True
        for obstacle in self.obstacles:
            if (x < obstacle.px + obstacle.larg) and (y < obstacle.py + obstacle.haut) and ( x > obstacle.px) and ( y > obstacle.py):
                return True
        return False
        
