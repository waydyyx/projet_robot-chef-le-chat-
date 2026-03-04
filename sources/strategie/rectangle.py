import time
from sources.modele.arene import Arene
from sources.modele.robot import Robot
import math


def rectangle(arene: Arene , longeur: int, hauteur: int, vitesse: int):
        d = arene.robot.vitesse_d 
        g = arene.robot.vitesse_g
        arene.robot.vitesse_d = vitesse
        arene.robot.vitesse_g = vitesse
        for i in range (2):
            arene.robot.vitesse_d = vitesse
            arene.robot.vitesse_g = vitesse
            for j in range(longeur) :
                if (arene.collision_bord() or arene.collision_obstacle()):
                    arene.robot.vitesse_g = g 
                    arene.robot.vitesse_d = d
                    return
                with arene.robot.lock: 
                    arene.robot.avancer()
                time.sleep(1/60)
            arene.robot.vitesse_d = -math.pi/2
            arene.robot.vitesse_g = math.pi/2
            for i in range(25):
                if (arene.collision_bord() or arene.collision_obstacle()):
                    arene.robot.vitesse_g = g
                    arene.robot.vitesse_d = d
                    return
                with arene.robot.lock: 
                    arene.robot.avancer()
                time.sleep(1/60)
            arene.robot.vitesse_d = vitesse
            arene.robot.vitesse_g = vitesse
            for k in range (hauteur):
                if (arene.collision_bord() or arene.collision_obstacle()):
                    arene.robot.vitesse_g = g
                    arene.robot.vitesse_d = d
                    return
                with arene.robot.lock:
                    arene.robot.avancer()
                time.sleep(1/60)
            arene.robot.vitesse_d = -math.pi/2
            arene.robot.vitesse_g = math.pi/2
            for i in range(25):
                if (arene.collision_bord() or arene.collision_obstacle()):
                    arene.robot.vitesse_g = g
                    arene.robot.vitesse_d = d
                    return 
                with arene.robot.lock:
                    arene.robot.avancer()
                time.sleep(1/60)
        arene.robot.vitesse_g = g
        arene.robot.vitesse_d = d
        return 