import tkinter as tk
from banco import *

janela = tk.Tk()

janela.title("Cadastrar Produtos")


#Titulo 
title = tk.Label(
    janela, 
    text="Cadastro de Produtos",
    font=("Arial", 30,"bold")
)
title.grid(row=0, column=0, columnspan=2)

#Mensagem
mensagem = tk.Label(
    janela,
    text="",
    font=("Arial", 15, "bold")
)
mensagem.grid(row=7, column=0, columnspan=2, padx=15, pady=15)

#Produto, COD, Valor, Data de Validade (posterior)

produto = tk.Label(
    janela,
    text="Produto: ",
    font=("Arial", 15)
)
produto.grid(row=1, column=0, padx=5, pady=5)

cod_pro = tk.Label(
    janela, 
    text="Código do Produto:",
    font=("Arial", 15)
)
cod_pro.grid(row=2, column=0, padx=5, pady=5)

valor = tk.Label(
    janela,
    text="Valor",
    font=("Arial", 15)
)
valor.grid(row=3, column=0, padx=5, pady=5)

entrada_produto = tk.Entry(janela)
entrada_cod = tk.Entry(janela)
entrada_valor = tk.Entry(janela)
entrada_produto.grid (row=1, column=1, padx=5, pady=5)
entrada_cod.grid(row=2, column=1, padx=5, pady=5)
entrada_valor.grid(row=3, column=1, padx=5, pady=5)

#Botao

def cadastrar1():
    pro = entrada_produto.get()
    cod = entrada_cod.get()
    valor_pro = entrada_valor.get()

    if pro == "":
        mensagem.configure(text="Preencha o nome do produto")
    elif cod == "":
        mensagem.configure(text="Preencha o código do produto")
    elif valor_pro == "":
            mensagem.configure(text="Preencha o valor do produto")
    else: 
        cadastrar(pro, cod, valor_pro)
        mensagem.configure(text="Produto cadastrado com sucesso!!")

botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar",
    font=("Arial", 15),
    command=cadastrar1
)
botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

#Mostrar Produtos

def listar():
     produtos = buscar_produtos()
     mostrar.delete(0, tk.END)

     for produtos in produtos:
            mostrar.insert(tk.END, produtos)
            mensagem.configure(
                text="Itans do estoque listados"
            )


mostrar = tk.Listbox(
     janela
)
mostrar.grid(row=5, column=0, columnspan=2)


botao_mostrar = tk.Button(
     janela,
     text="Listar",
     font=("Arial", 15),
     command=listar
)
botao_mostrar.grid(row=6, column=0, columnspan=2,  padx=10, pady=10)



janela.mainloop()


#Proximos Passos: Inserir entry de valor. Caixa para mostrar os produtos cadastrados. 
#Pesquisas por nome produtos, codigo e valor (um dos tres)