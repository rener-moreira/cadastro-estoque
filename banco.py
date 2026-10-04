import psycopg
from dotenv import load_dotenv
import os 

load_dotenv()


def conectar():
    conexao = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")

    )
    return conexao

def fechar_conexao(conexao):
    conexao.close()
def fechar_cursor(cursor):
    cursor.close()

def fechar_conexao(conexao):
    conexao.close()
def fechar_cursor(cursor):
    cursor.close()

def cadastrar(entrada_produto, entrada_cod, entrada_valor):
    conexao = conectar()
    cursor = conexao.cursor()
    exe_cadastro(cursor,entrada_produto, entrada_cod, entrada_valor)
    conexao.commit()
    fechar_conexao(conexao)
    fechar_cursor(cursor)

def exe_cadastro(cursor,entrada_produto, entrada_cod, entrada_valor):
    cursor.execute(
         "insert into estoque (nome_produto, cod_produto, valor) values (%s, %s, %s)", (entrada_produto, entrada_cod, entrada_valor),
    )

def listar_produtos(cursor):
    cursor.execute(
        "SELECT cod_produto, nome_produto FROM estoque"
    )
    produtos = cursor.fetchall()
    return produtos

def buscar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    produtos = listar_produtos(cursor)
    fechar_cursor(cursor)
    fechar_conexao(conexao)
    return produtos

#função de pesquisa por código, valor e nome

def pesquisar(pnome_pesquisa, pid_pesquisa, pvalor_pesquisa):
    conexao = conectar()
    cursor = conexao.cursor()

    if pnome_pesquisa:
        cursor.execute(
                "SELECT cod_produto, nome_produto, valor FROM estoque WHERE nome_produto ILIKE %s", (pnome_pesquisa,)
            )
    elif pid_pesquisa:
        cursor.execute(
                "SELECT cod_produto, nome_produto, valor FROM estoque WHERE cod_produto = %s", (pid_pesquisa,)
            )
    elif pvalor_pesquisa:
        cursor.execute(
                "SELECT cod_produto, nome_produto, valor FROM estoque WHERE valor = %s", (pvalor_pesquisa,)
            )
    
    produtos = cursor.fetchall()

    fechar_cursor(cursor)
    fechar_conexao(conexao)
    
    return produtos


def deletar_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM estoque WHERE cod_produto = %s", (id,)
    )
    conexao.commit()

    fechar_cursor(cursor)
    fechar_conexao(conexao)
