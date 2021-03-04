# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *


janela = Window(1280,720)
janela.set_title("Battle of the heroes")
teclado = Window.get_keyboard()
jogador1 = Sprite("Assets/bola2.png", 1)
jogador1.set_position(20,janela.height - jogador1.height - 50)
jump1 = True
fundo = GameImage("Assets/torcida2.jpg")
velX = 450
velY = 0
while True:

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
    
    # jogador1.y += 1

    fundo.draw()
    jogador1.draw()
    janela.update()