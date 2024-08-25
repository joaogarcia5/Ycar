import tkinter as tk
from tkinter import messagebox
import pygame
from utils import centralizar_janela  # Importe a função auxiliar

# Inicialize o mixer do pygame
pygame.init()

def criar_tela_musicas():
    root = tk.Tk()
    root.title("Selecionar Música")

    largura = 400
    altura = 480
    centralizar_janela(root, largura, altura)

    def tocar_musica(caminho, start=0):
        try:
            pygame.mixer.music.load(caminho)
            pygame.mixer.music.play(start=start)
            pygame.mixer.music.set_volume(0.1)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a música: {e}")

    def parar_musica():
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao parar a música: {e}")

    def on_select(opcao):
        caminhos = {
            '1': 'mscs/lofi.mp3',
            '2': 'mscs/sorvo.mp3',
            '3': 'mscs/chala.mp3',
            '4': 'mscs/minerap.mp3',
            '5': 'mscs/numb.mp3',
            '6': 'mscs/wii.mp3'
        }
        if opcao == '0':
            parar_musica()
        elif opcao in caminhos:
            tocar_musica(caminhos[opcao])
        else:
            messagebox.showerror("Erro", "Opção inválida")

    tk.Button(root, text="Parar Música", font=('Arial', 18), command=lambda: on_select('0')).pack(pady=10)
    tk.Button(root, text="LO-FI", font=('Arial', 18), command=lambda: on_select('1')).pack(pady=10)
    tk.Button(root, text="Sorvete de Ovo Maltine", font=('Arial', 18), command=lambda: on_select('20')).pack(pady=10)
    tk.Button(root, text="Chala Head Chala", font=('Arial', 18), command=lambda: on_select('3')).pack(pady=10)
    tk.Button(root, text="Rap do Minecraft", font=('Arial', 18), command=lambda: on_select('4')).pack(pady=10)
    tk.Button(root, text="Numb", font=('Arial', 18), command=lambda: on_select('5')).pack(pady=10)
    tk.Button(root, text="Wii Theme", font=('Arial', 18), command=lambda: on_select('6')).pack(pady=10)

    root.mainloop()
