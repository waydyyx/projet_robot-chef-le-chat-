import pygame
from class_robot import *

def gestion_touche(screen, event, robot):
	if event.type == pygame.QUIT:
				quit = 1
	pressed = pygame.key.get_pressed()
	if (pressed[pygame.K_ESCAPE]):
		quit = 1
	if (pressed[pygame.K_UP] or pressed[pygame.K_w] or pressed[pygame.K_z]):
		robot.avancer(screen)
	if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
		robot.tourner_droite()
	if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]):
		robot.reculer(screen)
	if (pressed[pygame.K_LEFT] or pressed[pygame.K_a] or pressed[pygame.K_q]):
		robot.tourner_gauche()
