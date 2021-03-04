from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *

class Mecanica():

    @classmethod
    def controles(self,jogador1, janela, velX, velY, teclado,jump1):
        
        if jogador1.y > janela.height - jogador1.height - 50:
            jump1 = True  

        else:

            jogador1.y -= velY * janela.delta_time()   
            velY-= 1600 * janela.delta_time()

        if teclado.key_pressed("W"):
            if(jump1):
                velY = 1000
                jogador1.y -= velY * janela.delta_time()
            jump1 = False

        if teclado.key_pressed("S"):

            velY-= 1600 * janela.delta_time()

        if teclado.key_pressed("A") and jogador1.x > 0:

            jogador1.x -= velX * janela.delta_time()

        if teclado.key_pressed("D") and jogador1.x < janela.width - jogador1.width:

            jogador1.x += velX * janela.delta_time()

        return velX , velY , jump1

    @classmethod
    def controles2(self,jogador1, janela, velX, velY, teclado,jump1):
        
        if jogador1.y > janela.height - jogador1.height - 50:
            jump1 = True  

        else:

            jogador1.y -= velY * janela.delta_time()   
            velY-= 1600 * janela.delta_time()
            
        if teclado.key_pressed("UP"):
            if(jump1):
                velY = 1000
                jogador1.y -= velY * janela.delta_time()
            jump1 = False

        if teclado.key_pressed("DOWN"):

            velY-= 1600 * janela.delta_time()

        if teclado.key_pressed("LEFT") and jogador1.x > 0:

            jogador1.x -= velX * janela.delta_time()

        if teclado.key_pressed("RIGHT") and jogador1.x < janela.width - jogador1.width:

            jogador1.x += velX * janela.delta_time()

        return velX , velY , jump1