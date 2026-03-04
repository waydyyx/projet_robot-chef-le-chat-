from sources.modele.arene import Arene

from sources.strategie.rectangle import rectangle
from sources.strategie.autonome import autonome
from sources.strategie.carree import carre

import time 
import pygame
from pygame import gfxdraw
import math

class Affichage :
    def __init__(self , screen):
        self.screen = screen
        self.screen_larg, self.screen_haut = screen.get_size()
        self.img_robot = pygame.image.load("images/robot_exceptionnel.png").convert_alpha()
        self.img_robot_larg, self.img_robot_haut = self.img_robot.get_size()

    def affiche(self, arene : Arene):
        while (True):
            self.screen.fill((255, 255, 255))
            self.affiche_obstacle(arene)
            with arene.robot.lock:
                img_robot_rotation = pygame.transform.rotate(self.img_robot, -math.degrees(arene.robot.angle) + 90)
                rect = img_robot_rotation.get_rect(center=((arene.robot.px + self.img_robot_larg / 2),(arene.robot.py + self.img_robot_haut / 2)))
            self.screen.blit(img_robot_rotation, rect)
            pygame.gfxdraw.pixel(self.screen,125,100,(0, 0, 255))
            pygame.display.flip()
            with arene.stop_lock:
                if (arene.stop == 1):
                    return 
            print(f"vit_g: {arene.robot.vitesse_g}, vit_d: {arene.robot.vitesse_d} px: {int(arene.robot.px)} py: {int(arene.robot.py)} obstacle: {arene.detection_obstacle()}")

    def affiche_obstacle(self, arene:Arene):
        for ob in arene.obstacles:
            for x in range (ob.px , ob.px + ob.larg):
                for y in range (ob.py , ob.py + ob.haut):
                    pygame.gfxdraw.pixel(self.screen,x,y,(1, 1, 1))


