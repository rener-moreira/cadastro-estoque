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

def cadastrar(entrada_produto, entrada_cod, entrada_valor):
    conexao = conectar()
    cursor = conexao.cursor()
    exe_cadastro(cursor,entrada_produto, entrada_cod, entrada_valor)
    conexao.commit()
    fechar_conexao(conexao)
    fechar_cursor(cursor)

def exe_cadastro(cursor,entrada_produto, entrada_cod, entrada_valor):
    cursor.execute(
        "insert into estoque (produto, cod_produto, valor) values (%s, %s, %s)", (entrada_produto, entrada_cod, entrada_valor),
    )

def listar_produtos(cursor):
    cursor.execute(
        "Select * from estoque"
    )