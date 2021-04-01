# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from jogador import *
from PPlay.animation import *

class Jogo():

    janela = Window(1280,720)
    janela.set_title("Battle of the heroes")
    teclado = Window.get_keyboard()

    jogador1 = {'direita' : Sprite("Assets/Jogador1/corrida-direita1.png", 8), 'esquerda' :Sprite("Assets/Jogador1/corrida-esquerda1.png", 8), 'parado' :Sprite("Assets/Jogador1/parado1.png",5), 'ataque-direita' :Sprite("Assets/Jogador1/ataque-direita-azul (1).png", 7), 'ataque-esquerda' :Sprite("Assets/Jogador1/Ataque-esquerda1.png", 7)}
    for i in jogador1:
        jogador1[i].set_position(20,janela.height - jogador1[i].height - 30)
        jogador1[i].set_total_duration(1000)

    jogador2 = {'direita' : Sprite("Assets/Jogador2/Corrida-direita.png", 8), 'esquerda' :Sprite("Assets/Jogador2/Corrida-esquerda.png", 8), 'parado' :Sprite("Assets/Jogador2/Parado.png",5), 'ataque-direita' :Sprite("Assets/Jogador2/Ataque-direita.png", 7), 'ataque-esquerda' :Sprite("Assets/Jogador2/Ataque-esquerda.png", 7)}
    for i in jogador2:
        jogador2[i].set_position(janela.width-jogador2[i].width-20,janela.height - jogador2[i].height - 30)
        jogador2[i].set_total_duration(1000)

    pe = Sprite("Assets/pad2.png", 1)
    pe2 = Sprite("Assets/pad2.png", 1)
    pe.set_position(66,janela.height - pe.height - 33)
    pe2.set_position(janela.width-pe.width-66,janela.height - pe.height - 45)

    jump1 = True
    jump2 = True
    fundo = GameImage("Assets/torcida2.jpg")

    velX = 450
    velY = 0
    velX2= 450
    velY2 = 0
    velpeX = 90
    velpeY = 0
    velpeX2 = 90
    velpeY2 = 0

    plataforma = GameImage("Assets/plataformaPequena.png")
    plataforma2 = GameImage("Assets/plataformaMedia.png")
    plataforma3 = GameImage("Assets/plataformaPequena.png")
    plataforma.set_position(150, janela.height - plataforma.height- 175)
    plataforma2.set_position(640 - (plataforma2.width/2),janela.height - plataforma2.height - 325)
    plataforma3.set_position(janela.width - 320, janela.height - plataforma3.height - 175)
    
    chao1 = GameImage("Assets/chao-plataformaPequena.png")
    chao2 = GameImage("Assets/chao-plataformaPequena.png")
    chao3 = GameImage("Assets/chao-plataformaMedia.png")
    chao1.set_position(150,janela.height - plataforma.height- 175)
    chao2.set_position(janela.width - 320, janela.height - plataforma.height- 175)
    chao3.set_position(640 - (plataforma2.width/2),janela.height - plataforma2.height - 325)
    
    cont = 0
    fps = 0
    atual = 0
    while True:
        ##FPS
        cont += janela.delta_time()
        fps += 1
        ##Atualizaçao jogadores
        velY ,jump1, velpeY= Jogador.controles(jogador1, janela, velX, velY, teclado, jump1, "w","s","a","d","space", [chao1, chao2, chao3],pe,velpeX,velpeY)
        velY2 ,jump2, velpeY2= Jogador.controles(jogador2, janela, velX2, velY2, teclado, jump2, "up","down","left","right","enter",[chao1, chao2, chao3],pe2,velpeX2,velpeY2)
        if cont>1:
            atual= fps
            cont=0
            fps=0
        ##Draws
        fundo.draw()
        janela.draw_text(f"FPS:{atual}", 10, 10, size=40, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
        plataforma.draw()
        plataforma2.draw()
        plataforma3.draw()
        for i in jogador1:
            jogador1[i].draw()
            jogador1[i].update()
        for i in jogador2:
            jogador2[i].draw()
            jogador2[i].update()
        
        janela.update()