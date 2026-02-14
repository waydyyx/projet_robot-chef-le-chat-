import math 
import pygame
import time 
from affichage import *

class Robot:
    def __init__(self, vitesse_d: int, vitesse_g: int, vitesse_rot :  int, angle : int, px : int = 0, py : int = 0):
        """
		:param vitesse_d: valeur compris entre 0-10 inclus pour choisir la vitesse_droite du robot
		:type vitesse: int
        :param vitesse_g: valeur compris entre 0-10 inclus pour choisir la vitesse_gauche du robot
		:type vitesse: int
		:param vitesse_rotation: valeur compris entre 0-10 inclus pour choisir la vitesse de rotation du robot
		:type vitesse_rotation: int
		:param angle: valeur compris entre 0-359 inclus pour choisir l'angle du depart du robot
		:type angle: int
		:param px: position x du robot
		:type px: int
		:param py: position y du robot
		:type py: int 
		"""

        # VITESSE_DROITE
        if (vitesse_d > 100):
            self.vitesse_d = 100
        elif (vitesse_d < 0):
            self.vitesse_d = 0
        else:
            self.vitesse_d = vitesse_d

        # VITESSE GAUCHE
        if (vitesse_g > 100):
            self.vitesse_g = 100
        elif (vitesse_g < 0):
            self.vitesse_g = 0
        else:
            self.vitesse_g = vitesse_g

        if (vitesse_rot > 10):
            self.vitesse_rot = 10
        elif (vitesse_rot < 0):
            self.vitesse_rot = 0
        else:
            self.vitesse_rot = vitesse_rot

        # ANGLE EN DEGREE
        if (angle > 359):
            self.angle = math.radians(359)
        elif (angle < 0):
            self.angle = 0
        else:		
            self.angle = math.radians(angle)

        self.px = px  # position x
        self.py = py  # position y 
        self.dx = math.cos(self.angle) * vitesse_g  # direction x (vecteur x ?)
        self.dy = math.sin(self.angle) * vitesse_d  # direction y (vecteur y ?)
        self.size = 50
        self.vitesse = 3

    def avancer(self):
        self.px += self.dx
        self.py += self.dy
        # self.angle += (math.pi / (110 - self.vitesse_d-self.vitesse_g * 10)) 
        if (self.vitesse_d > self.vitesse_g):
            self.angle -= (math.pi / (520 - (self.vitesse_d - self.vitesse_g) * 5))
            self.dx = math.cos(self.angle) * self.vitesse
            self.dy = math.sin(self.angle) * self.vitesse    
        elif (self.vitesse_g > self.vitesse_d):
            self.angle += (math.pi / (520 - (self.vitesse_g - self.vitesse_d) * 5))
            self.dx = math.cos(self.angle) * self.vitesse
            self.dy = math.sin(self.angle) * self.vitesse
        return (self.px, self.py, self.angle)

    def tourner_droite(self, angle : int = 0):
        if (angle != 0):
            self.angle += math.radians(angle)
        else:
            self.angle += (math.pi / (110 - self.vitesse_rot * 10)) 
        self.angle = self.angle % (2 * math.pi)
        self.dx = math.cos(self.angle) * self.vitesse
        self.dy = math.sin(self.angle) * self.vitesse

    def reculer(self):
        self.px -= self.dx
        self.py -= self.dy
        return (self.px, self.py, self.angle)

    def tourner_gauche(self, angle : int = 0):
        if (angle != 0):
            self.angle -= math.radians(angle)
        else:
            self.angle -= (math.pi / (110 - self.vitesse_rot * 10))
        self.angle = self.angle % (2 * math.pi)
        self.dx = math.cos(self.angle) * self.vitesse
        self.dy = math.sin(self.angle) * self.vitesse

    # def affiche_robot(self, screen):
    # 	for y in range(self.size):
    # 		for x in range(self.size):
    # 			pygame.gfxdraw.pixel(screen, int(self.px + x), int(self.py + y), (255, 0, 0))

    # def affiche_direction(self, screen):
    # 	centre = self.size / 2
    # 	length, height = screen.get_size()
    # 	i = 0
    # 	# while (x + math.cos(self.angle) * i + centre < length and x + math.cos(self.angle) * i + centre >= 0 and y + math.sin(self.angle) * i + centre < height and y + math.sin(self.angle)* i + centre >= 0):
    # 	while (i < self.size * 5):
    # 		pygame.gfxdraw.pixel(screen, int(self.px + math.cos(self.angle) * i + centre), int(self.py + math.sin(self.angle) * i + centre), (0, 255, 5))
    # 		i += 1

    # def carre(self, afficheur : Affichage, arene, deplacement : int):
    #     for i in range (4):
    #         for j in range (deplacement):
    #             self.avancer()
    #             afficheur.affiche(arene)
    #             time.sleep(0.1)
    #         self.tourner_droite(90)



    def rectangle( self, longeur : int, hauteur : int):
            rob = Robot( self.vitesse , self.vitesse_rotation, math.degrees(self.angle), self.px, self.py)
            liste_coordonnes = []
            for i in range (2):
                for j in range(longeur) :
                    liste_coordonnes.append( rob.avancer())
                rob.tourner_droite(90)
                for k in range (hauteur):
                    liste_coordonnes.append(rob.avancer())
                rob.tourner_droite(90)
            liste_coordonnes.append((rob.px, rob.py, rob.angle))
            return liste_coordonnes

        
    def carre(self,  deplacement : int):
            
        return self.rectangle( deplacement, deplacement)
            # rob = Robot(self.vitesse, self.vitesse_rotation, math.degrees(self.angle), self.px, self.py)
            # # print(f"self.angle : {math.degrees(self.angle)}")
            # liste_coordonnes = []
            # for i in range (4):
            #     for j in range (deplacement):
            #         liste_coordonnes.append(rob.avancer())
            #     rob.tourner_droite(90)
            # liste_coordonnes.append((rob.px, rob.py, rob.angle))
            # return liste_coordonnes

    def autonome(self, arene):
        liste_coordonnes = []
        while not(arene.detection_obstacle()) :
            if arene.collision_obstacle_avancer() or arene.est_dehors_avancer():
                self.tourner_droite(120)
                liste_coordonnes.append((self.px,self.py,self.angle))
                return liste_coordonnes
            liste_coordonnes.append(self.avancer())
        #self.reculer()
        self.tourner_droite(90)
        liste_coordonnes.append((self.px,self.py,self.angle))
        return liste_coordonnes