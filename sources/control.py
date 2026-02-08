import pygame
from pygame import gfxdraw
from class_robot import *
from arene import *
from obstacle import *
from affichage import *

def start(arene:Arene):
	pygame.init()
	quit = 0
	affichage_init(arene)
	clock = pygame.time.Clock()
	while not(quit):	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = 1
		pressed = pygame.key.get_pressed()
		if (pressed[pygame.K_ESCAPE]):
			quit = 1
		if (pressed[pygame.K_UP] or pressed[pygame.K_w] or pressed[pygame.K_z]):
			arene.robot.avancer(arene.screen)
		if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
			arene.robot.tourner_droite()
		if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]):
			arene.robot.reculer(arene.screen)
		if (pressed[pygame.K_LEFT] or pressed[pygame.K_a] or pressed[pygame.K_q]):
			arene.robot.tourner_gauche()
		affichage(arene)
		clock.tick(60)
	pygame.quit()
