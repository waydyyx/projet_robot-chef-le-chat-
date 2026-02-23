from affichage import Affichage
from arene import Arene
import math
import pygame

def rectangle(arene:Arene, longeur : int, hauteur : int, vitesse: int):
    d=arene.robot.vitesse_d 
    g=arene.robot.vitesse_g
    arene.robot.vitesse_d = vitesse
    arene.robot.vitesse_g = vitesse
    liste_coordonnes = []
    for i in range (2):
        arene.robot.vitesse_d = vitesse
        arene.robot.vitesse_g = vitesse
        for j in range(longeur) :
            if (arene.collision_bord() or arene.collision_obstacle()):
                arene.robot.vitesse_g = g 
                arene.robot.vitesse_d = d
                return liste_coordonnes
            liste_coordonnes.append(arene.robot.avancer())
        arene.robot.vitesse_d = -math.pi/2
        arene.robot.vitesse_g = math.pi/2
        for i in range(25):
            if (arene.collision_bord() or arene.collision_obstacle()):
                arene.robot.vitesse_g = g
                arene.robot.vitesse_d = d
                return liste_coordonnes
            liste_coordonnes.append( arene.robot.avancer())
        arene.robot.vitesse_d = vitesse
        arene.robot.vitesse_g = vitesse
        for k in range (hauteur):
            if (arene.collision_bord() or arene.collision_obstacle()):
                arene.robot.vitesse_g = g
                arene.robot.vitesse_d = d
                return liste_coordonnes
            liste_coordonnes.append(arene.robot.avancer())
        arene.robot.vitesse_d = -math.pi/2
        arene.robot.vitesse_g = math.pi/2
        for i in range(25):
            if (arene.collision_bord() or arene.collision_obstacle()):
                arene.robot.vitesse_g = g
                arene.robot.vitesse_d = d
                return liste_coordonnes
            liste_coordonnes.append(arene.robot.avancer())
    liste_coordonnes.append((arene.robot.px, arene.robot.py, arene.robot.angle))
    arene.robot.vitesse_g = g
    arene.robot.vitesse_d = d
    return liste_coordonnes

def carre(arene:Arene,deplacement : int, vitesse:int):
    return rectangle(arene, deplacement, deplacement, vitesse)


def start(arene:Arene):
    pygame.init()
    quit = 0
    afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)))
    clock = pygame.time.Clock()
    # print(arene.collision_point(90,90))

    autonome = None
    while not(quit):	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = 1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    liste = carre(arene,25,10)
                    # print(liste)
                    afficheur.affiche_trajet(arene, liste)
                    if (arene.collision_bord() or arene.collision_obstacle()):
                        pygame.quit()
                        return

                elif event.key == pygame.K_r:
                    liste = rectangle(arene,30,15,10)
                    afficheur.affiche_trajet(arene , liste)
                    if (arene.collision_bord() or arene.collision_obstacle()):
                        pygame.quit()
                        return

                elif event.key == pygame.K_p:
                    for x in range(10):
                        liste= arene.robot.autonome(arene)
                        afficheur.affiche_trajet(arene, liste)
                        if (arene.collision_bord() or arene.collision_obstacle()):
                            pygame.quit()
                            return 
                if event.key == pygame.K_e:
                    arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d + 1)
                elif event.key == pygame.K_d:
                    arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d - 1)        
                elif event.key == pygame.K_a:
                    arene.robot.change_vitesse(arene.robot.vitesse_g + 1,  arene.robot.vitesse_d)
                elif event.key == pygame.K_q:
                    arene.robot.change_vitesse(arene.robot.vitesse_g - 1,  arene.robot.vitesse_d)

        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_ESCAPE]):
            quit = 1
        if (pressed[pygame.K_w] or pressed[pygame.K_z]):
            if (arene.collision_bord() or arene.collision_obstacle()):
                pygame.quit()
                return
            arene.robot.avancer()

        # if ( pressed[pygame.K_c]):
        # 	arene.robot.carre(10)
        # 	# arene.robot.tourner_droite(90)
            # print("c")



        afficheur.affiche(arene)
        clock.tick(60)
    pygame.quit()