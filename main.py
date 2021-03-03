# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *


janela = Window(1280,720)
velX = 250
velY = 250
janela.set_title("Battle of the heroes")
teclado = Window.get_keyboard()
jogador1 = Sprite("Assets/bola2.png", 1)

fundo = GameImage("Assets/torcida2.jpg")

while True:

    if teclado.key_pressed("W") and jogador1.y > 0:
        jogador1.y -= velY * janela.delta_time()
    if teclado.key_pressed("S") and jogador1.y < janela.height - jogador1.height - 50:
        jogador1.y += velY * janela.delta_time()
    if teclado.key_pressed("A") and jogador1.x > 0:
        jogador1.x -= velX * janela.delta_time()
    if teclado.key_pressed("D") and jogador1.x < janela.width - jogador1.width:
        jogador1.x += velX * janela.delta_time()
    
    fundo.draw()
    jogador1.draw()
    janela.update()