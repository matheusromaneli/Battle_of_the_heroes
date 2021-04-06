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

    sprites1 = {'direita' : Sprite("Assets/Jogador1/Corrida-direita.png", 8), 'esquerda' :Sprite("Assets/Jogador1/Corrida-esquerda.png", 8), 'parado-direita' :Sprite("Assets/Jogador1/parado-direita.png",5),'parado-esquerda': Sprite("Assets/Jogador1/parado-esquerda.png",5), 'ataque-direita' :Sprite("Assets/Jogador1/Ataque-direita.png", 7), 'ataque-esquerda' :Sprite("Assets/Jogador1/ataque-esquerda.png", 7)}
    for i in sprites1:
        sprites1[i].set_position(20,janela.height - sprites1[i].height - 30)
        if i != 'ataque-direita' and i != 'ataque-esquerda':
            sprites1[i].set_total_duration(1000)
        else:
            sprites1[i].set_total_duration(300)
    
    sprites2 = {'direita' : Sprite("Assets/Jogador2/Corrida-direita.png", 8), 'esquerda' :Sprite("Assets/Jogador2/Corrida-esquerda.png", 8), 'parado-direita' :Sprite("Assets/Jogador2/parado-direita.png",5),'parado-esquerda': Sprite("Assets/Jogador2/parado-esquerda.png",5), 'ataque-direita' :Sprite("Assets/Jogador2/Ataque-direita.png", 7), 'ataque-esquerda' :Sprite("Assets/Jogador2/Ataque-esquerda.png", 7)}
    for i in sprites2:
        sprites2[i].set_position(janela.width-sprites2[i].width-20,janela.height - sprites2[i].height - 30)
        if i != 'ataque-direita' and i != 'ataque-esquerda':
            sprites2[i].set_total_duration(1000)
        else:
            sprites2[i].set_total_duration(300)

    pe = Sprite("Assets/pe_jogador.png", 1)
    pe2 = Sprite("Assets/pe_jogador.png", 1)
    pe.set_position(66,janela.height - pe.height - 33)
    pe2.set_position(janela.width-pe.width-66,janela.height - pe.height - 33)

    fundo = GameImage("Assets/fundo.png")

    jogador1 = Jogador(sprites1,450,0,True,"w","s","a","d","space")
    jogador2 = Jogador(sprites2,450,0,True,"up","down","left","right","enter")

    plataformas= [GameImage("Assets/chao-plataformaPequena.png"),GameImage("Assets/chao-plataformaMedia.png"),GameImage("Assets/chao-plataformaPequena.png")]
    plataformas[0].set_position(146,janela.height - 257)
    plataformas[1].set_position(436,janela.height - 411)
    plataformas[2].set_position(janela.width - 320, janela.height - 257)
    
    cont = 0
    fps = 0
    atual = 0
    while True:
        ##FPS
        cont += janela.delta_time()
        fps += 1
        if cont>1:
            atual= fps
            cont=0
            fps=0
        ##Atualizaçao jogadores
        jogador1.controles( janela, teclado, plataformas, pe)
        jogador2.controles( janela, teclado, plataformas, pe2)

        if jogador1.attacking:
            if jogador1.sprites[jogador1.getcurr_animation()].collided(jogador2.sprites[jogador2.getcurr_animation()]):
                jogador2.take_damange()
        else:
            jogador2.invulnerable = False
        
        if jogador2.attacking:
            if jogador2.sprites[jogador2.getcurr_animation()].collided(jogador1.sprites[jogador1.getcurr_animation()]):
                jogador1.take_damange()
        else:
            jogador1.invulnerable = False
        ##Draws
        fundo.draw()
        janela.draw_text(f"FPS:{atual}", 10, 10, size=40, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
        if jogador2.life == 0:
            janela.draw_text("Player 1 Wins", janela.width/2, janela.height/2, size=100, color=(0,0,255), font_name= 'Segoe UI', bold=True, italic=False)
        if jogador1.life == 0:
            janela.draw_text("Player 2 Wins", janela.width/2, janela.height/2, size=100, color=(255,0,0), font_name= 'Segoe UI', bold=True, italic=False)
        for i in jogador1.sprites:
            jogador1.sprites[i].draw()
            jogador1.sprites[i].update()
        for i in jogador2.sprites:
            jogador2.sprites[i].draw()
            jogador2.sprites[i].update()
        janela.update()