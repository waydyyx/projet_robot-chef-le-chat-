from modele.robot import Robot, UPDATE_TIME
from traducteur.state import Robot_IRL

class AvancerDroit:
    def __init__(self, robot:Robot, distance, vitesse):
        self.distance = distance
        self.vitesse = vitesse
        self.robot = robot
        self.parcouru=0

    def start(self):
        self.parcouru=0
        self.robot.set_rot(0)

    def step(self):
        # self.parcouru += self.vitesse * self.robot.ray / UPDATE_TIME
        if self.stop():return
        with self.robot.lock:
            self.robot.change_vitesse(self.vitesse,self.vitesse)
    
    def stop(self):
        return (self.robot.get_rot()[0]*self.robot.ray+self.robot.get_rot()[1]*self.robot.ray)/2 > self.distance
    
class Tourner:
    def __init__(self, robot:Robot, angle, vitesse):
        self.angle=angle
        if self.angle < 0:
            self.vit_g = vitesse * (-1)
            self.vit_d = vitesse
        else:
            self.vit_g = vitesse
            self.vit_d = vitesse * (-1)
        self.robot = robot
        print("obj",abs(self.angle*(self.robot.size/2)))
        # self.parcouru = (self.vit_g*self.robot.ray / UPDATE_TIME - self.vit_d * self.robot.ray / UPDATE_TIME) / self.robot.size

    def start(self):
        # self.parcouru=0
        self.robot.set_rot(0)

    def step(self):
        # self.parcouru += (self.vit_g*self.robot.ray / UPDATE_TIME - self.vit_d * self.robot.ray / UPDATE_TIME) / self.robot.size
        with self.robot.lock:
            self.robot.change_vitesse(self.vit_g, self.vit_d)
        if self.stop():
            print(self.parcouru)
            print(self.angle)
        # self.robot.update_pos()

    def stop(self):
        return abs(self.robot.get_rot()[1]*self.robot.ray)>abs(self.angle*(self.robot.size/2))
