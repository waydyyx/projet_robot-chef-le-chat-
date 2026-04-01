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
    autonome = Sequence([Strat_while(AvancerDroit(robot,10, 10), arene.detection_obstacle), Tourner(robot, math.pi / 2,5)])
    carre = Sequence([AvancerDroit(robot, 50, 5), Tourner(robot, math.pi / 2.0966, 5)])
    tab_strat.append(Strat_for(autonome, 1))
    tab_strat.append(Strat_for(carre, 4))
    return tab_strat + [arene]

class Control:
    def __init__(self, tab_strat):
        self.tab_strat = tab_strat
    def exec_strat(self, strat):
        while not strat.stop():
            with self.tab_strat[-1].stop_lock:
                if self.tab_strat[-1].stop == 1:
                    return
            strat.step()
            time.sleep(1 / UPDATE_TIME)

    def start(self):
        for i in range(len(self.tab_strat) - 1):
            self.exec_strat(self.tab_strat[i])
            with self.tab_strat[-1].stop_lock:
                if self.tab_strat[-1].stop == 1:
                    break
        with self.tab_strat[-1].stop_lock: # celle la
            self.tab_strat[-1].stop = 1            # Si on ne veut pas que le programme sarrete il faut commenter les deux lignes
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