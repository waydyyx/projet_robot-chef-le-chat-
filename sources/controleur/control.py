# from traducteur.state import State
import math
from strategie.strat_unit import Tourner, AvancerDroit, UPDATE_TIME
from strategie.strat_general import Sequence, Strat_while, Strat_for
import time
from threading import Thread
from modele.update_modele import update_mod
import pygame
from modele.arene import Arene

def instruction_robot(arene, robot):
    tab_strat = []
    autonome = Sequence([Strat_while(AvancerDroit(robot,10,5), arene.detection_obstacle), Tourner(robot, math.pi / 2,5)])
    carre = Sequence([AvancerDroit(robot, 50, 5), Tourner(robot,math.pi/2,5)])
    tab_strat.append(Strat_for(autonome, 1))
    tab_strat.append(Strat_for(carre, 4))
    return tab_strat

class Control:
    def __init__(self, tab_strat, stop_lock: "Rlock", stop):
        self.tab_strat = tab_strat
        self.stop_lock, self.stop = stop_lock, stop
    def exec_strat(self, strat):
        while not strat.stop():
            with self.stop_lock:
                if self.stop == 1:
                    return
            strat.step()
            time.sleep(1 / UPDATE_TIME)

    def start(self):
        for strat in self.tab_strat:
            self.exec_strat(strat)
            with self.stop_lock:
                if self.stop == 1:
                    break
        with self.stop_lock:
            self.stop = 1
        print("strat fini")
    
# class Control:
#     def __init__(self,arene):
#         self.arene=arene
#         self.robot=arene.robot

#     def exec_strat(self,strat):
#         while not strat.stop():
#             with self.arene.stop_lock:
#                 if self.arene.stop == 1:
#                     return
#             strat.step()
#             time.sleep(1 / (UPDATE_TIME))

#     def start(self):
        
        
#         # strat=Sequence([AvancerDroit(robot,10,5),Tourner(robot,math.pi,5)])
#         # self.exec_strat(strat)
#         print("fini")
#         with self.arene.stop_lock:
#             self.arene.stop = 1