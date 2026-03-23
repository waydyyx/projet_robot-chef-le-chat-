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