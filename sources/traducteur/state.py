import pygame
from threading import Thread
from modele.update_modele import update_mod
class Simulation:
    def __init__(self, st):
        self._st=st
    
    def start(self):
        for event in pygame.event.get():
                pass
        Thread(target=update_mod,args=(self._st.arene,)).start()
        Thread(target=self._st.affiche).start()
        
            

    # def __getattribute__(self, name):
    #     return getattr(self._st, name)$

class Robot_IRL:
    def __init__(self):
        pass

    def start(self):
        print("yeaah")