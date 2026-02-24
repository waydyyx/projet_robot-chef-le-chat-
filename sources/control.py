from affichage import Affichage
from arene import Arene
import math
import pygame
import time

def rectangle(arene:Arene, longeur : int, hauteur : int, vitesse: int):
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
            arene.robot.avancer()
            time.sleep(1/60)
        arene.robot.vitesse_d = -math.pi/2
        arene.robot.vitesse_g = math.pi/2
        for i in range(25):
            if (arene.collision_bord() or arene.collision_obstacle()):
                arene.robot.vitesse_g = g
                arene.robot.vitesse_d = d
                return
            arene.robot.avancer()
            time.sleep(1/60)
        arene.robot.vitesse_d = vitesse
        arene.robot.vitesse_g = vitesse
        for k in range (hauteur):
            if (arene.collision_bord() or arene.collision_obstacle()):
                arene.robot.vitesse_g = g
                arene.robot.vitesse_d = d
                return
            arene.robot.avancer()
            time.sleep(1/60)
        arene.robot.vitesse_d = -math.pi/2
        arene.robot.vitesse_g = math.pi/2
        for i in range(25):
            if (arene.collision_bord() or arene.collision_obstacle()):
                arene.robot.vitesse_g = g
                arene.robot.vitesse_d = d
                return 
            arene.robot.avancer()
            time.sleep(1/60)
    arene.robot.vitesse_g = g
    arene.robot.vitesse_d = d
    return 

def carre(arene:Arene,deplacement : int, vitesse:int):
    return rectangle(arene, deplacement, deplacement, vitesse)


def start(arene: Arene):
    pygame.init()
    # afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)))
    clock = pygame.time.Clock()
    autonome = None
    while not(arene.stop):	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = 1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    # print(liste)
                    # afficheur.affiche_trajet(arene, liste)
                    carre(arene, 7, 10)
                    if (arene.collision_bord() or arene.collision_obstacle()):
                        pygame.quit()
                        return

                elif event.key == pygame.K_r:
                    rectangle(arene, 15, 7, 10)
                    if (arene.collision_bord() or arene.collision_obstacle()):
                        pygame.quit()
                        return

                elif event.key == pygame.K_p:
                    for x in range(10):
                        liste= arene.robot.autonome(arene)
                        # afficheur.affiche_trajet(arene, liste)
                        if (arene.collision_bord() or arene.collision_obstacle()):
                            pygame.quit()
                            return 
                if event.key == pygame.K_e:
                    arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d + 1)
                if event.key == pygame.K_d:
                    arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d - 1)        
                if event.key == pygame.K_a:
                    arene.robot.change_vitesse(arene.robot.vitesse_g + 1,  arene.robot.vitesse_d)
                if event.key == pygame.K_q:
                    arene.robot.change_vitesse(arene.robot.vitesse_g - 1,  arene.robot.vitesse_d)

                if event.key == pygame.K_UP:
                    arene.robot.change_vitesse(4, 4)
                if event.key == pygame.K_RIGHT:
                    arene.robot.change_vitesse(2, -2)
                if event.key == pygame.K_DOWN:
                    arene.robot.change_vitesse(-4, -4)
                if event.key == pygame.K_LEFT:
                    arene.robot.change_vitesse(-2, 2)

        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_ESCAPE]):
            with arene.stop_lock:
                arene.stop = 1
        if (pressed[pygame.K_w] or pressed[pygame.K_z]):
            if (arene.collision_bord() or arene.collision_obstacle()):
                with arene.stop_lock:
                    arene.stop = 1
            arene.robot.avancer()
        print(f"vit_g: {arene.robot.vitesse_g}, vit_d: {arene.robot.vitesse_d}")
        # afficheur.affiche(arene)
        clock.tick(60)
    pygame.quit()