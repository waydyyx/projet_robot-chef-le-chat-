import pygame
from threading import Thread
from modele.update_modele import update_mod
from API_robot.robot2I013 import Robot2IN013

class Simulation:
    def __init__(self, st):
        self._st=st
    
    def start(self):
        for event in pygame.event.get():
                pass
        Thread(target=update_mod,args=(self._st.arene,)).start()
        # Thread(target=self._st.affiche).start()
        self._st.affiche()
            

    # def __getattribute__(self, name):
    #     return getattr(self._st, name)$


class Robot_IRL:
    def __init__(self,robot:Robot2IN013):
        self.robot=robot

    def start(self):
        print("yeaah")

    def change_vitesse(self,vit_g,vit_d):
        self.robot.set_motor_dps(self, "MOTOR_LEFT", vit_g)
        self.robot.set_motor_dps(self, "MOTOR_RIGHT", vit_d)

    def stop(self):
        self.robot.stop()

    def get_rot(self):
        return self.robot.get_motor_position()
    
    def set_rot(self,offset,port):
        self.robot.offset_motor_encoder(port,offset)

    def get_distance(self):
        return self.robot.get_distance()
