# from Assets.torcida2.jpg import torcida2.jpg 
from winreg import KEY_WOW64_32KEY
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from jogador import *
from PPlay.animation import *

K_w = 26
K_s = 22
K_a = 4
K_d = 7
K_space = 44
class Jogo():
    def init(connection):
        cont = 0
        fps = 0
        atual = 0
        rounds = 1
        contround1 = 0
        contround2 =0
        janela = Window(1280,720)
        janela.set_title("Battle of the heroes")
        janela.update()
        teclado = Window.get_keyboard()
        seg = janela.time_elapsed()
        fundoVitoria1 = GameImage("Assets/Player 1 wins.png")
        fundoVitoria2 = GameImage("Assets/Player 2 wins.png")

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

        fundo = GameImage("Assets/fundo.png")


        plataformas= [GameImage("Assets/chao-plataformaPequena.png"),GameImage("Assets/chao-plataformaMedia.png"),GameImage("Assets/chao-plataformaPequena.png")]
        plataformas[0].set_position(146,janela.height - 257)
        plataformas[1].set_position(436,janela.height - 411)
        plataformas[2].set_position(janela.width - 320, janela.height - 257)
        if(connection.id == "player:1"):
            jogador1 = Jogador(1,connection,sprites1,450,0,janela,True,pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d,pygame.K_SPACE)
            jogador2 = Jogador(0,connection,sprites2,450,0,janela,True,K_w,K_s,K_a,K_d,K_space)
        else:
            jogador1 = Jogador(0,connection,sprites1,450,0,janela,True,K_w,K_s,K_a,K_d,K_space)
            jogador2 = Jogador(1,connection,sprites2,450,0,janela,True,pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d,pygame.K_SPACE)
        
        while True:
            ##FPS
            cont += janela.delta_time()
            fps += 1
            if cont>1:
                atual= fps
                cont=0
                fps=0
            if rounds <= 5:
                while not(connection.ready):
                    fundo.draw()
                    janela.draw_text(f"Round {rounds}", 436, 200, size=100, color=(0,0,0), font_name= 'Segoe UI', bold=True, italic=False)
                    janela.update()
                    
            ##AtualizaÃ§ao jogadores
            if(connection.id == "player:1"):
                jogador1.controles( janela, teclado.keys_pressed(), plataformas)
                jogador2.controles( janela, connection.last_response, plataformas)
            else:
                jogador1.controles( janela, connection.last_response, plataformas)
                jogador2.controles( janela, teclado.keys_pressed(), plataformas)

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
            janela.draw_text(f"FPS:{atual} voce e o {connection.id}", 10, 10, size=25, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
            if jogador2.life == 0:
                contround1 +=1
                if contround1 == 2:
                    seg = janela.time_elapsed()
                    while janela.time_elapsed() - seg < 2500:
                        fundoVitoria1.draw()
                        janela.update()
                    rounds = 4
                    break
                else:
                    seg = janela.time_elapsed()
                    rounds+=1
            if jogador1.life == 0:
                contround2 +=1
                if contround2 == 2:
                    seg = janela.time_elapsed()
                    while janela.time_elapsed() - seg < 2500:
                        fundoVitoria2.draw()
                        janela.update()
                    rounds = 4
                    break
                else:
                    seg = janela.time_elapsed()
                    rounds+=1
            jogador1.draw()
            jogador2.draw()
            jogador1.pe.draw()
            jogador2.pe.draw()
            janela.update()