# Irmuun Uyanga , 2230806   
# R. Vincent , instructor
# Advanced Programming , section 2
# Final Project

import pygame

class Button():
	'''Create a clickable button in a pygame application'''
	def __init__(self, x, y, image, scale):
		'''
		Initialize Button object.
		x (int): X-coordinate of the button.
        y (int): Y-coordinate of the button.
        image (pygame.Surface): Image of the button.
        scale (float): Scale factor to resize the image.
		'''
		width = image.get_width()
		height = image.get_height()
		scaled_width = int(width * scale)
		scaled_height = int(height * scale)
		self.image = pygame.transform.scale(image, (scaled_width,scaled_height))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		'''Draw the button on a surface. Returns
		Args:
            surface(pygame.Surface): The surface to draw the button on.
        Returns:
            bool: True if the button was clicked, False otherwise.
		'''
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check if mouse is over and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action