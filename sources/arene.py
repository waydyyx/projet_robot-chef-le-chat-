import random
import math
from pygame import gfxdraw
from multiprocessing import RLock

class Obstacle:
    def __init__(self, px:int, py:int, larg:int, haut:int):
        self.px=px
        self.py=py
        self.larg=larg
        self.haut=haut

class Arene:
    def __init__(self, larg : int, haut : int, robot : "Robot"):
        self.larg = larg
        self.haut = haut
        self.robot = robot
        self.obstacles=[Obstacle(random.randint(0,larg),random.randint(0,haut), random.randint(15, 100), random.randint(15, 100)) for x in range (10)] 
        self.robot_lock = RLock()
        self.stop = 0
        self.stop_lock = RLock()

    # def est_dehors_avancer(self):
    #     if (self.robot.dx < 0 or self.robot.dx > self.larg - self.robot.size or self.robot.dy < 0 or self.robot.dy > self.haut - self.robot.size):
    #         return (1)
    #     return (0)
	
    # def est_dehors_reculer(self):
    #     if (self.robot.dx < 0 or self.robot.dx > self.larg - self.robot.size or self.robot.dy < 0 or self.robot.dy > self.haut - self.robot.size):
    #         return (1)
    #     return (0)
    
    def collision_bord(self):
        #avancer
        if (self.robot.px < 0 or self.robot.px > self.larg - self.robot.size or self.robot.py < 0 or self.robot.py > self.haut - self.robot.size):
            return (1)
        return (0)
    
    
    # def est_dehors_reculer(self):
    #     if (self.robot.px - self.robot.dx < 0 or self.robot.px - self.robot.dx > self.larg - self.robot.size or self.robot.py - self.robot.dy < 0 or self.robot.py - self.robot.dy > self.haut - self.robot.size):
    #         return (1)
    #     return (0)
    
    def collision_obstacle(self):
        """test la collision sur x
        test la collision sur y 
        si les deux soon vraie return true sinon false 
        robot ,obstacle -> bool""" 
        for obstacle in self.obstacles:
            if(self.robot.px + self.robot.size > obstacle.px and self.robot.px < obstacle.px + obstacle.larg and self.robot.py + self.robot.size > obstacle.py and self.robot.py < obstacle.py + obstacle.haut) :
                return True
        return False 
    
    # def collision_obstacle_reculer(self):
    #     """test la collision sur x
    #     test la collision sur y 
    #     si les deux soon vraie return true sinon false 
    #     robot ,obstacle -> bool""" 
    #     for obstacle in self.obstacles:
    #         if(self.robot.px + self.robot.size - self.robot.dx > obstacle.px and self.robot.px - self.robot.dx < obstacle.px + obstacle.larg and self.robot.py + self.robot.size - self.robot.dy > obstacle.py and self.robot.py - self.robot.dy < obstacle.py + obstacle.haut) :
    #             return True
    #     return False 
    
    def detection_obstacle(self): # prend un screen en parametre si on veut afficher
        """
        Docstring for detection_obstacle
        
        :param self: Description
        """
        centre = self.robot.size / 2
        # length, height = screen.get_size()
        i = 0
        angle =- self.robot.angle
        while ((self.robot.px + math.cos(-angle) * i + centre < self.larg and self.robot.px + math.cos(-angle) * i + centre >= 0 and self.robot.py + math.sin(-angle) * i + centre < self.haut and self.robot.py + math.sin(-angle)* i + centre >= 0) and not(self.collision_point(int(self.robot.px + math.cos(-angle) * i + centre), int(self.robot.py + math.sin(-angle) * i + centre)))):
            # gfxdraw.pixel(screen, int(self.robot.px + math.cos(-angle) * i + centre), int(self.robot.py + math.sin(-angle) * i + centre), (0, 255, 5))
            i += 1
        # print((i-25)*17/50)
        return i < 50
    
    def collision_point(self,x,y):
        for obstacle in self.obstacles:
            if (x < obstacle.px + obstacle.larg) and (y < obstacle.py + obstacle.haut) and ( x > obstacle.px) and ( y > obstacle.py):
                return True
        return False
        
