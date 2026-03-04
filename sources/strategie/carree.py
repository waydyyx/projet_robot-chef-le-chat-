
from sources.modele.arene import Arene
from sources.modele.robot import Robot
from sources.strategie.rectangle import rectangle




def carre(arene: Arene,deplacement: int, vitesse: int):
    return rectangle(arene, deplacement, deplacement, vitesse)
    