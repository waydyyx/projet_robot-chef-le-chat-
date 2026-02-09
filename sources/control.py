from affichage import *

def est_dehors_avancer(robot : Robot, screen):
	length, height = screen.get_size()
	if (robot.px + robot.dx < 0 or robot.px + robot.dx > length - robot.size or robot.py + robot.dy < 0 or robot.py + robot.dy > height - robot.size):
		return (1)
	return (0)
	
def est_dehors_reculer(robot : Robot, screen):
	length, height = screen.get_size()
	if (robot.px - robot.dx < 0 or robot.px - robot.dx > length - robot.size or robot.py - robot.dy < 0 or robot.py - robot.dy > height - robot.size):
		return (1)
	return (0)

def start(arene:Arene):
	pygame.init()
	quit = 0
	afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)))
	clock = pygame.time.Clock()
	while not(quit):	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = 1
		pressed = pygame.key.get_pressed()
		if (pressed[pygame.K_ESCAPE]):
			quit = 1
		if ((pressed[pygame.K_UP] or pressed[pygame.K_w] or pressed[pygame.K_z]) and not(est_dehors_avancer(arene.robot, afficheur.screen))):
			arene.robot.avancer()
		if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
			arene.robot.tourner_droite()
		if (pressed[pygame.K_DOWN] or pressed[pygame.K_s] and not(est_dehors_reculer(arene.robot, afficheur.screen))):
			arene.robot.reculer()
		if (pressed[pygame.K_LEFT] or pressed[pygame.K_a] or pressed[pygame.K_q]):
			arene.robot.tourner_gauche()
		afficheur.affiche(arene)
		clock.tick(60)
	pygame.quit()
