import pygame
import sys
import random
import math

pygame.init()

#Constantes
ALTURA = 480
LARGURA = 640
NOME_JOGO = "Grandma's Secrets" #nome do jogo
ICONE = pygame.image.load("assets\Veia_Enferma\Veia.png") #imagem do icone

#cores
MARROM_CLARO = (255,222,173)
BRANCO = (255,255,255)

RELOGIO = pygame.time.Clock() #frames

FUNDO = pygame.image.load("assets\GS_Background.png") #imagem de fundo
FUNDO = pygame.transform.scale(FUNDO, (LARGURA, ALTURA)) #dimensões da imagem de fundo
START_IMAGEM = pygame.image.load("assets\_start.png")
RESTART_IMAGEM = pygame.image.load("assets\_restart.png")
SAIR_IMAGEM = pygame.image.load("assets\_sair.png")
CREDITOS_IMAGEM = pygame.image.load("assets\_creditos.png")
CONTINUAR_IMAGEM = pygame.image.load("assets\_continuar.png")
VOLTAR_IMAGEM = pygame.image.load("assets\_voltar.png")

START_IMAGEM2 = pygame.image.load("assets\_start2.png")
RESTART_IMAGEM2 = pygame.image.load("assets\_restart2.png")
SAIR_IMAGEM2 = pygame.image.load("assets\_sair2.png")
CREDITOS_IMAGEM2 = pygame.image.load("assets\_creditos2.png")
CONTINUAR_IMAGEM2 = pygame.image.load("assets\_continuar2.png")
VOLTAR_IMAGEM2 = pygame.image.load("assets\_volta2.png")

FONTE = pygame.font.SysFont("arial", 20, True, False) #fonte da letra utilizada
FONTE_GAME_OVER = pygame.font.SysFont("arial", 100, True, False) #fonte da tela maior para game over e pause
FONTE_START = pygame.font.SysFont("arial", 55, True, False)
FONTE_CREDITOS = pygame.font.SysFont("arial", 14, True, False)
#Musica e som:
MUSICA = pygame.mixer.Sound("som\_start_song.wav") #musica de fundo
EFEITO_COLISAO = pygame.mixer.Sound("som\_attack1.wav")
EFEITO_COLISAO2 = pygame.mixer.Sound("som\_attack2.wav")
EFEITO_COLISAO3 = pygame.mixer.Sound("som\_attack3.wav")
MORTE_JOGADOR = pygame.mixer.Sound("som\damaged1.wav")
MORTE_JOGADOR2 = pygame.mixer.Sound("som\damaged2.wav")
MORTE_JOGADOR3 = pygame.mixer.Sound("som\damaged3.wav")
MUSICA_PM = pygame.mixer.Sound("som\_start_song.wav")
MUSICA_GO = pygame.mixer.Sound("som\_gameover_sound.wav")
MUSICA_QUADRINHOS = pygame.mixer.Sound("som\quadrinhos.wav")
MUSICA_BOSS = pygame.mixer.Sound("som\_boss_song.wav")
TELA_START = pygame.image.load("assets\_start_.png")
TELA_START = pygame.transform.scale(TELA_START, (LARGURA, ALTURA))
TELA_GAMEOVER = pygame.image.load("assets\_gameover_.jpeg")
TELA_GAMEOVER = pygame.transform.scale(TELA_GAMEOVER, (LARGURA + 65, ALTURA))
CAST = pygame.mixer.Sound("som\_cast.wav")

MOVIMENTO_MICE = pygame.mixer.Sound("som\_mouse-2.wav")
MOVIMENTO_SLIME = pygame.mixer.Sound("som\movimento_gosma.wav")
MOVIMENTO_MONSTRO = pygame.mixer.Sound("som\skeleton_walk.wav")

VOVO_AUDIO = pygame.mixer.Sound("som\_vovo.wav")

#jogador
class PLAYER(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.sprites = []
        self.hp = 10
        self.hp_texto = f'VIDA: {self.hp}'
        self.hp_formatado = FONTE.render(self.hp_texto, True, (255,0,0))
        janela.blit(self.hp_formatado, (40,0))
        
        self.colidiu = 0

        #sprites
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Lado_0000.png")) #1
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Lado_0001.png")) #2
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Lado_0002.png")) #3
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Lado_0003.png")) #4
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Baixo_0000.png")) #5
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Baixo_0001.png")) #6
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Baixo_0002.png")) #7
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Baixo_0003.png")) #8
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Cima_0000.png")) #9
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Cima_0001.png")) #10
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Cima_0002.png")) #11
        self.sprites.append(pygame.image.load("assets\Guri\Guri_Cima_0003.png")) #12

        #Dimensionamento
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        

        #Atributo para pausa da animação
        self.andar = False
        self.andar1 = False
        self.andar_baixo = False
        self.andar_cima = False

    def andar(self): #Play Animação
        self.andar = True
        self.andar1 = True
        self.andar_cima = True
        self.andar_baixo = True

    
    def update(self): #Codigo para animação da movimentação do jogador
        if self.andar == True:
            self.atual += 0.25
            if self.atual >= 4:
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        elif self.andar1 == True:
            self.atual += 0.25
            if self.atual >= 4:
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.flip(self.sprites[int(self.atual)], True, False)
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        elif self.andar_baixo == True:
            self.atual += 0.25
            if self.atual >= 8 or self.atual <= 3.99:
                self.atual = 4
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        elif self.andar_cima == True:
            self.atual += 0.25
            if self.atual >= 12 or self.atual <= 7.99:
                self.atual = 8
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        else:
            self.image = self.sprites[4]
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))

        for e in slime:
            if pygame.sprite.spritecollide(self, enemy, False):
                self.colidiu += 1
                if self.colidiu == 1:
                    efeito = random.randint(1,3)
                    if efeito == 1:
                        MORTE_JOGADOR.play()
                    elif efeito == 2:
                        MORTE_JOGADOR2.play()
                    elif efeito == 3:
                        MORTE_JOGADOR3.play()
                    self.hp -= e.dano
                elif self.colidiu == 60:
                    self.colidiu = 0
            else:
                self.colidiu = 0
        
        self.andar = False
        self.andar1 = False
        self.andar_baixo = False
        self.andar_cima = False

    
    def main(self): #Movimentação do jogador
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        
        #self.player = pygame.draw.rect(janela, (BRANCO), (self.x, self.y, self.largura, self.altura))
        self.rect.topleft = self.x, self.y
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= 5
            self.andar1 = True
        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += 5
            self.andar = True
        if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
            self.y += 5
            self.andar_baixo = True
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
            self.y -= 5
            self.andar_cima = True
            
        if self.x >= LARGURA-70:
            self.x = LARGURA-71
        elif self.x <= 55:
            self.x = 56
        elif self.y >= ALTURA-64:
            self.y = ALTURA-65
        elif self.y <= 75:
            self.y = 76
        
#tiros
class TIRO(pygame.sprite.Sprite): #Atributos do tiro
    def __init__(self, x, y, mouse_x, mouse_y, x_s, y_s, dano):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.sprites = [] #lista de sprites do tiro
        self.ponto = 0 #pontuação por morte de inimigos
        self.x_s = x_s
        self.y_s = y_s
        self.dano = dano
        
        self.sprites.append(pygame.image.load("assets\Bola\Bola.png")) #Sprite do tiro
        #dimencionamento da sprite do tiro
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.x_s, self.y_s))

        #atributos para calcular a direção do tiro
        self.speed = 10
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def update(self,janela): #disparo
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (self.x_s, self.y_s))
        self.show = janela.blit(self.image, (self.x, self.y))
        self.show

#inimigo
class INIMIGO(pygame.sprite.Sprite):
    def __init__(self, x, y, altura, largura, life, speed, dano, mob):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.sprites = []
        self.life = life
        self.speed = speed
        self.dano = dano

        #define o mob
        self.mob = mob

        #sprites monstro
        #1 = Gosma [0 - 11]
        self.sprites.append(pygame.image.load("assets\gosma\gosma0.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma1.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma2.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma3.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma4.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma5.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma6.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma7.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma8.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma9.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma10.png"))
        self.sprites.append(pygame.image.load("assets\gosma\gosma11.png"))

        #2 = Esqueleto! [12 - 13]
        self.sprites.append(pygame.image.load("assets\Esqueleto\Esqueleto.png"))
        self.sprites.append(pygame.transform.flip(self.sprites[12], True, False))
        #3 = Rato [14 - 15]
        self.sprites.append(pygame.image.load("assets\Mice\Mice.png"))
        self.sprites.append(pygame.transform.flip(self.sprites[14], True, False))

        #Dimensionamento
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))

        
    def update(self, janela): #Animação e Movimentação do monstro
        #Animação
        if self.mob == 1:
            self.atual += 0.30
        if self.mob >= 2:
            self.atual += 0.05
        if self.mob == 1:
            self.atual += 0.30
            if self.atual >= 11:
                self.atual = 0
                MOVIMENTO_SLIME.play()
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))

        if self.mob == 2:
            if self.atual <= 12 or self.atual >= 14:
                self.atual = 12
                MOVIMENTO_MONSTRO.play()
            self.image = self.sprites[(int(self.atual))]
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))

        if self.mob == 3:
            if self.atual <= 14 or self.atual >= 16:
                self.atual = 14
                MOVIMENTO_MICE.play()
            self.image = self.sprites[(int(self.atual))]
            self.image = pygame.transform.scale(self.image, (self.largura, self.altura))

        #Movimentação
        self.rect.topleft = self.x, self.y
        if self.x >= jogador.x:
            self.x -= self.speed
        if self.x <= jogador.x:
            self.x += self.speed
        if self.y >= jogador.y:
            self.y -= self.speed
        if self.y <= jogador.y:
            self.y += self.speed

        janela.blit(self.image,(self.x, self.y))

class AVO(pygame.sprite.Sprite):
    def __init__(self, x, y, altura, largura, life, speed, dano):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.altura = altura
        self.largura = largura
        self.sprites = []
        self.life = life
        self.speed = speed
        self.dano = dano

        #sprites monstro
        self.sprites.append(pygame.image.load("assets\Veia_Enferma\Veia.png"))

        #Dimensionamento
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y


        
    def update(self, janela): #Animação e Movimentação do monstro

        #Animação
        self.atual += 0
        if self.atual <= 1:
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (self.largura, self.altura))


        janela.blit(self.image,(self.x, self.y))

class BOSS_ATAQUE(pygame.sprite.Sprite): #Atributos do tiro
    def __init__(self, x, y, jogador_x, jogador_y, x_s, y_s, dano):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.mouse_x = jogador_x
        self.mouse_y = jogador_y
        self.sprites = [] #lista de sprites do tiro
        self.ponto = 0 #pontuação por morte de inimigos
        self.x_s = x_s
        self.y_s = y_s
        self.dano = dano

        
        self.sprites.append(pygame.image.load("assets\Bola\_vovo_atq.png")) #Sprite do tiro
        #dimencionamento da sprite do tiro
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = pygame.transform.scale(self.image, (self.x_s, self.y_s))

        #atributos para calcular a direção do tiro
        self.speed = 10

        self.angle = math.atan2(y-jogador_y, x-jogador_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        
        

    def update(self,janela): #disparo

        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (self.x_s, self.y_s))
        self.show = janela.blit(self.image, (self.x, self.y))
        self.show
            

class BOTAO():
    def __init__(self, x, y, widht, height, image, image2):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (widht, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.image2 = image2
        self.widht = widht
        self.height =height

    def draw(self, janela):
        acao = False

        posicao_mouse = pygame.mouse.get_pos()

        if self.rect.collidepoint(posicao_mouse):
            self.image1 = pygame.transform.scale(self.image2, (self.widht+15, self.height+15))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                acao = True
            janela.blit(self.image1, (self.rect.x-20, self.rect.y-20))
        else:
            self.image1 = pygame.transform.scale(self.image, (self.widht, self.height))
            janela.blit(self.image1, (self.rect.x, self.rect.y))
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        return acao

todas_as_sprites = pygame.sprite.Group() #grupo com todas as sprites do jogo

janela = pygame.display.set_mode((LARGURA, ALTURA)) #tamanho da tela
pygame.display.set_caption(NOME_JOGO) #Nome do jogo
pygame.display.set_icon(ICONE) #icone de jogo
janela.fill(MARROM_CLARO)

#jogador
jogador = PLAYER(298,208,42,42)
todas_as_sprites.add(jogador)


#inimigo
slime = []
todas_as_sprites.add(slime)
boss = []
todas_as_sprites.add(boss)

tiros = []
atirar = pygame.sprite.Group()
atirar.add(tiros)
todas_as_sprites.add(tiros)

golpe = []
golpear = pygame.sprite.Group()
golpear.add(golpe)
todas_as_sprites.add(golpe)
enemy = pygame.sprite.Group() #grupo com todas as sprites de inimigos dentro do jogo
enemy.add(slime)
enemy.add(boss)
kills = 0 #conta as vezes que o inimigo foi morto
spaw_boss = 0
vida = 0 #recebera a quantidade de HP do jogador
#tempo
tempo_global = 1201
tempo = 100
tempo_boss = 600
delay_boss = 600
delay_boss2 = 300
boss_spaw = 1
atacando = 0
danger = 1
comb = 0

#telas
start = True
jogando = False
game_over = False
pause = False
creditos = False
quadrinhos = False
chefe = False
chefe_start = False
#botões
start_button = BOTAO(LARGURA/2-140, ALTURA-43, 60,35,START_IMAGEM, START_IMAGEM2)
restart_button = BOTAO(LARGURA/2-60, ALTURA/2, 120,70,RESTART_IMAGEM, RESTART_IMAGEM2)
sair_button = BOTAO(LARGURA/2-60, ALTURA/2+80, 120,70,SAIR_IMAGEM, SAIR_IMAGEM2)
sair_button_inicial = BOTAO(LARGURA/2-60, ALTURA-43, 60,35,SAIR_IMAGEM, SAIR_IMAGEM2)
continuar_button = BOTAO(LARGURA/2-60, ALTURA/2-80, 120,70,CONTINUAR_IMAGEM, CONTINUAR_IMAGEM2)
creditos_button = BOTAO(LARGURA/2+20, ALTURA-43, 60,35,CREDITOS_IMAGEM, CREDITOS_IMAGEM2)
voltar_button = BOTAO(LARGURA/2+20, ALTURA-43, 60,35,VOLTAR_IMAGEM, VOLTAR_IMAGEM2)
#situação dentro do jogo
perigo = True
vovo = False
#Delay entre os tiros
delay = 0
carregado = 0

#Quadrinhos
arte_time = 0
comic = []
comic.append(pygame.image.load("assets\comic\_comic1.jpg"))
comic.append(pygame.image.load("assets\comic\_comic2.jpg"))
comic.append(pygame.image.load("assets\comic\_comic3.jpg"))
comic.append(pygame.image.load("assets\comic\_comic4.jpg"))
comic_tela = 0

while True:

    if start:
        janela.fill((255,0,0)) #cor da tela
        janela.blit(TELA_START, (0,0))
        MUSICA.play()
        MUSICA.set_volume(0.20)

        if start_button.draw(janela):
            jogador.hp = 10 #cura o jogador
            kills = 0 #zera o contador de kills
            start = False
            quadrinhos = True #fecha a tela de game over e exibe novamente a tela do jogo zerada
            pygame.mixer_music.load("som\quadrinhos.wav") # PRECISA TROCAR ESSA MUSICA!!!
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.10)
            MUSICA.stop()
        if sair_button_inicial.draw(janela):
            sys.exit()
            pygame.QUIT
        if creditos_button.draw(janela):
            start = False
            creditos = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_s]: #fechar o jogo
                sys.exit()
                pygame.QUIT

    elif creditos:
        janela.fill((0,0,0)) #cor da tela
        janela.blit(TELA_START, (0,0))
        creditos_texto = ["MUSICAS",
            "https://opengameart.org/content/free-music-pack",
            "Autor: tricksntraps",
            "",
            "Copyright/Attribution Notice: ",
            "https://www.youtube.com/@AlexandrZhelanovsMusic",
            "Autor: Alexandr Zhelanov",
            "",
            "EFEITOS SONOROS",
            "",
            "Licensing: Creative Commons Zero (CC0)",
            "https://opengameart.org/node/16331",
            "Autor: AntumDeluge",
            "",
            "DrMinky - https://freesound.org/people/DrMinky/sounds/167074/",
            "",
            "mrickey13 - https://freesound.org/people/mrickey13/sounds/515623/"]
        y = 0

        for linha in creditos_texto:
            continuar = FONTE_CREDITOS.render(linha, True, (255,255,255)) #formatação das opções continuar ou sair
            janela.blit(continuar, (0,y)) #exibe a mensagem continuar ou sair na tela
            y += 14
        MUSICA_PM.play()
        MUSICA_PM.set_volume(0.08)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_s]:
                sys.exit()
                pygame.QUIT
            
            """if pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_v]:
                    creditos = False
                    start = True"""
        if sair_button_inicial.draw(janela):
            sys.exit()
            pygame.QUIT
        if voltar_button.draw(janela):
            creditos = False
            start = True

    elif quadrinhos:
        janela.fill((0,0,0)) #cor da tela

        if arte_time == 1500:
            comic_tela += 1
        elif arte_time == 3000:
            comic_tela += 1
        elif arte_time == 4500:
            comic_tela += 1
        comic_atual = pygame.transform.scale(comic[comic_tela], (LARGURA,ALTURA))
        janela.blit(comic_atual, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_s]: #fechar o jogo
                sys.exit()
                pygame.QUIT

        arte_time += 1
        if arte_time >= 6000 : #4000
            quadrinhos = False
            jogando = True
            jogador.hp = 10 #cura o jogador
            kills = 0 #zera o contador de kills
            pygame.mixer_music.load("som\_playgame_sound.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.30)
            MUSICA.stop()

    elif jogando: #looping principal do jogo rodando aqui!
        janela.fill(MARROM_CLARO)
        mouse_x, mouse_y = pygame.mouse.get_pos() #cordenadas do mouse
        janela.blit(FUNDO, (0,0)) #fundo da tela
        mensagem = f'kills: {kills}' #mensagem que sera exibita na tela do jogo
        mensagem_formatada = FONTE.render(mensagem, True,  (255,0,0)) #formatação da mensagem, utilizando a fonte que foi deifinada e a sua localização na tela
        hp = f'HP: {vida}' #Texto da tela sobre o HP do jogador
        hp_formatado = FONTE.render(hp, True, (255,0,0)) #formatação do texto HP

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #fechar o jogo
                sys.exit()
                pygame.QUIT

            if event.type == pygame.MOUSEBUTTONDOWN: #verificação se do mouse
                if delay <= 0:
                    if event.button == 1:
                        tiros.append(TIRO(jogador.x, jogador.y, mouse_x, mouse_y, 15, 15, 1)) #iniciação do tiro
                        atirar.add(tiros) #adiciona o tiro criado dentro do grupo de sprites atirar
                        delay = 20
                        efeito = random.randint(1,3)
                        if efeito == 1:
                            EFEITO_COLISAO.play() #som do disparo do tiro
                            EFEITO_COLISAO.set_volume(0.15) #volume do som do disparo do tiro
                        if efeito == 2:
                            EFEITO_COLISAO2.play() #som do disparo do tiro
                            EFEITO_COLISAO2.set_volume(0.15) #volume do som do disparo do tiro
                        if efeito == 3:
                            EFEITO_COLISAO3.play() #som do disparo do tiro
                            EFEITO_COLISAO3.set_volume(0.15) #volume do som do disparo do tiro

            if pygame.mouse.get_pressed()[0]:
                carregado += 1
            
            if event.type == pygame.MOUSEBUTTONUP:
                if carregado >= 40:
                    tiros.append(TIRO(jogador.x+21, jogador.y+21, mouse_x, mouse_y, 30, 30, 3)) #iniciação do tiro
                    atirar.add(tiros) #adiciona o tiro criado dentro do grupo de sprites atirar
                    delay = 15
                        
                    efeito = random.randint(1,3)
                    if efeito == 1:
                        EFEITO_COLISAO.play() #som do disparo do tiro
                        EFEITO_COLISAO.set_volume(0.15) #volume do som do disparo do tiro
                    if efeito == 2:
                        EFEITO_COLISAO2.play() #som do disparo do tiro
                        EFEITO_COLISAO2.set_volume(0.15) #volume do som do disparo do tiro
                    if efeito == 3:
                        EFEITO_COLISAO3.play() #som do disparo do tiro
                        EFEITO_COLISAO3.set_volume(0.15) #volume do som do disparo do tiro
                    carregado = 0



            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]: #pausar o jogo
                    jogando = False
                    pause = True
                    pygame.mixer.music.pause()


        if jogador.hp <= 0: #game over
            jogando = False
            game_over = True
            pygame.mixer.music.pause()
            enemy.remove(slime)
            enemy.remove(boss)
            slime = []
            boss = []

        if perigo:
            if tempo_global == 0:
                perigo = True
                tempo_global = 600


            if spaw_boss >= 20:
                if boss_spaw >= 0:
                    VOVO_AUDIO.play()
                    tempo_boss = 300
                    boss_spaw -= 1
                    delay_boss = 300
                if tempo_boss <= 0: #analisa o contador, sempre que ele chegar a zero gera um monstro na tela e rezeta a contagem
                    boss.append(AVO(LARGURA/2-80, 0, 120, 105, 50, 2, 2)) #cria o boss na lista slime
                    enemy.add(boss) #adiciona o boss criada no grupo de sprites enemy
                    tempo_boss = 90000
                    chefe = True
                if delay_boss <= 0:
                    if danger%5 == 0:
                        atacando = 9
                        VOVO_AUDIO.play()
                        VOVO_AUDIO.set_volume(0.30)
                    else:
                        atacando = random.randint(1,11)
                        delay_boss = 300
                if delay_boss2%50 == 0 and chefe == True:
                    if 1 <= atacando <= 7:
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, jogador.x, jogador.y, 15, 15, 1)) #golpe do boss
                        danger += 1
                        VOVO_AUDIO.play()
                        VOVO_AUDIO.set_volume(0.30)
                    if 8 <= atacando <= 10:
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 0, 156.1, 15, 15, 1))
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 97.4, 263.6, 15, 15, 1))
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 175.5, 315.7, 15, 15, 1))
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 296, 367.8, 15, 15, 1))
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 376.4, 347.4, 15, 15, 1))
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 465.8, 290.8, 15, 15, 1))
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 554.1, 216, 15, 15, 1))
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, 592, 150.3, 15, 15, 1))
                        danger += 1
                        VOVO_AUDIO.play()
                        VOVO_AUDIO.set_volume(0.30)
                if atacando > 10:
                    if comb%20 == 0:
                        golpe.append(BOSS_ATAQUE(boss[0].x + 60, boss[0].y+52.5, random.randint(0, LARGURA), random.randint(0, ALTURA), 15, 15, 1))
                    if delay_boss2%35 == 0:
                        VOVO_AUDIO.play()
                        VOVO_AUDIO.set_volume(0.30)




                #if len(boss) == 0:
                    #spaw_boss = 0
                    #boss_spaw = 1
            else:
                if tempo <= 0: #analisa o contador, sempre que ele chegar a zero gera um monstro na tela e rezeta a contagem
                    monstro = random.randint(1,3)
                    if monstro == 1:
                        slime.append(INIMIGO(random.randint(0, LARGURA), random.randint(0, ALTURA), 40,40, 3, 2, 1, 1)) #cria o monstro na lista slime
                        enemy.add(slime) #adiciona a slime criada no grupo de sprites enemy
                        tempo = 137 #volta a contagem regressiva a partir do 150
                    elif monstro == 2:
                        slime.append(INIMIGO(random.randint(0, LARGURA), random.randint(0, ALTURA), 40,40, 3, 0.5, 2, 2)) #cria o monstro na lista slime
                        enemy.add(slime) #adiciona a slime criada no grupo de sprites enemy
                        tempo = 137 #volta a contagem regressiva a partir do 150
                    elif monstro == 3:
                        slime.append(INIMIGO(random.randint(0, LARGURA), random.randint(0, ALTURA), 40,40, 2, 2.8, 1, 3)) #cria o monstro na lista slime
                        enemy.add(slime) #adiciona a slime criada no grupo de sprites enemy
                        tempo = 137 #volta a contagem regressiva a partir do 150

        
        for disparo in tiros: #desenha o tiro na tela
            disparo.update(janela)
            #kills += disparo.ponto #adiciona o valor de pontos da classe tiro ao contador de kills
        for disparo in golpe:
            disparo.update(janela)
        for gosma in slime:
            gosma.update(janela)
        for vovo in boss:
            vovo.update(janela)
            

        vida = jogador.hp
        todas_as_sprites.draw(janela)
        todas_as_sprites.update()
        jogador.main()

        for t in tiros[:]:
            if t.x <= 0 or t.x >= LARGURA:
                tiros.remove(t)
            elif t.y <= 0 or t.y >= ALTURA:
                tiros.remove(t)
            for gosma in slime[:]:
                if pygame.Rect.colliderect(t.rect, gosma.rect): #verifica a colisão do tiro com a gosma
                    tiros.remove(t) #apaga o tiro
                    gosma.life -= t.dano #dano na gosma
                    if gosma.life <= 0: #verifica a vida da gosma, se for menor que zero ira apaga-la da tela
                        slime.remove(gosma) #remove a gosma da lista slime
                        enemy.remove(gosma) #remove a gosma do grupo de sprites enemy
                        kills += 1
                        spaw_boss += 1
            for vovo in boss[:]:
                if pygame.Rect.colliderect(t.rect, vovo.rect): #verifica a colisão do tiro com a gosma
                    tiros.remove(t) #apaga o tiro
                    vovo.life -= t.dano #dano na gosma
                    if vovo.life <= 0: #verifica a vida da gosma, se for menor que zero ira apaga-la da tela
                        boss.remove(vovo) #remove a gosma da lista slime
                        enemy.remove(vovo) #remove a gosma do grupo de sprites enemy
                        kills += 1
                        spaw_boss = 0
                        tempo = 120
                        chefe = False
                        tempo_boss = 150
                        pygame.mixer.music.unpause()
        
        
        for t in golpe:
            if t.x <= 0 or t.x >= LARGURA:
                golpe.remove(t)
            elif t.y <= 0 or t.y >= ALTURA:
                golpe.remove(t)
            if pygame.Rect.colliderect(t.rect, jogador.rect):
                golpe.remove(t)
                jogador.hp -= t.dano
                efeito = random.randint(1,3)
                if efeito == 1:
                    MORTE_JOGADOR.play()
                elif efeito == 2:
                    MORTE_JOGADOR2.play()
                elif efeito == 3:
                    MORTE_JOGADOR3.play()

        janela.blit(mensagem_formatada, (530,0)) #exibe o contador de kills na tela
        janela.blit(hp_formatado, (40,0)) #exibe o HP do jogador na tela
        tempo -= 1 #a cada frame diminui o contador tempo para spaw das gosmas
        tempo_boss -= 1 #a cada frame diminui o contador de tempo para spwanar o boss
        delay_boss -= 1
        delay_boss2 -= 1
        comb += 5
        chefe_start += 1
        tempo_global -= 1 #conta o tempo global
        delay -= 1
        RELOGIO.tick(60) #frames

    elif game_over: #tela de game over
        janela.fill((0,0,0)) #cor da tela
        janela.blit(TELA_GAMEOVER, (0,0))
        MUSICA_GO.play()
        MUSICA_GO.set_volume(0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_s]: #fechar o jogo
                sys.exit()
                pygame.QUIT

        if sair_button.draw(janela):
            sys.exit()
            pygame.QUIT
        if restart_button.draw(janela):
            jogador.hp = 10 #cura o jogador
            kills = 0 #zera o contador de kills
            game_over = False
            jogando = True #fecha a tela de game over e exibe novamente a tela do jogo zerada
            pygame.mixer.music.unpause()
            pygame.mixer.music.rewind()
            MUSICA_PM.stop()
            jogador.x = 298
            jogador.y = 208
            perigo = True
            tempo_global = 1201
            tempo = 100
            tempo_boss = 600

    elif pause: #tela de pause
        janela.fill((0,0,0)) #cor da tela
        janela.blit(TELA_START, (0,0))
        MUSICA_PM.play()
        MUSICA_PM.set_volume(0.08)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_s]: #fechar o jogo
                sys.exit()
                pygame.QUIT

        if sair_button.draw(janela):
            sys.exit()
            pygame.QUIT
        if restart_button.draw(janela):
            jogador.hp = 10 #cura o jogador
            kills = 0 #zera o contador de kills
            game_over = False
            jogando = True #fecha a tela de game over e exibe novamente a tela do jogo zerada
            pygame.mixer.music.unpause()
            pygame.mixer.music.rewind()
            MUSICA_PM.stop()
            jogador.x = 298
            jogador.y = 208
            enemy.remove(slime)
            slime = []
            atirar.remove(tiros)
            tiros = []
            perigo = True
            tempo_global = 1201
            tempo = 100
            tempo_boss = 600
        if continuar_button.draw(janela):
            pause = False
            jogando = True
            pygame.mixer.music.unpause()
            MUSICA_PM.stop()

    pygame.display.update()

    

pygame.QUIT