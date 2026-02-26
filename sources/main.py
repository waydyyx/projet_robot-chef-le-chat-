from robot import Robot
from arene import Arene
from threading import Thread
import sys
import pygame
from affichage import Affichage, start
import time
import pygame

if __name__ == "__main__":
	assert (len(sys.argv) >= 3 and len(sys.argv) <= 6), "\n\nobligatoire (2): vitesse_gauche ([int] 0-100) | vitesse_droite ([int] 0-100)\noptionnel   (3): l'angle de depart ([int] 0-359) | position x ([int]) | position y ([int])"
	if sys.argv[1][0] == '-':
		assert sys.argv[1][1:].isdigit(), "La vitesse_gauche doit etre un int."	
	else :
		assert sys.argv[1].isdigit(), "La vitesse_gauche doit etre un int."
	if sys.argv[2][0] == '-':
		assert sys.argv[2][1:].isdigit(), "La vitesse_droite doit etre un int."
	else:
		assert sys.argv[2].isdigit(), "La vitesse_gauche doit etre un int."

	#simulation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
	arene = None
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
	
	Thread(target=start, args=(arene,)).start()
	afficheur = Affichage(pygame.display.set_mode((arene.larg, arene.haut)))
	afficheur.affiche(arene)
	# start(arene)




