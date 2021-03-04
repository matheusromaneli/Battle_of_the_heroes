# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from mecanica import *
from PPlay.animation import *

class Main():
        janela = Window(1280,720)
        janela.set_title("Battle of the heroes")
        teclado = Window.get_keyboard()
        jogador1 = Sprite("Assets/Gladiator-parado.png", 5)
        jogador2 = Sprite("Assets/Gladiador2.png", 8)
        jogador1.set_position(20,janela.height - jogador1.height - 30)
        jogador2.set_position(1140,janela.height - jogador2.height - 30)
        jump1 = True
        jump2 = True
        fundo = GameImage("Assets/torcida2.jpg")
        velX = 450
        velY = 0
        velX2= 450
        velY2 = 0
        jogador1.set_total_duration(1000)
        jogador2.set_total_duration(1000)
        while True:
            
            velX, velY ,jump1 = Mecanica.controles(jogador1, janela, velX, velY, teclado, jump1)
            velX2, velY2 ,jump2 = Mecanica.controles2(jogador2, janela, velX2, velY2, teclado, jump2)
            jogador1.play()
            jogador1.update()

            fundo.draw()
            jogador1.draw()
            jogador2.draw()
            janela.update()