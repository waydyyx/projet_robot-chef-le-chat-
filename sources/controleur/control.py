
import pygame 
from sources.modele.arene import Arene
from sources.strategie.carree import carre
from sources.strategie.rectangle import rectangle
from sources.strategie.autonome import autonome
from threading import Thread
from sources.view.affichage import Affichage
from sources.modele.update_modele import update_mod





def start(arene: Arene):
    pygame.init()
    clock = pygame.time.Clock()

    # afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)))
    # Thread(target=afficheur.affiche,args=(arene,)).start()

    # Thread(target=update_mod,args=(arene,)).start()

    while not(arene.stop):	
        for event in pygame.event.get():
            # on arrete le programme en cas de collision + arene.stop est mis a 1 pour que le thread s'arrete.
            # if (event.type == pygame.QUIT or arene.collision_bord() or arene.collision_obstacle()):
            #     with arene.stop_lock:
            #         arene.stop = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    with arene.stop_lock:
                        arene.stop = 1
                        return

            # Strategies
                if event.key == pygame.K_c:
                    carre(arene, 35, 10)
                elif event.key == pygame.K_r:
                    rectangle(arene, 70, 35, 10)
                elif event.key == pygame.K_p:
                    autonome(arene, 2)
                elif event.key == pygame.K_k:
                    arene.robot.strat_avancer(25)

            # Changement directe de la vitesse des roues
                if event.key == pygame.K_e:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d + 1)
                if event.key == pygame.K_d:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d - 1)        
                if event.key == pygame.K_a:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g + 1,  arene.robot.vitesse_d)
                if event.key == pygame.K_q:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g - 1,  arene.robot.vitesse_d)

            # Preset sur les fleches directionnelles
                if event.key == pygame.K_UP:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(4, 4)
                if event.key == pygame.K_RIGHT:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(2, -2)
                if event.key == pygame.K_DOWN:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(-4, -4)
                if event.key == pygame.K_LEFT:
                    with arene.robot.lock:
                        arene.robot.change_vitesse(-2, 2)

        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_w] or pressed[pygame.K_z]):
            with arene.robot.lock:
                arene.robot.avancer()
        clock.tick(60)
    pygame.quit()    