# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from mecanica import *

class Main():
        janela = Window(1280,720)
        janela.set_title("Battle of the heroes")
        teclado = Window.get_keyboard()
        jogador1 = Sprite("Assets/bola2.png", 1)
        jogador2 = Sprite("Assets/bola2.png", 1)
        jogador1.set_position(20,janela.height - jogador1.height - 50)
        jogador2.set_position(100,janela.height - jogador2.height - 50)
        jump1 = True
        jump2 = True
        fundo = GameImage("Assets/torcida2.jpg")
        velX = 450
        velY = 0
        velX2= 450
        velY2 = 0
        while True:

            velX, velY ,jump1 = Mecanica.controles(jogador1, janela, velX, velY, teclado, jump1)
            velX2, velY2 ,jump2 = Mecanica.controles2(jogador2, janela, velX2, velY2, teclado, jump2)

            fundo.draw()
            jogador1.draw()
            jogador2.draw()
            janela.update()