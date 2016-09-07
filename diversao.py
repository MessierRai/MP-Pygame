#-*- coding: latin1 -*-

import pygame, sys, os, random, math, time
from pygame.locals import *
from pygame.time import *
from pygame.display import *

pygame.init()

##### Cores ######
preto = (0, 0, 0)
branco = (255, 255, 255)
rosa = (255, 179, 255)
##################

dimensao = (800, 600)
tela = pygame.display.set_mode(dimensao)
tela.fill(preto)

######### Objetos ###########
gramado = pygame.image.load(os.path.join("images", "fundocobrinha.jpg"))
paredes = pygame.image.load(os.path.join("images", "paredes.png"))
comp = pygame.image.load(os.path.join("images", "comidacobra.png"))
comp = pygame.transform.scale(comp, (18, 20))
cabeca = pygame.image.load(os.path.join("images", "cabecadacobra.png"))
corpito = pygame.image.load(os.path.join("images", "corpodacobra.png"))
corpo = pygame.transform.rotate(cabeca, 0)
caminhodafonte = os.path.join("fonte", "lunchds.ttf")
fonte = pygame.font.Font(caminhodafonte, 22)
fontefim = pygame.font.Font(caminhodafonte, 50)
#############################

###### Distancia #########
def distancia(x, y, x2, y2):
	distancia = math.sqrt(((x2 - x) ** 2) + ((y2 - y) ** 2))
	return distancia
##########################

########### cobra #############
pontos = 0
vidas = 3
raio_cobra = 12
x = 400
y = 300

def cobrinha():
	global x, y, corpo
	tela.blit(corpo, (x - raio_cobra, y - raio_cobra))
################################

###### Comida da Cobra #########
raio_cCobra = 4
nova_comida = True
x2 = 0
y2 = 0
def comida():
	global x2, y2, comp, nova_comida
	if nova_comida:
		x2 = random.randint(47, 747)
		y2 = random.randint(56, 548)
		nova_comida = False
	tela.blit(comp, (x2 - raio_cCobra, y2 - raio_cCobra))
################################

########## Textos #############
def porCima():
	global pontos, fonte
	p = fonte.render("Pontos: " + str(pontos), True, preto)
	tela.blit(p, (45,37))
	v = fonte.render("Vidas :" + str(vidas), True, preto)
	tela.blit(v, (45,61))
###############################

counter = True
clock = pygame.time.Clock()

x_modificado = 0
y_modificado = 0

########################### Loop principal do jogo ##################################
def loop_jogo():
	global x, y, x2, x2, x_modificado, y_modificado, vidas, pontos, distancia, corpo, raio_cCobra, raio_cobra, counter, nova_comida, clock

	while counter:
		clock.tick(60)
		fps = clock.get_fps()
		pygame.display.set_caption("Shazam Caraí II ## FPS: %.2f" %fps)

		#### Capiturando todos os eventos durante a execução ####
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					corpo = pygame.transform.rotate(cabeca, 0)
					x_modificado = 3
					y_modificado = 0
				elif event.key == pygame.K_LEFT:
					corpo = pygame.transform.rotate(cabeca, 180)
					x_modificado = -3
					y_modificado = 0
				elif event.key == pygame.K_UP:
					corpo = pygame.transform.rotate(cabeca, 90)
					y_modificado = - 3
					x_modificado = 0
				elif event.key == pygame.K_DOWN:
					corpo = pygame.transform.rotate(cabeca, 270)
					y_modificado = 3
					x_modificado = 0
		
			if event.type == QUIT:
				counter = False

		x += x_modificado
		y += y_modificado
	
		tela.blit(gramado, (0, 0))
		tela.blit(paredes, (0, 0))
		comida()
		cobrinha()
		porCima()

		########## Se bater nas paredes ##################
		if (x >= 751 or x <= 44) or (y >= 553 or y <= 42):
			vidas -= 1
			x = 400
			y = 300
		##################################################

		if distancia(x, y, x2, y2) < (raio_cobra + raio_cCobra):
			nova_comida = True
			pontos += 1

		if vidas == 0:
			go = fontefim.render("Game Over!", True, preto)
			tela.blit(go, (270, 250))
			counter = False

		pygame.display.flip()
###########################################################################################################

loop_jogo()

if vidas < 1:
	time.sleep(3)
sys.exit()
