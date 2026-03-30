# from traducteur.state import State
import math
from strategie.strat_unit import Tourner, AvancerDroit, UPDATE_TIME
from strategie.strat_general import Sequence, Strat_while, Strat_for
import time
from threading import Thread
from modele.update_modele import update_mod
import pygame
from modele.arene import Arene

class Control:
    def __init__(self,arene):
        self.arene=arene
        self.robot=arene.robot

    def exec_strat(self,strat):
        while not strat.stop():
            with self.arene.stop_lock:
                if self.arene.stop == 1:
                    return
            strat.step()
            time.sleep(1 / (UPDATE_TIME))

    def start(self):
        
        robot = self.robot
        autonome = Sequence([Strat_while(AvancerDroit(robot,10,5), self.arene.detection_obstacle),Tourner(robot,math.pi/2,5)])
        carre = Sequence([AvancerDroit(robot, 20, 5), Tourner(robot,math.pi/2,5)])
        strat = Strat_for(autonome, 1)
        self.exec_strat(strat)
        strat = Strat_for(carre, 4)
        self.exec_strat(strat)
        # strat=Sequence([AvancerDroit(robot,10,5),Tourner(robot,math.pi,5)])
        # self.exec_strat(strat)
        print("fini")
        with self.arene.stop_lock:
            self.arene.stop = 1