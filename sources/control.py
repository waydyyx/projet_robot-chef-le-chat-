from affichage import *

def start(arene:Arene):
	pygame.init()
	quit = 0
	afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)))
	clock = pygame.time.Clock()
	# print(arene.collision_point(90,90))

	autonome = None
	while not(quit):	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = 1
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					liste = arene.robot.carre(25)
					# print(liste)
					afficheur.affiche_trajet(arene, liste)

				elif event.key == pygame.K_r:
					liste = arene.robot.rectangle(40,20)
					afficheur.affiche_trajet(arene , liste)

				elif event.key == pygame.K_p:
					for x in range(15):
						liste= arene.robot.autonome(arene)
						afficheur.affiche_trajet(arene, liste)

		pressed = pygame.key.get_pressed()
		if (pressed[pygame.K_ESCAPE]):
			quit = 1
		if ((pressed[pygame.K_UP] or pressed[pygame.K_w] or pressed[pygame.K_z]) and not(arene.est_dehors_avancer() or arene.collision_obstacle_avancer())):
			arene.robot.avancer()
		if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]):
			arene.robot.tourner_droite()
		if ((pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and not(arene.est_dehors_reculer() or arene.collision_obstacle_reculer())):
			arene.robot.reculer()
		if (pressed[pygame.K_LEFT] or pressed[pygame.K_a] or pressed[pygame.K_q]):
			arene.robot.tourner_gauche()

		# if ( pressed[pygame.K_c]):
		# 	arene.robot.carre(10)
		# 	# arene.robot.tourner_droite(90)
			# print("c")



		afficheur.affiche(arene)
		clock.tick(200)
	pygame.quit()