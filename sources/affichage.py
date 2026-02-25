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

    
