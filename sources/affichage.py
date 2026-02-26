import pygame
from arene import Arene
from arene import Obstacle
import time 
from pygame import gfxdraw
import math

class Affichage :
    def __init__(self , screen):
        self.screen = screen
        self.screen_larg, self.screen_haut = screen.get_size()
        self.img_robot = pygame.image.load("../images/robot_exceptionnel.png").convert_alpha()
        self.img_robot_larg, self.img_robot_haut = self.img_robot.get_size()

    def affiche(self, arene : Arene):
        while (True):
            self.screen.fill((255, 255, 255))
            self.affiche_obstacle(arene)
            # print(f"{img_car_rotation}")
            with arene.robot_lock:
                img_robot_rotation = pygame.transform.rotate(self.img_robot, -math.degrees(arene.robot.angle) + 90)
                rect = img_robot_rotation.get_rect(center=((arene.robot.px + self.img_robot_larg / 2),(arene.robot.py + self.img_robot_haut / 2)))
            self.screen.blit(img_robot_rotation, rect)
            # arene.robot.affiche_direction(screen)
            # arene.robot.affiche_robot(screen)
            # pygame.draw.rect(screen, (255, 0, 0), rect)
            # pygame.gfxdraw.pixel(screen, int((arene.robot.px + arene.rob_larg / 2) + (arene.rob_larg / 4) * math.cos(arene.robot.angle)), int((robot.py + arene.rob_haut / 2) + (arene.rob_haut / 4) * math.sin(robot.angle)), (255, 0, 0))
            pygame.gfxdraw.pixel(self.screen,125,100,(0, 0, 255))
            # print(arene.detection_obstacle())
            # print(arene.detection_obstacle(self))
            pygame.display.flip()
            with arene.stop_lock:
                if (arene.stop == 1):
                    return 

    def affiche_obstacle(self, arene:Arene):
        for ob in arene.obstacles:
            for x in range (ob.px , ob.px + ob.larg):
                for y in range (ob.py , ob.py + ob.haut):
                    pygame.gfxdraw.pixel(self.screen,x,y,(255, 0, 0))

def start(arene: Arene):
    pygame.init()
    # afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)))
    clock = pygame.time.Clock()
    autonome = None
    while not(arene.stop):	
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                arene.stop = 1
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    arene.robot.carre(arene, 7, 10)
                    if (arene.collision_bord() or arene.collision_obstacle()):
                        with arene.stop_lock:
                            arene.stop = 1
                        return

                elif event.key == pygame.K_r:
                    arene.robot.rectangle(arene, 15, 7, 10)
                    if (arene.collision_bord() or arene.collision_obstacle()):
                        with arene.stop_lock:
                            arene.stop = 1
                        return

                elif event.key == pygame.K_p:
                    arene.robot.autonome(arene, 2)
                    if (arene.collision_bord() or arene.collision_obstacle()):
                        with arene.stop_lock:
                            arene.stop = 1
                        return 
                if event.key == pygame.K_e:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d + 1)
                if event.key == pygame.K_d:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d - 1)        
                if event.key == pygame.K_a:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g + 1,  arene.robot.vitesse_d)
                if event.key == pygame.K_q:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(arene.robot.vitesse_g - 1,  arene.robot.vitesse_d)

                if event.key == pygame.K_UP:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(4, 4)
                if event.key == pygame.K_RIGHT:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(2, -2)
                if event.key == pygame.K_DOWN:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(-4, -4)
                if event.key == pygame.K_LEFT:
                    with arene.robot_lock:
                        arene.robot.change_vitesse(-2, 2)

        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_ESCAPE]):
            with arene.stop_lock:
                arene.stop = 1
        if (pressed[pygame.K_w] or pressed[pygame.K_z]):
            if (arene.collision_bord() or arene.collision_obstacle()):
                with arene.stop_lock:
                    arene.stop = 1
            with arene.robot_lock:
                arene.robot.avancer()
        print(f"vit_g: {arene.robot.vitesse_g}, vit_d: {arene.robot.vitesse_d} px: {arene.robot.px} py: {arene.robot.py} obstacle: {arene.detection_obstacle()}")
        clock.tick(60)
    pygame.quit()    
