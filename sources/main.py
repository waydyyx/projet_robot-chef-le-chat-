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


if __name__ == "__main__":
	assert (len(sys.argv) >= 3 and len(sys.argv) <= 6), "\n\nobligatoire (2): vitesse_gauche ([int] 0-100) | vitesse_droite ([int] 0-100)\noptionnel   (3): l'angle de depart ([int] 0-359) | position x ([int]) | position y ([int])"
	if sys.argv[1][0] == '-':
		assert sys.argv[1][1:].isdigit(), "La vitesse_gauche doit etre un int."	
	else:
		assert sys.argv[1].isdigit(), "La vitesse_gauche doit etre un int."
	if sys.argv[2][0] == '-':
		assert sys.argv[2][1:].isdigit(), "La vitesse_droite doit etre un int."
	else:
		assert sys.argv[2].isdigit(), "La vitesse_gauche doit etre un int."

	if len(sys.argv) == 3:
		arene = Arene(800, 800, Robot(int(sys.argv[1]), int(sys.argv[2])))
	elif len(sys.argv) == 4:
		arene = Arene(800, 800, Robot(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
		assert sys.argv[3].isdigit(), "La vitesse_rot doit etre un int."
	elif len(sys.argv) == 5:
		arene = Arene(800, 800, Robot(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))
		assert sys.argv[4].isdigit(), "La position x doit etre un int."
	elif len(sys.argv) == 6:
		arene = Arene(800, 800, Robot(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
		assert sys.argv[5].isdigit(), "La position y doit etre un int."
	
	
	afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)), arene)
	# Thread(target=update_mod,args=(arene,)).start()
	# # Thread(target=afficheur.start, args=(arene,)).start()
	# # afficheur.affiche(arene)
	# Thread(target=afficheur.affiche).start()
	# # afficheur.start()

	# state=1


	tableau_strategies = instruction_robot(arene, arene.robot) # on va mettre les instructions du robot dans cette fonction pour charger les instruction a l'avance dans un tableaux
	controleur = Control(tableau_strategies)
	controleur_irl = Robot_IRL(arene.robot)
	# control=Control(Test())
	Thread(target = controleur.start).start()
	# Thread(target=controleur.state.affiche).start()
	# state.start()

	# if state==1:
	for event in pygame.event.get():
		pass
	Thread(target = update_mod, args = (arene,)).start()
	Thread(target = afficheur.recuperer_touche).start()
	# Thread(target=self._st.affiche).start()
	afficheur.affiche()
