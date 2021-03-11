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
        jogador1 = {'direita' : Sprite("Assets/Jogador1/Corrida-direita.png", 8), 'esquerda' :Sprite("Assets/Jogador1/Corrida-esquerda.png", 8), 'parado' :Sprite("Assets/Jogador1/Parado.png",5)}
        for i in jogador1:
            jogador1[i].set_position(20,janela.height - jogador1[i].height - 30)
            jogador1[i].set_total_duration(1000)
        jogador2 = {'direita' : Sprite("Assets/Jogador2/Corrida-direita.png", 8), 'esquerda' :Sprite("Assets/Jogador2/Corrida-esquerda.png", 8), 'parado' :Sprite("Assets/Jogador2/Parado.png",5)}
        for i in jogador2:
            jogador2[i].set_position(janela.width-jogador2[i].width-20,janela.height - jogador2[i].height - 30)
            jogador2[i].set_total_duration(1000)
        jump1 = True
        jump2 = True
        fundo = GameImage("Assets/torcida2.jpg")
        velX = 450
        velY = 0
        velX2= 450
        velY2 = 0
        while True:

            velY ,jump1 = Jogador.controles(jogador1, janela, velX, velY, teclado, jump1, "w","s","a","d")
            velY2 ,jump2 = Jogador.controles(jogador2, janela, velX2, velY2, teclado, jump2, "up","down","left","right")

            
            fundo.draw()
            for i in jogador1:
                jogador1[i].draw()
                jogador1[i].update()
            for i in jogador2:
                jogador2[i].draw()
                jogador2[i].update()
            janela.update()