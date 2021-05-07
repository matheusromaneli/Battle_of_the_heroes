from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.animation import *

def set_animation(direita, esquerda, last, jogador, attacking):
    if not(attacking):
        for i in jogador:
            jogador[i].hide() 
        if direita:
            jogador['direita'].unhide()
        elif esquerda:
            jogador['esquerda'].unhide()
        elif last == 'esquerda':
            jogador['parado-esquerda'].unhide()
        else:
            jogador['parado-direita'].unhide()

def attack_animation(sprites, side):

        for i in sprites:
            sprites[i].hide()

        if side =='direita':
            sprites['ataque-direita'].unhide()
            sprites['ataque-direita'].play()
            
        else:
            sprites['ataque-esquerda'].unhide()
            sprites['ataque-esquerda'].play()

class Jogador():

    def __init__(self, sprites, velX, velY, jump, cima, baixo, esquerda,direita, ataque):
        self.sprites = sprites
        self.velX = velX
        self.velY = velY
        self.jump = jump
        self.controleCima = cima
        self.controleBaixo = baixo
        self.controleEsquerda = esquerda
        self.controleDireita = direita
        self.controleAtaque = ataque
        self.last = ''
        self.life = 5
        self.life_bar = []
        for i in range(self.life):
            self.life_bar.append([GameImage("Assets/comvida.png"),GameImage("Assets/semvida.png")])
        for i in range(len(self.life_bar)):
            for j in self.life_bar[i]:
                j.set_position(sprites['direita'].x-j.width/2 + i * j.width , sprites['direita'].y-j.height-5)
        self.attacking = False
        self.cooldownAtack = 0
        self.invulnerable = False
        
    def getcurr_animation(self):
        for i in self.sprites:
            if self.sprites[i].drawable:
                return i
    
    def controles(self, janela, teclado, plataformas, pe):
        posInicial = self.sprites['direita'].x
        ##Física do pulo
        if self.sprites['direita'].y >= janela.height - self.sprites['direita'].height - 30:

            self.jump = True  

        else:
            for i in self.sprites:
                self.sprites[i].y -= self.velY * janela.delta_time()
            for i in range(len(self.life_bar)):
                for j in self.life_bar[i]:
                    j.y -= self.velY * janela.delta_time()
            pe.y -= self.velY * janela.delta_time()
            self.velY-= 2000 * janela.delta_time()
           
            for plataforma in plataformas:
                #para de cair   
                if (Collision.collided(pe, plataforma) and self.velY < 0) and not(teclado.key_pressed(self.controleBaixo)):
                    self.velY = 0
                    self.jump = True

        ##Controles
        #CIMA
        if teclado.key_pressed(self.controleCima):

            if(self.jump):

                self.velY = 1000
                for i in self.sprites:
                    self.sprites[i].y -= self.velY * janela.delta_time()
                for i in range(len(self.life_bar)):
                    for j in self.life_bar[i]:
                        j.y -= self.velY * janela.delta_time()
                pe.y -= self.velY * janela.delta_time()
            self.jump = False
        #Baixo
        if teclado.key_pressed(self.controleBaixo):
            self.velY-= 2000 * janela.delta_time()
        #Esquerda    
        if teclado.key_pressed(self.controleEsquerda) and self.sprites['direita'].x > 0:
            self.last = 'esquerda'

            for i in self.sprites:
                self.sprites[i].x -= self.velX * janela.delta_time()

            for i in range(len(self.life_bar)):
                for j in self.life_bar[i]:
                    j.x -= self.velX * janela.delta_time()

            pe.x -= self.velX * janela.delta_time()
            set_animation(0,1,self.last,self.sprites,self.attacking)

        #Direita
        if teclado.key_pressed(self.controleDireita) and self.sprites['direita'].x < janela.width - self.sprites['direita'].width:
            self.last = 'direita'

            for i in self.sprites:
                self.sprites[i].x += self.velX * janela.delta_time()
            for i in range(len(self.life_bar)):
                for j in self.life_bar[i]:
                    j.x += self.velX * janela.delta_time()

            pe.x += self.velX * janela.delta_time()
            set_animation(1,0,self.last,self.sprites,self.attacking)

        #Parado
        if self.sprites['direita'].x == posInicial:

            set_animation(0,0,self.last,self.sprites,self.attacking)
        
        #Ataque
        if teclado.key_pressed(self.controleAtaque):
            
            if janela.time_elapsed() - self.cooldownAtack > 1000:
                self.attacking = True           
                attack_animation(self.sprites,self.last)
                self.cooldownAtack = janela.time_elapsed()
        if self.sprites['ataque-direita'].get_curr_frame() == self.sprites['ataque-direita'].get_final_frame()-1:
            self.attacking=False
            self.sprites['ataque-direita'].stop()
        if self.sprites['ataque-esquerda'].get_curr_frame() == self.sprites['ataque-esquerda'].get_final_frame()-1:
            self.attacking=False
            self.sprites['ataque-esquerda'].stop()
        return

    def take_damange(self):
        if not(self.invulnerable):
            self.life -= 1
        self.invulnerable = True

    def draw(self):
        for i in self.sprites:
            self.sprites[i].draw()
            self.sprites[i].update()
        for i in range(len(self.life_bar)):
            if i < self.life:
                self.life_bar[i][0].draw()
            else:
                self.life_bar[i][1].draw()
            

