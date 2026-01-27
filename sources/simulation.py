import pygame
from class_robot import *
pygame.init()

length = 800 
width = 800

screen = pygame.display.set_mode((length, width))

img_car_original = pygame.image.load("../images/voiture.png").convert_alpha()
img__car_length, img__car_width = img_car_original.get_size()
print(f"length {img__car_length} width : {img__car_width}")

quit = 0

clock = pygame.time.Clock()
robot = Robot(0, 50, 50) # angle, coordonee de depart du robot (x,y)
while not(quit):	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit = 1
	pressed = pygame.key.get_pressed()
	if (pressed[pygame.K_ESCAPE]):
		quit = 1
	if (pressed[pygame.K_UP] or pressed[pygame.K_w]):
		if (robot.px <= length and robot.px >= 0 and robot.py < width and robot.py >= 0):
			robot.avancer()
		print(f"px :{robot.px} py :{robot.py}")
	if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
		robot.tourner_droite()
	if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]):
		robot.reculer()
	if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]):
		robot.tourner_gauche()

	
	screen.fill((0, 0, 0))
	img_car_rotation = pygame.transform.rotate(img_car_original, -math.degrees(robot.angle) - 90)
	# print(math.degrees(robot.angle))
	screen.blit(img_car_rotation, (robot.px, robot.py))
	pygame.display.flip()
	clock.tick(60)
pygame.quit()