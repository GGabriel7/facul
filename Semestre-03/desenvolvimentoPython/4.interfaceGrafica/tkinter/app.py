import tkinter as tk
from tkinter import messagebox

def submit():
    # Recupera os dados dos campos de entrada
    nome = nome_entry.get() # Obtém o texto do campo de nome
    email = email_entry.get() # Obtém o texto do campo de email
    
    linguagem_preferida = linguagem_var.get() # Obtém a linguagem preferida selecionada
    
    # Imprime os dados no console
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Linguagem Preferida: {linguagem_preferida}")
    print("-=" * 15)
    
    # mostra uma caixa de mensagem com os dados
    messagebox.showinfo(
        "dados enviados",
        f"Nome: {nome}\nE-mail: {email}\nLinguagem Preferida: {linguagem_preferida}"
    ) 
    

# Cria a janela principal
root = tk.Tk()
root.title("Formulário Simples")

# Cria um frame para conter os widgets
frame = tk.Frame(root)
frame.pack(padx=80, pady=200)

# Label para o campo de email e nome
email_label = tk.Label(frame, text="E-mail:")
email_label.grid(row=1, column=0, padx=5, pady=5)

nome_entry = tk.Entry(frame, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

# Campo de entrada para o nome e email
nome_label = tk.Label(frame, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5)

email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Variavel para armazenar a linguagem preferida
linguagem_var = tk.StringVar(value="Python") # Valor padrão é Python

# Radiobuttons para selecionar a linguagem preferida
python_radio = tk.Radiobutton(frame, text="Python", variable=linguagem_var, value="Python")
python_radio.grid(row=2, column=0, padx=5, pady=5)
java_radio = tk.Radiobutton(frame, text="Java", variable=linguagem_var, value="Java")
java_radio.grid(row=2, column=1, padx=5, pady=5)

# Botão de submissão/envio
submit_button = tk.Button(frame, text="Enviar", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()