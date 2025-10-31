import tkinter as tk
from tkinter import ttk
import pandas as pd

janela = tk.Tk() # Cria a janela principal da aplicação
janela.title("Sistema de Gestão Escolar")
janela.geometry("800x400")

# Label e campo de entrada para o nome do aluno, nota 1 e nota 2
tk.Label(janela, text="Nome do Aluno:").pack() 
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Nota 1:").pack()
entrada_nota1 = tk.Entry(janela)
entrada_nota1.pack()

tk.Label(janela, text="Nota 2:").pack()
entrada_nota2 = tk.Entry(janela)
entrada_nota2.pack()

# Cria a tabela para exibir os dados dos alunos
tabela = ttk.Treeview(janela, columns=("Nome", "Nota1", "Nota2", "Média", "Situação"), show="headings")
tabela.heading("Nome", text="Nome do Aluno")
tabela.heading("Nota1", text="Nota 1")
tabela.heading("Nota2", text="Nota 2")
tabela.heading("Média", text="Média")
tabela.heading("Situação", text="Situação")
tabela.pack(pady=10)

# Tabela de rolagem
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

alunos_iniciais = [
    ("Ana Silva", 8.5, 7.0),
    ("Bruno Souza", 6.0, 5.5),
    ("Carla Dias", 9.0, 8.5),
    ("Diego Lima", 4.5, 6.0)
]

for aluno in alunos_iniciais:
    nome, nota1, nota2 = aluno
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.1f}", situacao))
    
def cadastro_aluno():
    nome = entrada_nome.get()
    try:
        nota1 = float(entrada_nota1.get())
        nota2 = float(entrada_nota2.get())
    except ValueError:
        tk.messagebox.showerror("Erro", "Notas devem ser números.")
        return

    media = (nota1 + nota2) / 2
    
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.1f}", situacao))
    entrada_nome.delete(0, tk.END)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)

# Botão para cadastrar aluno
tk.Button(janela, text="Cadastrar", command=cadastro_aluno).pack()

janela.mainloop()