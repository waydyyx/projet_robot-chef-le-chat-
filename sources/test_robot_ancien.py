from robot import Robot
import unittest
import math 

class test_robot(unittest.TestCase):
    def setUp(self):
        self.robot=Robot(5,5,0,100,100)

    def test_avancer(self):
        x=self.robot.px
        y=self.robot.py
        angle=self.robot.angle
        self.robot.avancer()
        self.assertAlmostEqual(self.robot.px,x+((self.robot.vitesse_d + self.robot.vitesse_g) / 2 * math.cos(angle + (self.robot.vitesse_g - self.robot.vitesse_d) / self.robot.L)))
        self.assertAlmostEqual(self.robot.py,y+((self.robot.vitesse_d + self.robot.vitesse_g) / 2 * math.sin(angle + (self.robot.vitesse_g - self.robot.vitesse_d) / self.robot.L)))
        self.assertAlmostEqual(self.robot.angle,(angle+(self.robot.vitesse_g - self.robot.vitesse_d) / self.robot.L)% (2 * math.pi))



    #def test_tourner_droite(self):
    #    self.robot.tourner_droite(90)
    #    angle_rechercher = math.pi/2

    def test_change_vitesse(self):
        self.robot.change_vitesse(5, -3)
        self.assertAlmostEqual(self.robot.vitesse_g, 5)
        self.assertAlmostEqual(self.robot.vitesse_d, -3)
        self.robot.change_vitesse(20, 15)
        self.assertAlmostEqual(self.robot.vitesse_g, 10)
        self.assertAlmostEqual(self.robot.vitesse_d, 10)
        self.robot.change_vitesse(-20, -15)
        self.assertAlmostEqual(self.robot.vitesse_g, -10)
        self.assertAlmostEqual(self.robot.vitesse_d, -10)
        self.robot.change_vitesse(20, -20)
        self.assertAlmostEqual(self.robot.vitesse_g, 10)
        self.assertAlmostEqual(self.robot.vitesse_d, -10)

        #le probleme de ce code c qu'il recalcule la même chose que la fonction avancer mais je le laisse là pour que vous le voyez 
        #j'ai changer juste assetEqual en assertAlmostEqual car on compare des float à virgule ;) genre ils ne sont jamais egale mais tjr à virgule près egale 
        


