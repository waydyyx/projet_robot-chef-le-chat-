from robot import Robot
from control import start
from arene import Arene
import sys
import pygame


if __name__ == "__main__":
	assert len(sys.argv) == 7, "Veuillez enter 6 arguments, vitesse_droite ([int] 0-100), vitesse_gauche ([int] 0-100), vitesse_rot ([int] 0-100), l'angle de depart ([int] 0-359), position x ([int]), position y ([int])"
	assert sys.argv[1].isdigit(), "La vitesse_droite doit etre un int."
	assert sys.argv[2].isdigit(), "La vitesse_gauche doit etre un int."
	assert sys.argv[3].isdigit(), "La vitesse_rot doit etre un int."
	assert sys.argv[4].isdigit(), "l'angle de depart doit etre un int."
	assert sys.argv[5].isdigit(), "La position x doit etre un int."
	assert sys.argv[6].isdigit(), "La position y doit etre un int."
	#simulation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))

	arene = Arene(800, 800, Robot(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])))
	start(arene)


