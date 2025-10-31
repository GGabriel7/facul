import tkinter as tk
from tkinter import ttk
from AppBD import AppBD

class PrincipalBD:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Gerenciador de Produtos")
        
        # Componetes da interface
        self.label_id = tk.Label(root, text="CÓDIGO")
        self.label_id.grid(row=0, column=0)
        self.text_id = tk.Entry(root)
        self.text_id.grid(row=0, column=1)
        
        self.label_nome = tk.Label(root, text="NOME")
        self.label_nome.grid(row=1, column=0)
        self.text_nome = tk.Entry(root) 
        self.text_nome.grid(row=1, column=1)
        
        self.label_preco = tk.Label(root, text="PREÇO")
        self.label_preco.grid(row=2, column=0)
        self.text_preco = tk.Entry(root)
        self.text_preco.grid(row=2, column=1)
        
        # BOTÕES
        self.btn_cadastrar = tk.Button(root, text="CADASTRAR", command=self.fCadastroProduto)
        self.btn_cadastrar.grid(row=3, column=0, pady=10, padx=10)
        
        self.btn_alterar = tk.Button(root, text="ALTERAR", command=self.fAlterarProduto)
        self.btn_alterar.grid(row=3, column=1, pady=10, padx=10)
        
        self.btn_deletar = tk.Button(root, text="DELETAR", command=self.fDeletarProduto)
        self.btn_deletar.grid(row=4, column=0, pady=10, padx=10)
        
        self.btn_limpar = tk.Button(root, text="LIMPAR", command=self.fLimparCampos)
        self.btn_limpar.grid(row=4, column=1, pady=10, padx=10)
        
        # TABELA
        self.tree = ttk.Treeview(root, columns=("CODIGO", "NOME", "PRECO"), show='headings')
        self.tree.heading("CODIGO", text="CÓDIGO")
        self.tree.heading("NOME", text="NOME")
        self.tree.heading("PRECO", text="PREÇO")
        self.tree.grid(row=5, column=0, columnspan=2)
        self.tree.bind("<ButtonRelease-1>", self.apresentarRegistrosSelecionados)
        
        self.carregarDadosIniciais()
        
    def fCadastroProduto(self):
        codigo = self.text_id.get()
        nome = self.text_nome.get()
        preco = self.text_preco.get()
        
        self.db.inserir_dados(nome, preco)
        self.tree.insert("", "end", values=(codigo, nome, preco))
        self.fLimparCampos()
        
    def fAlterarProduto(self):
        codigo = self.text_id.get()
        nome = self.text_nome.get()
        preco = self.text_preco.get()
        
        self.db.atualizar_dados(codigo, nome, preco)
        self.fLimparCampos()
        self.carregarDadosIniciais()
        
    def fDeletarProduto(self):
        codigo = self.text_id.get()
        self.db.deletar_dados(codigo)
        self.fLimparCampos()
        self.carregarDadosIniciais()
        
    def fLimparCampos(self):
        self.text_id.delete(0, tk.END)
        self.text_nome.delete(0, tk.END)
        self.text_preco.delete(0, tk.END)
        
    def apresentarRegistrosSelecionados(self, event):
        item  = self.tree.selection()[0]
        valores = self.tree.item(item, "values")
        self.text_id.delete(0, tk.END)
        self.text_id.insert(tk.END, valores[0])
        self.text_nome.delete(0, tk.END)
        self.text_nome.insert(tk.END, valores[1])
        self.text_preco.delete(0, tk.END)
        self.text_preco.insert(tk.END, valores[2])
        
    def carregarDadosIniciais(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        registros = self.db.selecionar_dados()
        
        for registro in registros:
            self.tree.insert("", "end", values=registro)
            
# criando a interface gráfica
root = tk.Tk()
db = AppBD()
app = PrincipalBD(root, db)
root.mainloop()