from modele.arene import Arene
import time
from modele.robot import UPDATE_TIME

def update_mod(arene:Arene):
    while True:
        for robot in arene.robot:
            if (arene.collision_bord(robot) or arene.collision_obstacle(robot)):
                with arene.stop_lock:
                    arene.stop = 1
                    return
            with robot.lock:
                robot.update_pos()
                robot.dist=arene.detection_obstacle(robot)
                #print(f"vit_g: {arene.robot.vitesse_g}, vit_d: {arene.robot.vitesse_d} px: {int(arene.robot.px)} py: {int(arene.robot.py)} obstacle: {arene.detection_obstacle()}")
            with arene.stop_lock:
                if arene.stop == 1:
                    return
        time.sleep(1 / UPDATE_TIME)