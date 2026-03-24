
from modele.arene import Arene
from strategie.rectangle import rectangle




def carre(arene: Arene,deplacement: int, vitesse: int):
    return rectangle(arene, deplacement, deplacement, vitesse)
    