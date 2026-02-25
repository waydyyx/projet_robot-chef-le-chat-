import math 
import pygame
import time 
from arene import Arene

class Robot:
    def __init__(self, vitesse_g: int, vitesse_d: int, angle : int = 270, px : int = 50, py : int = 50):
        """
		:param vitesse_d: valeur compris entre (-10, 10) inclus pour choisir la vitesse_droite du robot
		:type vitesse: int
        :param vitesse_g: valeur compris entre (-10, 10) inclus pour choisir la vitesse_gauche du robot
		:type vitesse: int
		:param angle: valeur compris entre 0-359 inclus pour choisir l'angle du depart du robot
		:type angle: int
		:param px: position x du robot
		:type px: int
		:param py: position y du robot
		:type py: int 
		"""

        # TAILLE ROBOT
        self.size = 50

        # distance entre les rous
        self.L =  self.size 

        # pas de temps
        self.dt = 0.1

        # VITESSE_DROITE
        if (vitesse_d > 10):
            self.vitesse_d = 10
        elif (vitesse_d < -10):
            self.vitesse_d = -10
        else:
            self.vitesse_d = vitesse_d

        # VITESSE GAUCHE
        if (vitesse_g > 10):
            self.vitesse_g = 10
        elif (vitesse_g < -10):
            self.vitesse_g = -10
        else:
            self.vitesse_g = vitesse_g

        
        self.vitesse_rot = 6

        # ANGLE EN DEGREE
        if (angle > 359):
            self.angle = math.radians(359)
        elif (angle < 0):
            self.angle = 0
        else:		
            self.angle = math.radians(angle)

        self.px = px  # position x
        self.py = py  # position y 

        self.dx = (self.vitesse_d + self.vitesse_g) / 2 * math.cos(self.angle + (self.vitesse_g - self.vitesse_d) / self.L)
        self.dy = (self.vitesse_d + self.vitesse_g) / 2 * math.sin(self.angle + (self.vitesse_g - self.vitesse_d) / self.L)

        self.vitesse = (self.vitesse_g+self.vitesse_d)/2


    def avancer(self):

        v = (self.vitesse_d + self.vitesse_g) / 2
        omega = (self.vitesse_g - self.vitesse_d) / self.L

        # mise à jour position
        self.px += self.dx 
        self.py += self.dy 

        # calcul déplacement
        self.dx = v * math.cos(self.angle + omega)
        self.dy = v * math.sin(self.angle + omega)



        # mise à jour angle
        self.angle += omega 
        self.angle = self.angle % (2 * math.pi)
        return (self.px, self.py, self.angle)


    #def tourner_droite(self, angle : int = 0):
    #    if (angle!=0):
    #        self.angle += math.radians(angle)
    #    else:
    #        self.angle += (math.pi / (110 - self.vitesse_rot))
    #    self.angle = self.angle % (2 * math.pi)
    #    v = (self.vitesse_d + self.vitesse_g) / 2
    #    self.dx = v * math.cos(self.angle)
    #    self.dy = v * math.sin(self.angle)

    def change_vitesse(self, vitesse_g, vitesse_d):
        self.vitesse_g = vitesse_g
        self.vitesse_d = vitesse_d
        if (self.vitesse_g > 10):
            self.vitesse_g = 10
        elif (self.vitesse_g < -10):
            self.vitesse_g = -10
        if (self.vitesse_d > 10):
            self.vitesse_d = 10
        elif (self.vitesse_d < -10):
            self.vitesse_d = -10


    #def tourner_gauche(self, angle : int = 0):
    #    if (angle!=0):
    #        self.angle -= math.radians(angle)
    #    else:
    #        self.angle -= (math.pi / (110 - self.vitesse_rot))
    #    self.angle = self.angle % (2 * math.pi)
    #    v = (self.vitesse_d + self.vitesse_g) / 2
    #    self.dx = v * math.cos(self.angle)
    #    self.dy = v * math.sin(self.angle)

    def rectangle(self, arene: Arene, longeur: int, hauteur: int, vitesse: int):
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
                with arene.robot_lock:
                    arene.robot.avancer()
                time.sleep(1/60)
            arene.robot.vitesse_d = -math.pi/2
            arene.robot.vitesse_g = math.pi/2
            for i in range(25):
                if (arene.collision_bord() or arene.collision_obstacle()):
                    arene.robot.vitesse_g = g
                    arene.robot.vitesse_d = d
                    return
                with arene.robot_lock:
                    arene.robot.avancer()
                time.sleep(1/60)
            arene.robot.vitesse_d = vitesse
            arene.robot.vitesse_g = vitesse
            for k in range (hauteur):
                if (arene.collision_bord() or arene.collision_obstacle()):
                    arene.robot.vitesse_g = g
                    arene.robot.vitesse_d = d
                    return
                with arene.robot_lock:
                    arene.robot.avancer()
                time.sleep(1/60)
            arene.robot.vitesse_d = -math.pi/2
            arene.robot.vitesse_g = math.pi/2
            for i in range(25):
                if (arene.collision_bord() or arene.collision_obstacle()):
                    arene.robot.vitesse_g = g
                    arene.robot.vitesse_d = d
                    return 
                with arene.robot_lock:
                    arene.robot.avancer()
                time.sleep(1/60)
        arene.robot.vitesse_g = g
        arene.robot.vitesse_d = d
        return 

    def carre(self, arene: Arene,deplacement: int, vitesse: int):
        return self.rectangle(arene, deplacement, deplacement, vitesse)
    

    def autonome(self, arene, nb_collision):
        with arene.robot_lock:
            self.change_vitesse(4, 4)
        for x in range(nb_collision):
            while not(arene.detection_obstacle()):
                if arene.collision_obstacle() or arene.collision_bord():
                    # self.tourner_droite(120)
                    # liste_coordonnes.append((self.px,self.py,self.angle))
                    return
                with arene.robot_lock:
                    self.avancer()
                time.sleep(1/60)
            self.tourner_droite(90)
        return
    

    