import math 
from pygame import gfxdraw
import pygame
import math 

class Robot:
	def __init__(self, vitesse : int, vitesse_rotation : int, angle : int, px : int = 0, py : int = 0):
		# VITESSE 
		if (vitesse > 10):
			self.vitesse = 10
		elif (vitesse < 0):
			self.vitesse = 0
		else:
			self.vitesse = vitesse

		# VITESSE_ROTATION
		if (vitesse_rotation > 10):
			self.vitesse_rotation = 10
		elif (vitesse_rotation < 0):
			self.vitesse_rotation = 0
		else:
			self.vitesse_rotation = vitesse_rotation

		# ANGLE
		if (angle > 359):
			self.angle = math.radians(359)
		elif (angle < 0):
			self.angle = 0
		else:		
			self.angle = math.radians(angle)

		self.px = px  # position x
		self.py = py  # position y 
		self.dx = math.cos(self.angle) * self.vitesse  # direction x (vecteur x ?)
		self.dy = math.sin(self.angle) * self.vitesse  # direction y (vecteur y ?)
		self.size = 50

	def avancer(self):
		"""avancer le robot
		"""
		self.px += self.dx
		self.py += self.dy
	
		
	def reculer(self):
		"""reculer le robot
		"""
		self.px -= self.dx
		self.py -= self.dy


	def tourner_droite(self):
		"""tourner le robot a droite
		"""
		self.angle += (math.pi / (110 - self.vitesse_rotation * 10)) 
		self.angle = self.angle % (2 * math.pi)
		self.dx = math.cos(self.angle) * self.vitesse
		self.dy = math.sin(self.angle) * self.vitesse

	
	def tourner_gauche(self):
		"""tourner le robot a gauche
		""" 
		self.angle -= (math.pi / (110 - self.vitesse_rotation * 10))
		self.angle = self.angle % (2 * math.pi)
		self.dx = math.cos(self.angle) * self.vitesse
		self.dy = math.sin(self.angle) * self.vitesse

class Robot:
	def __init__(self, vitesse : int, vitesse_rotation : int, angle : int, px : int = 0, py : int = 0):
		# VITESSE 
		if (vitesse > 10):
			self.vitesse = 10
		elif (vitesse < 0):
			self.vitesse = 0
		else:
			self.vitesse = vitesse

		# VITESSE_ROTATION
		if (vitesse_rotation > 10):
			self.vitesse_rotation = 10
		elif (vitesse_rotation < 0):
			self.vitesse_rotation = 0
		else:
			self.vitesse_rotation = vitesse_rotation

		# ANGLE
		if (angle > 359):
			self.angle = math.radians(359)
		elif (angle < 0):
			self.angle = 0
		else:		
			self.angle = math.radians(angle)

		self.px = px  # position x
		self.py = py  # position y 
		self.dx = math.cos(self.angle) * self.vitesse  # direction x (vecteur x ?)
		self.dy = math.sin(self.angle) * self.vitesse  # direction y (vecteur y ?)
		self.size = 50

	def avancer(self):
		self.px += self.dx
		self.py += self.dy
		return ((self.px, self.py))
	
	def tourner_droite(self):
		self.angle += (math.pi / (110 - self.vitesse_rotation * 10)) 
		self.angle = self.angle % (2 * math.pi)
		self.dx = math.cos(self.angle) * self.vitesse
		self.dy = math.sin(self.angle) * self.vitesse
	
	def reculer(self):
		self.px -= self.dx
		self.py -= self.dy
		return ((self.px, self.py))
		
	
	def tourner_gauche(self):
		self.angle -= (math.pi / (110 - self.vitesse_rotation * 10))
		self.angle = self.angle % (2 * math.pi)
		self.dx = math.cos(self.angle) * self.vitesse
		self.dy = math.sin(self.angle) * self.vitesse



