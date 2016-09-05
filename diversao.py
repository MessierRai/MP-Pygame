#-*- coding: latin1 -*-

import pygame, sys, os, random, math, time
from pygame.locals import *
from pygame.time import *
from pygame.display import *

##### Cores ######
preto = (0, 0, 0)
branco = (255, 255, 255)
rosa = (255, 179, 255)
##################

###### Distancia #########
def distancia(x, y, x2, y2):
	distancia = math.sqrt(((x2 - x) ** 2) + ((y2 - y) ** 2))
	return distancia
##########################

##### Cobra ######
raio_cobra = 7.5
x = 400
y = 300
corpo = pygame.Surface((15, 15))
corpo.fill(branco)
def cobrinha():
	global x, y, corpo
	key = pygame.key.get_pressed()
	if key[pygame.K_RIGHT]:
		x += 3
	elif key[pygame.K_LEFT]:
		x -= 3
	elif key[pygame.K_UP]:
		y -= 3
	elif key[pygame.K_DOWN]:
		y += 3
	tela.blit(corpo, (x - raio_cobra, y - raio_cobra))
##################

###### Comida da Cobra ########
raio_cCobra = 4
nova_comida = True
x2 = 0
y2 = 0
comp = pygame.Surface((8, 8))
comp.fill(rosa)
def comida():
	global x2, y2, comp, nova_comida
	if nova_comida:
		x2 = random.randint(15, 785)
		y2 = random.randint(15, 585)
		nova_comida = False
	tela.blit(comp, (x2 - raio_cCobra, y2 - raio_cCobra))
###############################

dimensao = (800, 600)
tela = pygame.display.set_mode(dimensao)
tela.fill(preto)


counter = True
clock = pygame.time.Clock()

while counter:
	clock.tick(60)
	fps = clock.get_fps()
	pygame.display.set_caption("Shazam Caraí II ## FPS: %.2f" %fps)
	for event in pygame.event.get():
		if event.type == QUIT:
			counter = False
	
	comida()
	cobrinha()

	if distancia(x, y, x2, y2) < (raio_cobra + raio_cCobra):
		nova_comida = True


	pygame.display.flip()
sys.exit()
