import pygame
from threading import Thread
from modele.update_modele import update_mod
# from API_robot.robot2I013 import Robot2IN013

# class Simulation:
#     def __init__(self, st):
#         self._st=st
    
#     def start(self):
#         for event in pygame.event.get():
#                 pass
#         Thread(target=update_mod,args=(self._st.arene,)).start()
#         # Thread(target=self._st.affiche).start()
#         self._st.affiche()
            

    # def __getattribute__(self, name):
    #     return getattr(self._st, name)$

SEUIL_DETECTION_MM = 300  # 30 cm

class Robot_IRL:
    def __init__(self,robot:"Robot2IN013"):
        self.robot=robot
        #self.robot.ray=33.25

    def start(self):
        print("yeaah")

    def change_vitesse(self,vit_g,vit_d):
        self.robot.set_motor_dps("MOTOR_LEFT", vit_g)
        self.robot.set_motor_dps("MOTOR_RIGHT", vit_d)

    #  def change_vitesse(self,vit_g,vit_d):
    #     self.robot.set_motor_dps(Robot2IN013.MOTOR_LEFT, vit_g)
    #     self.robot.set_motor_dps(Robot2IN013.MOTOR_RIGHT, vit_d)

    def stop(self):
        self.robot.stop()

    def get_rot(self):
        return self.robot.get_motor_position()
    
    def set_rot(self,offset,port):
        self.robot.offset_motor_encoder(port,offset)


    #def set_rot(self, offset, roues: str = "both"):
    #    if roues == "L" or roues == "both":
    #        current_g, _ = self.robot.get_motor_position()
    #       self.robot.offset_motor_encoder(Robot2IN013.MOTOR_LEFT, current_g - offset)
    #    if roues == "R" or roues == "both":
    #        _, current_d = self.robot.get_motor_position()
    #       self.robot.offset_motor_encoder(Robot2IN013.MOTOR_RIGHT, current_d - offset)


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
