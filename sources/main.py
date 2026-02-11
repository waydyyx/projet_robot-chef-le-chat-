from robot import *
from control import *
import sys
if __name__ == "__main__":
	assert len(sys.argv) == 6, "Veuillez enter 5 arguments, vitesse ([int] 0-10), vitesse_rotation ([int] 0-10), l'angle ([int] 0-359), position x ([int]), position y ([int])"
	assert sys.argv[1].isdigit(), "La vitesse doit etre un int."
	assert sys.argv[2].isdigit(), "La vitesse_rotation doit etre un int."
	assert sys.argv[3].isdigit(), "l'angle doit etre un int."
	assert sys.argv[4].isdigit(), "La position x doit etre un int."
	assert sys.argv[5].isdigit(), "La position y doit etre un int."
	#simulation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))

	arene = Arene(800, 800, Robot(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
	start(arene)


