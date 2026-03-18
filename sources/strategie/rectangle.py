import time
from sources.modele.arene import Arene
from sources.modele.robot import Robot
import math


def rectangle(arene: Arene, longeur: int, hauteur: int, vitesse: int):
    d = arene.robot.vitesse_d 
    g = arene.robot.vitesse_g
    for i in range (2):
        with arene.robot.lock:
            arene.robot.strat_avancer(longeur,vitesse)
            arene.robot.tourner_droite(90)
            arene.robot.strat_avancer(hauteur,vitesse)
            arene.robot.tourner_droite(90)
    with arene.robot.lock:
        arene.robot.change_vitesse(g,d)
    return 