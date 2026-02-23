import math
from arene import detection_obstacle,collision_obstacle,collision_bord

class robot: 

    def __init__(self, vitesse_rg: int, vitesse_rd: int, angle: int, px : int = 0, py : int = 0):
        self.vitesse_rg=vitesse_rg
        self.vitesse_rd=vitesse_rd
        self.px = px
        self.py = py 

    def avancer(self):
        self.px += (self.vitesse_rg + self.vitesse_rd) / 2 * math.cos(self.angle)
        self.py += (self.vitesse_rg + self.vitesse_rd) / 2 * math.sin(self.angle)
        self.angle += (self.vitesse_rd - self.vitesse_rg) 
        self.angle = self.angle % (2 * math.pi)
        return (self.px, self.py, self.angle)

    def autonome(self, arene):
        """
        Avance le robot automatiquement jusqu'à ce qu'il rencontre un obstacle
        ou sorte de l'arène. Utilise la fonction 'avancer' pour gérer les roues.
        """
        liste_coordonnes = []
        while True:
            if arene.detection_obstacle() or arene.collision_obstacle() or arene.collision_bord():
                break
            liste_coordonnes.append(self.avancer())
        return liste_coordonnes

    def carre(self, longueur):
        """
        Fait avancer le robot en carré.
        :param longueur: nombre de pas ou distance à parcourir pour chaque côté
        """
        liste_coordonnes = []
        for _ in range(4):
            for _ in range(longueur):
                if arene and (arene.detection_obstacle() or arene.collision_obstacle() or arene.collision_bord()):
                    return liste_coordonnes
                liste_coordonnes.append(self.avancer())
            self.angle += math.pi / 2
            self.angle = self.angle % (2 * math.pi)
        return liste_coordonnes
    
#les fonction qui sont pas là a été supprimer , supoposé inutile selon le prof 