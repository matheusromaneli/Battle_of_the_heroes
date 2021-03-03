# from Assets.torcida2.jpg import torcida2.jpg 
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

janela = Window(1300,700)
janela.set_title("Battle of the heroes")
teclado = Window.get_keyboard()

fundo = GameImage("Assets/torcida2.jpg")

while True:
    fundo.draw()
    janela.update()