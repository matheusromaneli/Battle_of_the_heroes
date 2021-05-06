from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *
from jogo import *
from creditos import *  

class Menu:
    # Inicialização
    janela = Window(1200,720)
    janela.set_title("Home")
    janela.set_background_color ((0,0,0))

    mouse = Window.get_mouse()
    fundo = GameImage("Assets/fundoMenu.png")
    botaoJogar = Sprite("Assets/botao.jpg", 1)
    botaoSair = Sprite("Assets/botao.jpg", 1)
    botaoCredito = Sprite("Assets/botao.jpg", 1)

    botaoJogar.set_position(480, 226)
    botaoSair.set_position(480, 340)
    botaoCredito.set_position(480, 460)

    while True:

        if mouse.is_over_object(botaoJogar) and mouse.is_button_pressed(1):
            Jogo.init()

        if mouse.is_over_object(botaoSair) and mouse.is_button_pressed(1):
            exit()

        if mouse.is_over_object(botaoCredito) and mouse.is_button_pressed(1):
            Creditos.creditos()

        fundo.draw()
        janela.update()