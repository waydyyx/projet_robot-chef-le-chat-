from multiprocessing import RLock
# from view.affichage import UPDATE_TIME

import math 
import time 
UPDATE_TIME = 60

class Robot:
    def __init__(self, angle : int = 0, px : int = 50, py : int = 50):
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
        self.ray = 30
        self.vitesse_d = 5 # VITESSE_DROITE
        self.vitesse_g = 5 # VITESSE GAUCHE
        self.angle = math.radians(359) if (angle > 359) else 0 if (angle < 0) else angle # ANGLE EN DEGREE
        self.px = px  # position x
        self.py = py  # position y 
        self.lock = RLock()
        self.rot_g=0
        self.rot_d=0
        self.dist=100
        self.start=time.time()
        self.end=0

    def update_pos(self):
        self.end=time.time()
        UPDATE_TIME=int(1/(self.end-self.start))
        v = (self.vitesse_d + self.vitesse_g)*self.ray / (UPDATE_TIME * 2)
        omega = (self.vitesse_g - self.vitesse_d) *self.ray / (UPDATE_TIME * self.size)

        # mise à jour position
        self.px += v * math.cos(self.angle + omega) 
        self.py += v * math.sin(self.angle + omega) 

        # mise à jour angle
        self.angle += omega 
        self.angle = self.angle % (2 * math.pi)

        #mise à jour des etat des roues
        self.rot_g+=self.vitesse_g/UPDATE_TIME
        self.rot_d+=self.vitesse_d/UPDATE_TIME

        self.start=time.time()
        
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

    def get_rot(self):
        return (self.rot_g,self.rot_d)
    
    def set_rot(self,offset,roues="both"):
        if roues=="L":
            self.rot_g=offset
        if roues=="R":
            self.rot_d=offset
        if roues=="both":
            self.rot_g=offset
            self.rot_d=offset

    def get_distance(self):
        return self.dist
    
    def detection(self):
        return self.dist<50
  