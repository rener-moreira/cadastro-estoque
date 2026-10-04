import tkinter as tk
from banco import *
from estilos import estilos

janela = tk.Tk()

janela.title("Cadastrar Produtos")


#Titulo 
title = tk.Label(
    janela, 
    text="Cadastro de Produtos",
    font=("Arial", 30,"bold")
)
title.grid(row=0, column=0, columnspan=2)

#Frames 
frame_cadastro = tk.LabelFrame(janela, text="Dados do Produto", font=(10))
frame_cadastro.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

frame_exibir = tk.LabelFrame( janela, text="Mostrar Produtos", font=(5))
frame_exibir.grid(row=2, column=0,padx=10, pady=10)

frame_pesquisa = tk.LabelFrame(janela, text="Pesquisar Produtos", font=(10))
frame_pesquisa.grid(row=2, column=1, padx=10, pady=10)

frame_excluir = tk.LabelFrame(janela, text="Excluir Produto", font=(10))
frame_excluir.grid(row=3, column=0,columnspan=2, padx=10, pady=10)

frame_mensagem = tk.LabelFrame(janela, text="Mensagem do Sistema", font="10")
frame_mensagem.grid(row=4, column=0,padx=20, pady=10, columnspan=2)

#Mensagem
mensagem = tk.Label(
    frame_mensagem,
    text="",
    font=("Arial", 15, "bold")
)
mensagem.grid(row=11, column=0, columnspan=2, padx=15, pady=15)

#Produto, COD, Valor, Data de Validade (posterior)

produto = tk.Label(
    frame_cadastro,
    text="Produto: ",
    font=("Arial", 15)
)
produto.grid(row=1, column=0, padx=5, pady=5)

cod_pro = tk.Label(
    frame_cadastro, 
    text="Código do Produto:",
    font=("Arial", 15)
)
cod_pro.grid(row=2, column=0, padx=5, pady=5)

valor = tk.Label(
    frame_cadastro,
    text="Valor",
    font=("Arial", 15)
)
valor.grid(row=3, column=0, padx=5, pady=5)

entrada_produto = tk.Entry(frame_cadastro)
entrada_cod = tk.Entry(frame_cadastro)
entrada_valor = tk.Entry(frame_cadastro)

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
    frame_cadastro,
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


mostrar = tk.Listbox(frame_exibir)
mostrar.grid(row=5, column=0, columnspan=2, padx=20)

botao_mostrar = tk.Button(
     frame_exibir,
     text="Listar",
     font=("Arial", 15),
     command=listar
)
botao_mostrar.grid(row=6, column=0)

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
     frame_exibir,
     text="Limpar",
     font=("Arial", 15),
     command=limpar
)
botao_limpar.grid(row=6, column=1)

#Pesquisar produtos

def executar_pesquisa():
     nome1 = pnome_pesquisa.get()
     cod1 = pid_pesquisa.get()
     valor1 = pvalor_pesquisa.get()

     if nome1 != "" or cod1 != "" or valor1 != "":
        try:
            produtos = pesquisar(nome1, cod1, valor1)
            mostrar.delete(0, tk.END)
     
            for produto in produtos:
                mostrar.insert(tk.END, produto)

            mensagem.configure(text="Itens do estoque listados")

        except psycopg.ProgrammingError:
           mensagem.configure(text="Erro de Consulta")

     else:
        mensagem.configure(
            text="Digite em ao menos um dos campos!"
            )
        mostrar.delete(0, tk.END)
     
produto_pesquisa = tk.Label(
     frame_pesquisa,
     text="Nome do Produto",
     font=("Times Roman", 10)
)
produto_pesquisa.grid(row=7, column=0, padx=5, pady=5)

id_pesquisa = tk.Label(
     frame_pesquisa,
     text="Id do Produto",
     font=("Times Roman", 10)
)
id_pesquisa.grid(row=8, column=0, padx=5, pady=5)

valor_pesquisa = tk.Label(
     frame_pesquisa,
     text="Valor do Produto",
     font=("Times Roman", 10)
)
valor_pesquisa.grid(row=9, column=0, padx=5, pady=5)

pnome_pesquisa = tk.Entry(frame_pesquisa) 
pid_pesquisa = tk.Entry(frame_pesquisa) 
pvalor_pesquisa = tk.Entry(frame_pesquisa) 

pnome_pesquisa.grid(row=7,column=1, padx=5, pady=10)
pid_pesquisa.grid(row=8,column=1, padx=5)
pvalor_pesquisa.grid(row=9,column=1, padx=5, pady=10)

botao_pesquisa = tk.Button(
     frame_pesquisa,
     text="Pesquisar",
     font=("Arial", 15),
     command=executar_pesquisa
)
botao_pesquisa.grid(row=10, column=0, columnspan=2, padx=20, pady=20)


#Excluir Produto


def excluir_pro():
    id_produto = entrada_produto1.get()

    if id_produto == "":
        mensagem.configure(
            text="Digite o Código do produto para ser excluído"
        )
    else: 
        id_convert = int(id_produto)
        deletar_produto(id_convert)
        mensagem.configure(
            text="Produto Removido, por favor verifique o estoque novamente"
        )

id_label = tk.Label(
    frame_excluir,
    text="Id do Produto:",
    font=("Times Roman", 10)
)
id_label.grid(row=0, column=0, sticky="ew")


entrada_produto1 = tk.Entry(frame_excluir, width=20)
entrada_produto1.grid(row=1, column=0, padx=20, pady=10)

botao_excluir = tk.Button(
    frame_excluir,
    text="Excluir Produto",
    command=excluir_pro
) 
botao_excluir.grid(row=2, column=0, columnspan=2, pady=10, padx=20)

janela.mainloop()
