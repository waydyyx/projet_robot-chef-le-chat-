from sources.modele.arene import Arene
from sources.strategie.carree import carre
from sources.strategie.rectangle import rectangle
from sources.strategie.autonome import autonome



def traiter_touche(arene: Arene, cle: str):
    if cle == "z":
        with arene.robot.lock:
            arene.robot.avancer()
    elif cle == "ESC" or cle == "QUIT":
        with arene.stop_lock:
            arene.stop = 1
    # changement directe de la vitesse des roues 
    elif cle  == "e":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d + 1)
    elif cle == "d":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g,  arene.robot.vitesse_d - 1)        
    elif cle == "a":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g + 1,  arene.robot.vitesse_d)
    elif cle =="q":
        with arene.robot.lock:
            arene.robot.change_vitesse(arene.robot.vitesse_g - 1,  arene.robot.vitesse_d) 

    # strategie
    elif cle =="c":
        carre(arene, 35, 10)
    elif cle == "r":
        rectangle(arene, 70, 35, 10)
    elif cle == "p":
        autonome(arene, 2)
    elif cle =="k":
        arene.robot.strat_avancer(25)

    # preset sur les fleches directionnelles
    elif cle =="UP":
        with arene.robot.lock:
            arene.robot.change_vitesse(4, 4)
    elif cle == "RIGHT":
        with arene.robot.lock:
            arene.robot.change_vitesse(2, -2)
    elif cle == "DOWN":
        with arene.robot.lock:
            arene.robot.change_vitesse(-4, -4)
    elif cle == "LEFT":
        with arene.robot.lock:
            arene.robot.change_vitesse(-2, 2)