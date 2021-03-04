from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.animation import *

def set_animation(player,teclado):
    x = player.x
    y = player.y

    if(teclado.key_pressed("A")):
        
        if(not(player.is_playing())):
            player = Sprite("Assets/Gladiator-corrida-esquerda.png",8)
            player.play()

    elif teclado.key_pressed("D"):

        if(not(player.is_playing())):
            player = Sprite("Assets/Gladiator-corrida.png",8)
            player.set_initial_frame(7)
            player.play()
    else:
        player.stop()
        
    player.set_position(x,y)
    player.set_total_duration(1000)

    return player

def set_animation2(player,teclado):
    x = player.x
    y = player.y

    if(teclado.key_pressed("LEFT")):
        if(not(player.is_playing())):
            player = Sprite("Assets/Gladiador2-corrida-esquerda.png",8)
            player.play()
    elif teclado.key_pressed("RIGHT"):
        if(not(player.is_playing())):
            player = Sprite("Assets/Gladiador2-corrida.png",8)
            player.set_initial_frame(7)
            player.play()
    else:
        player.stop()
    player.set_position(x,y)
    player.set_total_duration(1000)

    return player

class Mecanica():
    

    @classmethod
    def controles(self,jogador1, janela, velX, velY, teclado,jump1):
        
        jogador1 = set_animation(jogador1,teclado)

        if jogador1.y > janela.height - jogador1.height - 30:
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
            jogador1.play()

        if teclado.key_pressed("D") and jogador1.x < janela.width - jogador1.width:

            jogador1.x += velX * janela.delta_time()
            jogador1.update()

        return velX , velY , jump1, jogador1

    @classmethod
    def controles2(self,jogador1, janela, velX, velY, teclado,jump1):
        
        jogador1 = set_animation2(jogador1,teclado)

        if jogador1.y > janela.height - jogador1.height - 30:
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
            jogador1.update()

        if teclado.key_pressed("RIGHT") and jogador1.x < janela.width - jogador1.width:
            jogador1.x += velX * janela.delta_time()
            jogador1.update()

        return velX , velY , jump1, jogador1