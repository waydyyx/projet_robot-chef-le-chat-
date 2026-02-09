import pygame
from arene import *
from obstacle import *
import time 

# def affichage_init(arene:Arene):
#     arene.screen = pygame.display.set_mode((arene.larg, arene.haut))
#     arene.img_car=pygame.image.load("../images/robot_exceptionnel.png").convert_alpha()
#     arene.rob_larg, arene.rob_haut = arene.img_car.get_size()


# def affichage(arene:Arene):
#     arene.screen.fill((255, 255, 255))
#     img_car_rotation = pygame.transform.rotate(arene.img_car, -math.degrees(arene.robot.angle) + 90)
# 	# print(f"{img_car_rotation}")
#     rect=img_car_rotation.get_rect(center=((arene.robot.px + arene.rob_larg / 2),(arene.robot.py + arene.rob_haut / 2)))
#     arene.screen.blit(img_car_rotation, rect)
# 	# arene.robot.affiche_direction(screen)
# 	# arene.robot.affiche_robot(screen)
# 	# pygame.draw.rect(screen, (255, 0, 0), rect)
# 	# pygame.gfxdraw.pixel(screen, int((arene.robot.px + arene.rob_larg / 2) + (arene.rob_larg / 4) * math.cos(arene.robot.angle)), int((robot.py + arene.rob_haut / 2) + (arene.rob_haut / 4) * math.sin(robot.angle)), (255, 0, 0))
#     pygame.display.flip()



class Affichage :
    def __init__(self , screen):
        self.screen = screen
        self.screen_larg, self.screen_haut = screen.get_size()
        self.img_robot = pygame.image.load("../images/robot_exceptionnel.png").convert_alpha()
        self.img_robot_larg, self.img_robot_haut = self.img_robot.get_size()

    def affiche(self, arene : Arene):
        self.screen.fill((255, 255, 255))
        img_robot_rotation = pygame.transform.rotate(self.img_robot, -math.degrees(arene.robot.angle) + 90)
        # print(f"{img_car_rotation}")
        rect = img_robot_rotation.get_rect(center=((arene.robot.px + self.img_robot_larg / 2),(arene.robot.py + self.img_robot_haut / 2)))
        self.screen.blit(img_robot_rotation, rect)
        # arene.robot.affiche_direction(screen)
        # arene.robot.affiche_robot(screen)
        # pygame.draw.rect(screen, (255, 0, 0), rect)
        # pygame.gfxdraw.pixel(screen, int((arene.robot.px + arene.rob_larg / 2) + (arene.rob_larg / 4) * math.cos(arene.robot.angle)), int((robot.py + arene.rob_haut / 2) + (arene.rob_haut / 4) * math.sin(robot.angle)), (255, 0, 0))
        pygame.display.flip()


    def affiche_trajet(self, arene : Arene, liste_coordonnes: list) :
        for i in range (len(liste_coordonnes)):
            arene.robot.px = liste_coordonnes[i][0]
            arene.robot.py = liste_coordonnes[i][1]
            arene.robot.angle = liste_coordonnes[i][2]
            # arene.robot.dx = math.cos(arene.robot.angle) * 5
            # arene.robot.dy = math.sin(arene.robot.angle) * 5
            self.affiche(arene)
            time.sleep(1/ (len(liste_coordonnes) // 4))
        self.affiche(arene)
