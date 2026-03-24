from modele.robot import Robot

class AvancerDroit:
    def __init__(self,robot:Robot,distance,vitesse):
        self.distance=distance
        self.vitesse=vitesse
        self.robot=robot
        self.parcouru=0

    def start(self):
        self.parcouru=0

    def step(self):
        self.parcouru+=self.vitesse*self.robot.ray/60
        if self.stop():return
        self.robot.change_vitesse(self.vitesse,self.vitesse)
        self.robot.update_pos()
    
    def stop(self):
        return self.parcouru>self.distance
    
class Tourner:
    def __init__(self,robot:Robot,angle,vitesse):
        self.angle=angle
        if self.angle<0:
            self.vit_g=vitesse*(-1)
            self.vit_d=vitesse
        else:
            self.vit_g=vitesse
            self.vit_d=vitesse*(-1)
        self.robot=robot
        self.parcouru=0

    def start(self):
        self.parcouru=0

    def step(self):
        self.parcouru+=(self.vit_g*self.robot.ray/60 - self.vit_d*self.robot.ray/60) / self.robot.size
        # if self.stop():return
        self.robot.change_vitesse(self.vit_g,self.vit_d)
        # self.robot.update_pos()

    def stop(self):
        return abs(self.parcouru)>abs(self.angle)