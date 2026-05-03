import pygame
from threading import Thread
from modele.update_modele import update_mod
# from API_robot.robot2I013 import Robot2IN013

class Robot_IRL:
    def __init__(self, robot):
        self.robot=robot
        #self.robot.ray=33.25

    def change_vitesse(self,vit_g,vit_d):
        self.robot.set_motor_dps("MOTOR_LEFT", vit_g)
        self.robot.set_motor_dps("MOTOR_RIGHT", vit_d)

    def stop(self):
        self.robot.stop()

    def get_rot(self):
        return self.robot.get_motor_position()
    
    def set_rot(self,offset,port):
        self.robot.offset_motor_encoder(port,offset)

    def get_distance(self):
        return self.robot.get_distance()
    
    def get_distance(self):
        return self.robot.get_distance()
    
    def detection(self) -> bool:
        """
       Renvoie True si un obstacle est détecté à moins de SEUIL_DETECTION_MM.
       Même rôle que robot.detection() dans la simulation.
       """
        dist = self.get_distance()
        # 8190 c'est la valeur qui veut dire que le capteur ne detecte rien jcrois
        if dist >= 8190:
            return False
        return dist < SEUIL_DETECTION_MM
