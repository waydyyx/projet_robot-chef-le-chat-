import pygame
from pygame import gfxdraw
from class_robot import *


def simulation(vitesse : int, vitesse_rotation : int, angle : int, px : int, py : int):
	pygame.init()

	length = 800 
	width = 800

	screen = pygame.display.set_mode((length, width))

	img_car_original = pygame.image.load("../images/robot_style.png").convert_alpha()
	img_car_length, img_car_height = img_car_original.get_size()
	# print(f"length {img_car_length} width : {img_car_height}")

	quit = 0

	clock = pygame.time.Clock()
	robot = Robot(vitesse, vitesse_rotation, angle, px, py) # angle, coordonee de depart du robot (x,y)
	while not(quit):	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = 1
		pressed = pygame.key.get_pressed()
		if (pressed[pygame.K_ESCAPE]):
			quit = 1
		if (pressed[pygame.K_UP] or pressed[pygame.K_w] or pressed[pygame.K_z]):
			robot.avancer()
		if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
			robot.tourner_droite()
		if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]):
			robot.reculer()
		if (pressed[pygame.K_LEFT] or pressed[pygame.K_a] or pressed[pygame.K_q]):
			robot.tourner_gauche()


		screen.fill((255, 255, 255))
		img_car_rotation = pygame.transform.rotate(img_car_original, -math.degrees(robot.angle) + 90)
		# print(math.degrees(robot.angle))
		rect=img_car_rotation.get_rect(center=((robot.px + img_car_length / 2),(robot.py + img_car_height / 2)))
		# print(rect)
		screen.blit(img_car_rotation, rect)
		gfxdraw.pixel(screen, int((robot.px + img_car_length / 2) + (img_car_length / 4) * math.cos(robot.angle)), int((robot.py + img_car_height / 2) + (img_car_height / 4) * math.sin(robot.angle)), (255, 0, 0))
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()
