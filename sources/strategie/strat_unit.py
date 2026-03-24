from modele.robot import Robot, UPDATE_TIME
import time
import math
class AvancerDroit:
    def __init__(self,robot:Robot,distance,vitesse):
        self.distance=distance
        self.vitesse=vitesse
        self.robot=robot
        self.parcouru=0

    def start(self):
        self.parcouru=0

    def step(self):
        self.parcouru += self.vitesse * self.robot.ray / UPDATE_TIME
        if self.stop():return
        with self.robot.lock:
            self.robot.change_vitesse(self.vitesse,self.vitesse)
    
    def stop(self):
        return self.parcouru>self.distance
    
class Tourner:
    def __init__(self,robot:Robot,angle,vitesse):
        self.angle=angle
        if self.angle < 0:
            self.vit_g = vitesse * (-1)
            self.vit_d = vitesse
        else:
            self.vit_g = vitesse
            self.vit_d = vitesse * (-1)
        self.robot=robot
        self.parcouru=0

    def start(self):
        self.parcouru=0

    def step(self):
        self.parcouru += (self.vit_g*self.robot.ray / UPDATE_TIME - self.vit_d*self.robot.ray / UPDATE_TIME) / self.robot.size
        if self.stop():return
        with self.robot.lock:
            self.robot.change_vitesse(self.vit_g,self.vit_d)
        # self.robot.update_pos()

    def stop(self):
        return abs(self.parcouru)>abs(self.angle)

class Rectangle:
    def __init__(self, robot: Robot, longueur, largeur, vitesse):
        self.robot = robot
        self.strats = [AvancerDroit(robot, longueur, vitesse), Tourner(robot, math.pi / 2, vitesse), AvancerDroit(robot, largeur, vitesse), Tourner(robot, math.pi / 2, vitesse), AvancerDroit(robot, longueur, vitesse), Tourner(robot, math.pi / 2, vitesse), AvancerDroit(robot, largeur, vitesse), Tourner(robot, math.pi / 2, vitesse)]
        self.cur = -1

    def start(self):
        self.cur = -1

    def step(self):
        if self.stop(): return
        if self.cur < 0 or self.strats[self.cur].stop():
            self.cur += 1
            self.strats[self.cur].start()
        self.strats[self.cur].step()

    def stop(self):
        return self.cur == len(self.strats) - 1 and self.strats[self.cur].stop()