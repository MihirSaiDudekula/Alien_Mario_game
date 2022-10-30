import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((,))
pygame.display.set_caption()
clock = pygame.time.Clock()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	screen.blit()
	pygame.display.update()
	clock.tick(60)