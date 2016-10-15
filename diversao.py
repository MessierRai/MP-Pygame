#-*- coding: latin1 -*-

import pygame, sys, os, random, math, time
from pygame.locals import *

pygame.init()

##### Cores ######
preto = (0, 0, 0)
vermelho = (255, 0, 0)
branco = (255,255,255)
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
	global x, y, corpo, direcao, x_modificado, y_modificado, incremento, decremento

	tela.blit(corpo, (x - raio_cobra, y - raio_cobra))

	if direcao == "direita":
		corpo = pygame.transform.rotate(cabeca, 0)
		x_modificado = incremento
		y_modificado = 0
	elif direcao == "esquerda":
		corpo = pygame.transform.rotate(cabeca, 180)
		x_modificado = decremento
		y_modificado = 0
	elif direcao == "cima":
		corpo = pygame.transform.rotate(cabeca, 90)
		y_modificado = decremento
		x_modificado = 0
	elif direcao == "baixo":
		corpo = pygame.transform.rotate(cabeca, 270)
		y_modificado = incremento
		x_modificado = 0

	for XnY in lista_cobra:
		tela.blit(corpito, (XnY[0] - raio_corpo, XnY[1] - raio_corpo))

	x += x_modificado
	y += y_modificado
################################

###### Comida da Cobra #########
raio_cCobra = 4
nova_comida = True
x2 = 0
y2 = 0
vel = 10
vell = 10

def comida():
	count = 0
	global x2, y2, comp, nova_comida, vel, vell
	if nova_comida:
		x2 = random.randint(47, 747)
		y2 = random.randint(56, 548)
		nova_comida = False
	tela.blit(comp, (x2 - raio_cCobra, y2 - raio_cCobra))

	x2 += vel
	y2 += vell

	if (x2 >= 751):
		vel = -2
	if(x2 <= 44):
		vel = 2
	if (y2 >= 553):
		vell = -2
	if (y2 <= 42):
		vell = 2


def comidaNormal():
	global x2, y2, comp, nova_comida
	if nova_comida:
		x2 = random.randint(47, 747)
		y2 = random.randint(56, 548)
		nova_comida = False
	tela.blit(comp, (x2 - raio_cCobra, y2 - raio_cCobra))

################################

########## InformaÃ§Ãµes de status #############
def status_de_jogo():
	global pontos, fonte
	p = fonte.render("Pontos: " + str(pontos), True, preto)
	tela.blit(p, (45,37))
	v = fonte.render("Vidas :" + str(vidas), True, preto)
	tela.blit(v, (45,61))
###############################

######## mensagen de tela ######
def mensagem_de_tela():
	mensagem_de_texto = fonte_fim.render("FIM DE JOGO.", True, branco)
	mensagem_de_texto2 = fonte_fim.render("Pressione C para jogar ou Q para sair.", True, branco)
	tela.blit(mensagem_de_texto, (315,200))
	tela.blit(mensagem_de_texto2, (160,250))
################################

######################################## Loop principal ###################################################
def loop_jogo():
	global x, y, x2, y2, vel, vell, vidas, pontos, distancia, corpo, nova_comida, lista_cobra, direcao, incremento, decremento

	incremento = 3
	decremento = -3

	direcao = "direita"

	x_modificado = 0
	y_modificado = 0
	comprimento_cobra = 1
	lista_cobra = []

	clock = pygame.time.Clock()

	sair_do_jogo = False
	fim_de_jogo = False

	while not sair_do_jogo:

		clock.tick(60)
		fps = clock.get_fps()
		pygame.display.set_caption("Snake ## FPS: %.2f" %fps)

		while fim_de_jogo == True:
			mensagem_de_tela()
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						sair_do_jogo = True
						fim_de_jogo = False
					if event.key == pygame.K_c:
						x = 400
						y = 300
						incremento = 3
						decremento = -3
						vel = 10
						vell = 10
						vidas = 3
						pontos = 0
						loop_jogo()

		#### Capturando todos os eventos durante a execuÃ§Ã£o ####
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT and direcao != "esquerda":
					direcao = "direita"

				elif event.key == pygame.K_LEFT and direcao != "direita":
					direcao = "esquerda"

				elif event.key == pygame.K_UP and direcao != "baixo":
					direcao = "cima"

				elif event.key == pygame.K_DOWN and direcao != "cima" :
					direcao = "baixo"

			if event.type == pygame.QUIT:
				sair_do_jogo = True

		####### posiÃ§Ã£o da cabeÃ§a da cobra ###########

		cabeca_cobra = []
		cabeca_cobra.append(x)
		cabeca_cobra.append(y)
		lista_cobra.append(cabeca_cobra)

		if len(lista_cobra) > comprimento_cobra:
			del lista_cobra[0]

		###############################################

		for todo_segmento in lista_cobra[:-1]:
			if todo_segmento == cabeca_cobra:
				fim_de_jogo = True

		tela.blit(gramado, (0, 0))
		tela.blit(paredes, (0, 0))

		if pontos > 15:
			comida()
		else:
			comidaNormal()
		cobrinha()
		status_de_jogo()

		########## Se bater nas paredes ##################
		if (x >= 751 or x <= 44) or (y >= 553 or y <= 42):
			vidas -= 1
			direcao = "direita"
			x = 400
			y = 300
		# if direcao == "direita" and ((x2 >= 751 or x2 <= 44) or (y2 >= 553 or y2 <= 42)):
			# x2 -=3

		##################################################

		if distancia(x, y, x2, y2) < (raio_cobra + raio_cCobra):
			nova_comida = True
			pontos += 1
			comprimento_cobra += 7
		############ Incremento de velocidade, tendo a ponuaÃ§Ã£o como base ############
		if pontos >= 8 and pontos < 16:
			incremento = 6
			decremento = -6
		elif pontos >= 16 and pontos < 24:
			incremento = 9
			decremento = -9
		elif pontos >= 24 and pontos < 32:
			incremento = 12
			decremento = -12
		elif pontos >= 32 and pontos < 40:
			incremento = 15
			decremento = -15
		elif pontos >= 40 and pontos < 50:
			incremento = 18
			decremento = -18
		elif pontos >= 50:
			incremento = 21
			decremento = -21
		##############################################################################

		if vidas == 0:
			fim_de_jogo = True

		pygame.display.flip()

	pygame.quit()

	quit()
###########################################################################################################

loop_jogo()
