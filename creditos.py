from PPlay.window import *
from PPlay.gameimage import *


class Creditos:

    def creditos():

        janela = Window(1200,720)
        janela.set_title("Creditos")
        janela.set_background_color ((0,0,0))
        texto = "   Obrigado por jogar Battle of the Heroes!"
        texto2 = "Esse jogo foi desenvolvido a fins educacionais por"
        texto3 = "Leonardo Saracino e Matheus Romaneli."
        texto4 = "press ESC para sair."
        teclado = Window.get_keyboard()

        while True:

            if teclado.key_pressed("ESC"):
                exit()

            janela.draw_text(texto,150, 80, size=50, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
            janela.draw_text(texto2,80,300, size=50, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
            janela.draw_text(texto3,200, 380, size=50, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
            janela.draw_text(texto4,10, 1, size=25, color=(255,255,255), font_name= 'Segoe UI', bold=False, italic=False)
            janela.update()