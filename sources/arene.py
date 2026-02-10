from obstacle import *
import random


class Arene:
    def __init__(self, larg : int, haut : int, robot : "Robot"):
        self.larg = larg
        self.haut = haut
        self.robot = robot
        self.obstacles=[Obstacle(random.randint(0,larg),random.randint(0,haut),50,50)for x in range (10)]

    def collision_obstacle_avancer(self):
        """test la collision sur x
        test la collision sur y 
        si les deux soon vraie return true sinon false 
        robot ,obstacle -> bool""" 
        for obstacle in self.obstacles:
            if(self.robot.px + self.robot.size + self.robot.dx > obstacle.px and self.robot.px + self.robot.dx < obstacle.px + obstacle.larg and self.robot.py + self.robot.size +self.robot.dy > obstacle.py and self.robot.py + self.robot.dy < obstacle.py + obstacle.haut) :
                return True
        return False 
    
    def collision_obstacle_reculer(self):
        """test la collision sur x
        test la collision sur y 
        si les deux soon vraie return true sinon false 
        robot ,obstacle -> bool""" 
        for obstacle in self.obstacles:
            if(self.robot.px + self.robot.size - self.robot.dx > obstacle.px and self.robot.px - self.robot.dx < obstacle.px + obstacle.larg and self.robot.py + self.robot.size - self.robot.dy > obstacle.py and self.robot.py - self.robot.dy < obstacle.py + obstacle.haut) :
                return True
        return False 

    
