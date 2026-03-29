from modele.arene import Arene
from modele.robot import Robot, UPDATE_TIME
import time
import math
class AvancerDroit:
    def __init__(self, robot:Robot, distance, vitesse):
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
    def __init__(self, robot:Robot, angle, vitesse):
        self.angle=angle
        if self.angle < 0:
            self.vit_g = vitesse * (-1)
            self.vit_d = vitesse
        else:
            self.vit_g = vitesse
            self.vit_d = vitesse * (-1)
        self.robot = robot
        self.parcouru = (self.vit_g*self.robot.ray / UPDATE_TIME - self.vit_d * self.robot.ray / UPDATE_TIME) / self.robot.size

    def start(self):
        self.parcouru=0

    def step(self):
        self.parcouru += (self.vit_g*self.robot.ray / UPDATE_TIME - self.vit_d * self.robot.ray / UPDATE_TIME) / self.robot.size
        with self.robot.lock:
            self.robot.change_vitesse(self.vit_g, self.vit_d)
        if self.stop():
            print(self.parcouru)
            print(self.angle)
        # self.robot.update_pos()

    def stop(self):
        return abs(self.parcouru)>abs(self.angle)

# class Rectangle:
#     def __init__(self, robot: Robot, longueur, largeur, vitesse):
#         self.robot = robot
#         self.strats = [AvancerDroit(robot, longueur, vitesse), Tourner(robot, math.pi / 2, vitesse), AvancerDroit(robot, largeur, vitesse), Tourner(robot, math.pi / 2, vitesse), AvancerDroit(robot, longueur, vitesse), Tourner(robot, math.pi / 2, vitesse), AvancerDroit(robot, largeur, vitesse), Tourner(robot, math.pi / 2, vitesse)]
#         self.cur = -1

#     def start(self):
#         self.cur = -1

#     def step(self):
#         if self.stop(): return
#         if self.cur < 0 or self.strats[self.cur].stop():
#             self.cur += 1
#             self.strats[self.cur].start()
#         self.strats[self.cur].step()

#     def stop(self):
#         return self.cur == len(self.strats) - 1 and self.strats[self.cur].stop()
    

# class Autonome:
#     def __init__(self, arene: Arene, robot: Robot, vitesse, max_collision: int):
#         self.arene = arene
#         self.robot = robot
#         self.nb_collision = 0
#         self.max_collision = max_collision
#         self.strats = [AvancerDroit(robot, 2000, vitesse), Tourner(robot, 2 * math.pi / 3, vitesse)]
#         self.cur = 0
#         self.detec_obstacle = False

#     def start(self):
#         self.cur = 0

#     def step(self):
#         if self.stop(): return
#         if (self.strats[self.cur].stop() and self.cur == 1):
#             self.cur = 0
#             self.detec_obstacle = False
#         if self.detec_obstacle == False and self.arene.detection_obstacle():
#             self.cur = 1
#             self.strats[self.cur].start()
#             self.detec_obstacle = True
#             self.nb_collision += 1
#         self.strats[self.cur].step()

#     def stop(self):
#         with self.arene.stop_lock:
#             if self.arene.stop == 1:
#                 return True
#         return self.nb_collision == self.max_collision


class Sequence:
    def __init__(self, seq):
        self.strats = seq
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
    

class Strat_while:
    def __init__(self,strat,condition):
        self.strat = strat
        self.cond=condition

    def start(self):
        self.strat.start()

    def step(self):
        self.strat.step()

    def stop(self):
        return self.cond()
    
class Strat_for:
    def __init__(self, strat, n):
        self.max=n
        self.curr=0
        self.strat=strat

    def start(self):
        self.curr=0

    def step(self):
        if self.strat.stop():
            self.curr+=1
            self.strat.start()
        self.strat.step()

    def stop(self):
        return self.curr>=self.max
        

