# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from jogador import *
from PPlay.animation import *

class Main():
        janela = Window(1280,720)
        janela.set_title("Battle of the heroes")
        teclado = Window.get_keyboard()
        jogador1 = {'direita' : Sprite("Assets/Gladiator-corrida.png", 8), 'esquerda' :Sprite("Assets/Gladiator-corrida-esquerda.png", 8), 'parado' :Sprite("Assets/Gladiator-parado.png",5)}
        for i in jogador1:
            jogador1[i].set_position(20,janela.height - jogador1[i].height - 30)
            jogador1[i].set_total_duration(1000)
        # jogador2 = Sprite("Assets/Gladiador2-corrida-esquerda.png", 8)
        # jogador2.set_position(1140,janela.height - jogador2.height - 30)
        jump1 = True
        jump2 = True
        fundo = GameImage("Assets/torcida2.jpg")
        velX = 450
        velY = 0
        velX2= 450
        velY2 = 0
        while True:

            velY ,jump1 = Jogador.controles(jogador1, janela, velX, velY, teclado, jump1, "w","s","a","d")
            # velX2, velY2 ,jump2 = Jogador.controles(jogador2, janela, velX2, velY2, teclado, jump2, "up","down","left","right")

            
            fundo.draw()
            for i in jogador1:
                jogador1[i].draw()
                jogador1[i].update()
            # jogador2.draw()
            # jogador2.update()
            janela.update()