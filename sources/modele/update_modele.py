from modele.arene import Arene
import time

def update_mod(arene:Arene):
    while True:
        if (arene.collision_bord() or arene.collision_obstacle()):
            with arene.stop_lock:
                arene.stop = 1
                return
        with arene.stop_lock:
            if arene.stop==1:
                return
        with arene.robot.lock:
            arene.robot.update_pos()
        time.sleep(1/60)