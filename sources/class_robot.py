import math 

class Robot:
	def __init__(self,  angle : float, px : int = 0, py : int = 0):
		self.px = px  # position x
		self.py = py  # position y 
		self.angle = angle
		self.dx = math.cos(angle) * 5  # direction x (vecteur x ?)
		self.dy = math.sin(angle) * 5  # direction y (vecteur y ?)
	
	def avancer(self):
		self.px += self.dx
		self.py += self.dy
	
	def tourner_droite(self):
		self.angle += math.pi / 48
		if (self.angle > 2 * math.pi):
			self.angle -= 2 * math.pi
		self.dx = math.cos(self.angle) * 5
		self.dy = math.sin(self.angle) * 5
	
	def reculer(self):
		self.px -= self.dx
		self.py -= self.dy
	
	def tourner_gauche(self):
		self.angle -= math.pi / 48
		if (self.angle < 0):
			self.angle += 2 * math.pi
		self.dx = math.cos(self.angle) * 5
		self.dy = math.sin(self.angle) * 5