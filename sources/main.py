from modele.robot import Robot
from modele.arene import Arene
from threading import Thread
import sys
from view.affichage import Affichage
import time
import pygame
from modele.update_modele import update_mod
# from traducteur.state import Simulation
from controleur.control import Control, instruction_robot
from traducteur.state import Robot_IRL
# from API_robot.robot2I013 import Robot2IN013


if __name__ == "__main__":
	assert (len(sys.argv) >= 1 and len(sys.argv) <= 5), "\n\nobligatoire (2): vitesse_gauche ([int] 0-100) | vitesse_droite ([int] 0-100)\noptionnel   (3): l'angle de depart ([int] 0-359) | position x ([int]) | position y ([int])"
	if len(sys.argv) == 1:
		state=1
		arene = Arene(800, 800, Robot())
	if len(sys.argv) == 2:
		state=int(sys.argv[1])
		arene = Arene(800, 800, Robot())
	if len(sys.argv) == 3:
		state=int(sys.argv[1])
		arene = Arene(800, 800, Robot(int(sys.argv[2])))
	if len(sys.argv) == 4:
		state=int(sys.argv[1])
		arene = Arene(800, 800, Robot(int(sys.argv[2]), int(sys.argv[3])))
	elif len(sys.argv) == 5:
		state=int(sys.argv[1])
		arene = Arene(800, 800, Robot(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
		assert sys.argv[3].isdigit(), "La vitesse_rot doit etre un int."
	
	
	
	# Thread(target=update_mod,args=(arene,)).start()
	# # Thread(target=afficheur.start, args=(arene,)).start()
	# # afficheur.affiche(arene)
	# Thread(target=afficheur.affiche).start()
	# # afficheur.start()


	# if state==0:
	# 	tableau_strategies = instruction_robot(arene, Robot_IRL(Robot2IN013()))
	# 	controleur = Control(tableau_strategies)
	# 	controleur.start()

	if state==1:
		afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)), arene)
		tableau_strategies = instruction_robot(arene, arene.robot) # on va mettre les instructions du robot dans cette fonction pour charger les instruction a l'avance dans un tableaux
		controleur = Control(tableau_strategies)
		Thread(target = controleur.start).start()
		for event in pygame.event.get():
			pass
		Thread(target = update_mod, args = (arene,)).start()
		# Thread(target = afficheur.recuperer_touche).start()
		# Thread(target=self._st.affiche).start()
		afficheur.affiche()
