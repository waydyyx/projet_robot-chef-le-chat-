from multiprocessing import RLock
import math 
import time 


class Robot:
    def __init__(self, vitesse_g: int, vitesse_d: int, angle : int = 0, px : int = 50, py : int = 50):
        """
		:param vitesse_d: valeur compris entre (-10, 10) inclus pour choisir la vitesse_droite du robot
		:type vitesse: int
        :param vitesse_g: valeur compris entre (-10, 10) inclus pour choisir la vitesse_gauche du robot
		:type vitesse: int
		:param angle: valeur compris entre 0-359 inclus pour choisir l'angle du depart du robot
		:type angle: int
		:param px: position x du robot
		:type px: int
		:param py: position y du robot
		:type py: int 
		"""
        self.size = 50 # TAILLE ROBOT
        self.ray=10
        # self.L =  self.size # distance entre les rous
        # self.dt = 0.1 # pas de temps
        self.vitesse_d = 10 if (vitesse_d > 10) else -10 if (vitesse_d < -10) else vitesse_d # VITESSE_DROITE
        self.vitesse_g = 10 if (vitesse_g > 10) else -10 if (vitesse_g < -10) else vitesse_g # VITESSE GAUCHE
        # self.vitesse_rot = 6 # VITESSE ROTATION
        self.angle = math.radians(359) if (angle > 359) else 0 if (angle < 0) else angle # ANGLE EN DEGREE
        self.px = px  # position x
        self.py = py  # position y 
        self.dx = ((self.vitesse_d*self.ray / 60  + self.vitesse_g * self.ray / 60) / 2) * math.cos((self.vitesse_g * self.ray / 60 - self.vitesse_d*self.ray / 60) / self.size) # unite de deplacement en x
        self.dy = ((self.vitesse_d*self.ray / 60  + self.vitesse_g * self.ray / 60) / 2 )* math.sin((self.vitesse_g * self.ray / 60 - self.vitesse_d*self.ray / 60) / self.size) # unite de deplacement en y
        # self.vitesse = (self.vitesse_g+self.vitesse_d) / 2
        self.lock = RLock()

    def update_pos(self):
        v = (self.vitesse_d*self.ray / 60  + self.vitesse_g*self.ray / 60) / 2
        omega = (self.vitesse_g*self.ray / 60 - self.vitesse_d*self.ray / 60) / self.size

        # calcul déplacement
        self.dx = v * math.cos(self.angle + omega)
        self.dy = v * math.sin(self.angle + omega)

        # mise à jour position
        self.px += self.dx * 5
        self.py += self.dy * 5

        # mise à jour angle
        self.angle += omega 
        self.angle = self.angle % (2 * math.pi)
        return (self.px, self.py, self.angle)

    def change_vitesse(self, vitesse_g, vitesse_d):
        self.vitesse_g = vitesse_g
        self.vitesse_d = vitesse_d
        if (self.vitesse_g > 10):
            self.vitesse_g = 10
        elif (self.vitesse_g < -10):
            self.vitesse_g = -10
        if (self.vitesse_d > 10):
            self.vitesse_d = 10
        elif (self.vitesse_d < -10):
            self.vitesse_d = -10


    # def tourner_droite(self, angle: int):
    #     with self.lock: # arene.robot.lock
    #         self.change_vitesse(math.pi/2, -math.pi/2)
    #     for x in range(round((25 * angle) / 90)):
    #         time.sleep(1/60)
    #         self.avancer()

    # def strat_avancer(self, distance:int, vitesse:int):
    #     vd=self.vitesse_d
    #     vg=self.vitesse_g
    #     d=int(distance//(vitesse*self.ray/60))
    #     print(d)
    #     self.change_vitesse(vitesse,vitesse)
    #     for i in range (d):
    #         self.avancer()
    #         # time.sleep(1/60)
    #     self.change_vitesse(vd,vg)