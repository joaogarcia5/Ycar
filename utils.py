import tkinter as tk

def centralizar_janela(root, largura, altura):
    """
    Centraliza a janela `root` com as dimensões especificadas.
    """
    tela_largura = root.winfo_screenwidth()
    tela_altura = root.winfo_screenheight()
    
    # Calcula a posição x e y para centralizar a janela
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    
    # Define o tamanho e a posição da janela
    root.geometry(f"{largura}x{altura}+{x}+{y}")
