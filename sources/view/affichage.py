from sources.modele.arene import Arene
from sources.controleur.control import traiter_touche
from pygame import gfxdraw
import pygame
import time 
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
                if arene.stop == 1:
                    return 

    def start(self, arene : Arene):
        pygame.init()
        clock = pygame.time.Clock()
        # Lecture des touches
        while not(arene.stop):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    traiter_touche(arene, "QUIT")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        traiter_touche(arene, "ESC")
                    elif event.key == pygame.K_a:
                        traiter_touche(arene, "a")
                    
                    elif event.key == pygame.K_q:
                        traiter_touche(arene, "q")
                    
                    elif event.key == pygame.K_e:
                        traiter_touche(arene, "e")
                    
                    elif event.key == pygame.K_d:
                        traiter_touche(arene, "d")
                    
                    elif event.key == pygame.K_c:
                        traiter_touche(arene, "c")
                    
                    elif event.key == pygame.K_r:
                        traiter_touche(arene, "r")
                    
                    elif event.key == pygame.K_p:
                        traiter_touche(arene, "p")
                    
                    elif event.key == pygame.K_UP:
                        traiter_touche(arene, "UP")
                    
                    elif event.key == pygame.K_DOWN:
                        traiter_touche(arene, "DOWN")
                    
                    elif event.key == pygame.K_LEFT:
                        traiter_touche(arene, "LEFT")
                    
                    elif event.key == pygame.K_RIGHT:
                        traiter_touche(arene, "RIGHT")

                    elif event.key == pygame.K_k:
                        traiter_touche(arene, "k")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_z]:
                traiter_touche(arene, "z")

            with arene.stop_lock:
                if (arene.stop == 1):
                    return 
            print(f"vit_g: {arene.robot.vitesse_g}, vit_d: {arene.robot.vitesse_d} px: {int(arene.robot.px)} py: {int(arene.robot.py)} obstacle: {arene.detection_obstacle()}")
            clock.tick(60)

    def affiche_obstacle(self, arene:Arene):
        for ob in arene.obstacles:
            for x in range (ob.px , ob.px + ob.larg):
                for y in range (ob.py , ob.py + ob.haut):
                    pygame.gfxdraw.pixel(self.screen,x,y,(1, 1, 1))





