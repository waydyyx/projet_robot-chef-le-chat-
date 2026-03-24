from modele.arene import Arene
from strategie.carree import carre
from strategie.rectangle import rectangle
from strategie.autonome import autonome
from strategie.strat_unit import AvancerDroit, Tourner, Rectangle, Autonome, UPDATE_TIME
import time
import math



def traiter_touche(arene: Arene, cle: str):
    if cle == "z":
        with arene.robot.lock:
            arene.robot.update_pos()
    elif cle == "ESC" or cle == "QUIT":
        with arene.stop_lock:
            arene.stop = 1
    # changement directe de la vitesse des roues 
    elif cle  == "e":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d + 1)
    elif cle == "d":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d - 1)        
    elif cle == "a":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g + 1,  arene.robot.vitesse_d)
    elif cle =="q":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g - 1,  arene.robot.vitesse_d) 

    # strategie
    elif cle =="c":
        carre(arene, 35, 10)
    elif cle == "r":
        vd=arene.robot.vitesse_d
        vg=arene.robot.vitesse_g
        strat = Rectangle(arene.robot, 20, 10, 5)
        while(not strat.stop()):
            strat.step()
            time.sleep(1 / UPDATE_TIME)
        arene.robot.change_vitesse(vg, vd)
    elif cle == "p":
        vd=arene.robot.vitesse_d
        vg=arene.robot.vitesse_g
        strat = Autonome(arene, arene.robot, 5, 5)
        while not strat.stop():
            strat.step()
            time.sleep(1 / UPDATE_TIME)
        arene.robot.change_vitesse(vg,vd)
    elif cle =="k":
        # arene.robot.strat_avancer(100,5)
        vd=arene.robot.vitesse_d
        vg=arene.robot.vitesse_g
        strat=AvancerDroit(arene.robot,25,5)
        while not strat.stop():
            strat.step()
            time.sleep(1 / UPDATE_TIME)
        arene.robot.change_vitesse(vg,vd)
    elif cle =="t":
        # arene.robot.strat_avancer(100,5)
        vd=arene.robot.vitesse_d
        vg=arene.robot.vitesse_g
        strat=Tourner(arene.robot,math.pi/2,10)
        while not strat.stop():
            strat.step()
            time.sleep(1 / UPDATE_TIME)
        arene.robot.change_vitesse(vg,vd)

    # preset sur les fleches directionnelles
    elif cle =="UP":
        with arene.robot.lock:
            arene.robot.change_vitesse(4, 4)
    elif cle == "RIGHT":
        with arene.robot.lock:
            arene.robot.change_vitesse(2, -2)
    elif cle == "DOWN":
        with arene.robot.lock:
            arene.robot.change_vitesse(-4, -4)
    elif cle == "LEFT":
        with arene.robot.lock:
            arene.robot.change_vitesse(-2, 2)