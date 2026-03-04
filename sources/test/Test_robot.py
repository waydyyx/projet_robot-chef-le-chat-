import unittest
from sources.modele.robot import Robot
import math

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot(5, 5, 0, 100, 100)

    def test_change_vitesse(self):
        self.robot.change_vitesse(20, -20)
        self.assertEqual(self.robot.vitesse_g, 10)
        self.assertEqual(self.robot.vitesse_d, -10)

    def test_avancer(self):
        x = self.robot.px
        self.robot.avancer()
        self.assertNotEqual(self.robot.px, x)

if __name__ == "__main__":
    unittest.main()
    
 #commande pour tester : python -m unittest discover test -v
