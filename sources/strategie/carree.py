
from sources.modele.arene import Arene
from sources.strategie.rectangle import rectangle




def carre(arene: Arene,deplacement: int, vitesse: int):
    return rectangle(arene, deplacement, deplacement, vitesse)
    