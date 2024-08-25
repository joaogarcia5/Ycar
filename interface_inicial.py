import tkinter as tk
from tkinter import messagebox
from calculadora_gui import criar_calculadora
from musicas_gui import criar_tela_musicas
from utils import centralizar_janela  # Importe a função auxiliar

def criar_tela_inicial():
    root = tk.Tk()
    root.title("Tela Inicial")

    largura = 400
    altura = 350
    centralizar_janela(root, largura, altura)

    def abrir_calculadora():
        root.destroy()  # Fecha a tela inicial
        criar_calculadora()  # Abre a calculadora

    def abrir_gerador_senha():
        # Aqui você deve implementar a função para abrir o gerador de senha
        pass

    def abrir_tela_musicas():
        root.destroy()  # Fecha a tela inicial
        criar_tela_musicas()  # Abre a tela de músicas

    def abrir_informacoes():
        # Aqui você deve implementar a função para abrir a tela de informações
        pass

    def ganhar_milhao():
        messagebox.showinfo("Ganhar 1 Milhão", "Parabéns! Você ganhou 1 milhão de reais!")

    tk.Button(root, text="Calculadora", font=('Arial', 18), command=abrir_calculadora).pack(pady=10)
    tk.Button(root, text="Gerador de Senha", font=('Arial', 18), command=abrir_gerador_senha).pack(pady=10)
    tk.Button(root, text="Músicas", font=('Arial', 18), command=abrir_tela_musicas).pack(pady=10)
    tk.Button(root, text="Informações", font=('Arial', 18), command=abrir_informacoes).pack(pady=10)
    tk.Button(root, text="GANHE 1 MILHÃO DE REAIS", font=('Arial', 18), command=ganhar_milhao).pack(pady=10)

    root.mainloop()
