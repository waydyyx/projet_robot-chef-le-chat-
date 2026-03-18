from sources.modele.arene import Arene

import time


def autonome(arene, nb_collision):
    with arene.robot.lock:
        temp_g = arene.robot.vitesse_g
        temp_d = arene.robot.vitesse_d
        arene.robot.change_vitesse(4, 4)
    for x in range(nb_collision):
        while not(arene.detection_obstacle()):
            if arene.collision_obstacle() or arene.collision_bord():
                return
            with arene.robot.lock:
                time.sleep(1/60)
                arene.robot.avancer()
        with arene.robot.lock:
            arene.robot.tourner_droite(90) # on fait touner de 90 degre vers la droite lorsquon sort de la boucle de la non detection d'obstacle
            arene.robot.change_vitesse(4, 4) # on remet la vitesse des roues a 4,4 car on les as change lorsquon a voulu tourner de 90 degre vers la droiterobot.vitesse_g = temp_grobot.vitesse_d = temp_d
    