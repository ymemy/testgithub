import pygame

class Button():
	'''Create a clickable button in a pygame application'''
	def __init__(self, x, y, text):
		'''
		Initialize Button object.
		x (int): X-coordinate of the button.
        y (int): Y-coordinate of the button.
        image (pygame.Surface): Image of the button.
        scale (float): Scale factor to resize the image.
		'''
		self.x = x
		self.y = y
		self.text = text
		self.width = 200
		self.height = 50
		self.color = (0, 128, 255)
		self.hover_color = (0, 200, 255)
		self.font = pygame.font.Font(None, 48)
		self.rect = pygame.Rect(x, y, self.width, self.height)
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
			pygame.draw.rect(surface, self.hover_color, self.rect)
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		
		else:
			pygame.draw.rect(surface, self.color, self.rect)

		text_surface = self.font.render(self.text, True, (255, 255, 255))
		text_rect = text_surface.get_rect(center=self.rect.center)
		surface.blit(text_surface, text_rect) 

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action