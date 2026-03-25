from modele.arene import Arene
from modele.robot import Robot, UPDATE_TIME
from controleur.touche import traiter_touche
from modele.update_modele import update_mod
from pygame import gfxdraw
import pygame
import time 
import math
from threading import Thread
class Affichage :
    def __init__(self , screen, arene):
        self.screen = screen
        self.screen_larg, self.screen_haut = screen.get_size()
        self.img_robot = pygame.image.load("images/robot_exceptionnel.png").convert_alpha()
        self.img_robot_larg, self.img_robot_haut = self.img_robot.get_size()
        self.arene=arene

    def affiche(self):
        while (True):
            self.screen.fill((255, 255, 255))
            self.affiche_obstacle()
            with self.arene.robot.lock:
                img_robot_rotation = pygame.transform.rotate(self.img_robot, -math.degrees(self.arene.robot.angle) + 90)
                rect = img_robot_rotation.get_rect(center=((self.arene.robot.px + self.img_robot_larg / 2),(self.arene.robot.py + self.img_robot_haut / 2)))
            self.screen.blit(img_robot_rotation, rect)  
            pygame.gfxdraw.pixel(self.screen,125,100,(0, 0, 255))
            pygame.display.flip()
            with self.arene.stop_lock:
                if self.arene.stop == 1:
                    return 

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        # Lecture des touches
        while not(self.arene.stop):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    traiter_touche(self.arene, "QUIT")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        traiter_touche(self.arene, "ESC")
                    elif event.key == pygame.K_a:
                        traiter_touche(self.arene, "a")
                    
                    elif event.key == pygame.K_q:
                        traiter_touche(self.arene, "q")
                    
                    elif event.key == pygame.K_e:
                        traiter_touche(self.arene, "e")
                    
                    elif event.key == pygame.K_d:
                        traiter_touche(self.arene, "d")
                    
                    elif event.key == pygame.K_c:
                        traiter_touche(self.arene, "c")
                    
                    elif event.key == pygame.K_r:
                        traiter_touche(self.arene, "r")
                    
                    elif event.key == pygame.K_p:
                        traiter_touche(self.arene, "p")
                    
                    elif event.key == pygame.K_UP:
                        traiter_touche(self.arene, "UP")
                    
                    elif event.key == pygame.K_DOWN:
                        traiter_touche(self.arene, "DOWN")
                    
                    elif event.key == pygame.K_LEFT:
                        traiter_touche(self.arene, "LEFT")
                    
                    elif event.key == pygame.K_RIGHT:
                        traiter_touche(self.arene, "RIGHT")

                    elif event.key == pygame.K_k:
                        traiter_touche(self.arene, "k")

                    elif event.key == pygame.K_t:
                        traiter_touche(self.arene, "t")

            pressed = pygame.key.get_pressed()
            # if pressed[pygame.K_z]:
            #     traiter_touche(self.arene, "z")

            with self.arene.stop_lock:
                if (self.arene.stop == 1):
                    return 
            clock.tick(UPDATE_TIME)

    def affiche_obstacle(self):
        for ob in self.arene.obstacles:
            for x in range (ob.px , ob.px + ob.larg):
                for y in range (ob.py , ob.py + ob.haut):
                    pygame.gfxdraw.pixel(self.screen,x,y,(1, 1, 1))





