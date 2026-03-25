# from traducteur.state import State
import math
from strategie.strat_unit import Tourner, AvancerDroit
import time
from threading import Thread
from modele.update_modele import update_mod
import pygame
from modele.arene import Arene

class Control:
    def __init__(self,arene):
        self.arene=arene
        self.robot=arene.robot

    def start(self):
        
        robot=self.robot
        vd=robot.vitesse_d
        vg=robot.vitesse_g
        strat=Tourner(robot,math.pi/2,5)
        while not strat.stop():
            strat.step()
            time.sleep(1/60)
        robot.change_vitesse(vg,vd)
        strat=AvancerDroit(robot,50,7)
        while not strat.stop():
            strat.step()
            time.sleep(1/60)
        robot.change_vitesse(vg,vd)
        print("fini")
        with self.arene.stop_lock:
            self.arene.stop_lock=1