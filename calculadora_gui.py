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

def criar_calculadora():
    def calcular(expressao):
        try:
            return eval(expressao)
        except Exception as e:
            return "Erro"

    def on_button_click(button, entry):
        current_text = entry.get()
        if button == "=":
            result = calcular(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, button)

    root = tk.Tk()
    root.title("Calculadora")

    largura = 300
    altura = 400
    centralizar_janela(root, largura, altura)  # Centraliza a janela da calculadora

    entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=4, justify='right')
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', 'C', '=', '+'
    ]

    row_val = 1
    col_val = 0
    for button in buttons:
        action = lambda x=button: on_button_click(x, entry)
        tk.Button(root, text=button, padx=20, pady=20, bd=4, fg="black", font=('Arial', 18),
                  command=action).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    root.mainloop()
