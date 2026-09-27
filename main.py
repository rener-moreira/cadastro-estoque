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
mensagem.grid(row=11, column=0, columnspan=2, padx=15, pady=15)

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
                text="Itens do estoque listados"
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
botao_mostrar.grid(row=6, column=0,padx=5, pady=10)

#Limpar tela
def limpar():
    entrada_produto.delete(0, tk.END)
    entrada_cod.delete(0, tk.END)
    entrada_valor.delete(0, tk.END)
    mostrar.delete(0, tk.END)
    pnome_pesquisa.delete(0, tk.END)
    pid_pesquisa.delete(0, tk.END)
    pvalor_pesquisa.delete(0, tk.END)

    mensagem.configure(text="Tela limpa com sucesso!!")

botao_limpar = tk.Button(
     janela,
     text="Limpar",
     font=("Arial", 15),
     command=limpar
)
botao_limpar.grid(row=6, column=1,padx=5, pady=10)

#Pesquisar produtos

def executar_pesquisa():
     nome1 = pnome_pesquisa.get()
     cod1 = pid_pesquisa.get()
     valor1 = pvalor_pesquisa.get()

     produtos = pesquisar(nome1, cod1, valor1)
     mostrar.delete(0, tk.END)
     
     for produtos in produtos:
        mostrar.insert(tk.END, produtos)
        
     mensagem.configure(
           text="Itens do estoque listados"
        )
     


produto_pesquisa = tk.Label(
     janela,
     text="Nome do Produto",
     font=("Times Roman", 10)
)
produto_pesquisa.grid(row=7, column=0, padx=5, pady=5)

id_pesquisa = tk.Label(
     janela,
     text="Id do Produto",
     font=("Times Roman", 10)
)
id_pesquisa.grid(row=8, column=0, padx=5, pady=5)


valor_pesquisa = tk.Label(
     janela,
     text="Valor do Produto",
     font=("Times Roman", 10)
)
valor_pesquisa.grid(row=9, column=0, padx=5, pady=5)

pnome_pesquisa = tk.Entry(janela) 
pid_pesquisa = tk.Entry(janela) 
pvalor_pesquisa = tk.Entry(janela) 


pnome_pesquisa.grid(row=7,column=1)
pid_pesquisa.grid(row=8,column=1)
pvalor_pesquisa.grid(row=9,column=1)

botao_pesquisa = tk.Button(
     janela,
     text="Pesquisar",
     font=("Arial", 15),
     command=executar_pesquisa
)
botao_pesquisa.grid(row=10, column=0, columnspan=2)


janela.mainloop()


#Proximos Passos: Caixa para mostrar os produtos cadastrados. 
#Pesquisas por nome produtos, codigo e valor (um dos tres)