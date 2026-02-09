import pygame
from pygame import gfxdraw
from robot import *
from arene import *
# from obstacle import *

def affichage_init(arene:Arene):
    arene.screen = pygame.display.set_mode((arene.larg, arene.haut))
    arene.img_car=pygame.image.load("../images/robot_exceptionnel.png").convert_alpha()
    arene.rob_larg, arene.rob_haut = arene.img_car.get_size()


def affichage(arene:Arene):
    arene.screen.fill((255, 255, 255))
    img_car_rotation = pygame.transform.rotate(arene.img_car, -math.degrees(arene.robot.angle) + 90)
	# print(f"{img_car_rotation}")
    rect=img_car_rotation.get_rect(center=((arene.robot.px + arene.rob_larg / 2),(arene.robot.py + arene.rob_haut / 2)))
    arene.screen.blit(img_car_rotation, rect)
	# arene.robot.affiche_direction(screen)
	# arene.robot.affiche_robot(screen)
	# pygame.draw.rect(screen, (255, 0, 0), rect)
	# pygame.gfxdraw.pixel(screen, int((arene.robot.px + arene.rob_larg / 2) + (arene.rob_larg / 4) * math.cos(arene.robot.angle)), int((robot.py + arene.rob_haut / 2) + (arene.rob_haut / 4) * math.sin(robot.angle)), (255, 0, 0))
    pygame.display.flip()