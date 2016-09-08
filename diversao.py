#-*- coding: latin1 -*-

import pygame, sys, os, random, math, time
from pygame.locals import *

pygame.init()

##### Cores ######
preto = (0, 0, 0)
vermelho = (255, 0, 0)
##################

##################

dimensao = [800, 600]
tela = pygame.display.set_mode(dimensao)

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
fonte_fim = pygame.font.Font(caminhodafonte, 25)

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
raio_corpo = 12
x = 400
y = 300

def cobrinha(): 
	global x, y, corpo
	tela.blit(corpo, (x - raio_cobra, y - raio_cobra))
	for XnY in lista_cobra:
		tela.blit(corpito, (XnY[0] - raio_corpo, XnY[1] - raio_corpo))
		
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

########## Informações de status #############

def status_de_jogo():
	global pontos, fonte
	p = fonte.render("Pontos: " + str(pontos), True, preto)
	tela.blit(p, (45,37))
	v = fonte.render("Vidas :" + str(vidas), True, preto)
	tela.blit(v, (45,61))

###############################

######## mensagen de tela ######

def mensagem_de_tela():
	mensagem_de_texto = fonte_fim.render("Fim de Jogo, pressione C para jogar ou Q para sair.", True, vermelho)
	tela.blit(mensagem_de_texto,[55,200])

################################

######################################## Loop principal ###################################################

def loop_jogo():
	global x, y, x2, x2, vidas, pontos, distancia, corpo, raio_cCobra, raio_cobra, counter, nova_comida, lista_cobra
	
	x_modificado = 0
	y_modificado = 0
	
	comprimento_cobra = 1
	lista_cobra = []

	clock = pygame.time.Clock()

	sair_do_jogo = False
	fim_de_jogo = False

	while not sair_do_jogo:
		
		while fim_de_jogo == True:
		    mensagem_de_tela()
		    pygame.display.update()
		    for event in pygame.event.get():
		        if event.type == pygame.KEYDOWN:
		            if event.key == pygame.K_q:
		                sair_do_jogo = True
		                fim_de_jogo = False
		            if event.key == pygame.K_c:
		                loop_jogo()

		#### Capturando todos os eventos durante a execução ####
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
				sair_do_jogo = True

		x += x_modificado
		y += y_modificado
		
		####### posição da cabeça da cobra ###########

		cabeca_cobra = []
		cabeca_cobra.append(x)
		cabeca_cobra.append(y)
		lista_cobra.append(cabeca_cobra)

		if len(lista_cobra) > comprimento_cobra:
            		del lista_cobra[0]

		###############################################

		for todo_seguimento in lista_cobra[:-1]:
			if todo_seguimento == cabeca_cobra:
                		fim_de_jogo = True
		
		

		tela.blit(gramado, (0, 0))
		tela.blit(paredes, (0, 0))

		comida()
		cobrinha()
		status_de_jogo()
		
		pygame.display.update()

		clock.tick(60)

		fps = clock.get_fps()

		pygame.display.set_caption("Shazam Caraí II ## FPS: %.2f" %fps)

		########## Se bater nas paredes ##################
		if (x >= 751 or x <= 44) or (y >= 553 or y <= 42):

			vidas -= 1
			x = 400
			y = 300

		##################################################

		if distancia(x, y, x2, y2) < (raio_cobra + raio_cCobra):

			nova_comida = True
			pontos += 1
			comprimento_cobra += 1

		if vidas == 0:

			fim_de_jogo = True
			mensagem_de_tela()

###########################################################################################################

loop_jogo()
