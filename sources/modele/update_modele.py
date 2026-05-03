from modele.arene import Arene
import time
from modele.robot import UPDATE_TIME

def update_mod(arene:Arene):
    arene.robot.start=time.time()
    while True:
        if (arene.collision_bord() or arene.collision_obstacle()):
            with arene.stop_lock:
                arene.stop = 1
                return
        with arene.robot.lock:
            arene.robot.update_pos()
            arene.robot.dist=arene.detection_obstacle()
            #print(f"vit_g: {arene.robot.vitesse_g}, vit_d: {arene.robot.vitesse_d} px: {int(arene.robot.px)} py: {int(arene.robot.py)} obstacle: {arene.detection_obstacle()}")
        with arene.stop_lock:
            if arene.stop == 1:
                return