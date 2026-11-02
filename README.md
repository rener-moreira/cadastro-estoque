# 📦 Cadastro de Produtos

Aplicação desktop simples para **cadastro, listagem, limpeza e pesquisa de produtos**, desenvolvida em Python como projeto de prática de programação, interface gráfica e integração com banco de dados PostgreSQL.

## 🚀 Funcionalidades

- Cadastrar produtos no estoque
- Informar:
  - Nome do produto
  - Código do produto
  - Valor
- Listar produtos cadastrados
- Pesquisar produtos por:
  - Nome
  - Código
  - Valor
- Limpar os campos da tela
- Exibir mensagens de confirmação na interface
- Armazenar os dados em um banco de dados PostgreSQL

A interface gráfica foi desenvolvida com **Tkinter**, enquanto a comunicação com o PostgreSQL é feita utilizando **Psycopg**. As credenciais do banco são carregadas por meio de variáveis de ambiente com `python-dotenv`. 

## 🛠️ Tecnologias utilizadas

- **Python**
- **Tkinter**
- **PostgreSQL**
- **Psycopg**
- **python-dotenv**

## 📁 Estrutura do projeto

```text
cadastrar_produtos/
├── main.py
├── banco.py
├── .env
├── .gitignore
└── .venv/
```

### `main.py`

Responsável pela interface gráfica da aplicação.

Entre as funcionalidades presentes estão o cadastro, a listagem, a limpeza dos campos e a pesquisa dos produtos. 

### `banco.py`

Responsável pela comunicação com o PostgreSQL.

O arquivo possui funções para:

- Abrir e fechar conexão com o banco
- Cadastrar produtos
- Listar produtos
- Pesquisar produtos

A conexão utiliza as variáveis `DB_HOST`, `DB_NAME`, `DB_USER` e `DB_PASSWORD`. 

## 🗄️ Banco de dados

A aplicação utiliza uma tabela chamada `estoque`.

A estrutura utilizada pelo código possui as seguintes colunas:

```text
nome_produto
cod_produto
valor
```

O cadastro é realizado por meio de:

```sql
INSERT INTO estoque (nome_produto, cod_produto, valor)
VALUES (%s, %s, %s);
```

E as pesquisas utilizam consultas SQL com parâmetros, evitando a montagem direta dos valores dentro da consulta.

## ⚙️ Configuração

### 1. Clone o projeto

```bash
git clone URL_DO_REPOSITORIO
cd cadastrar_produtos
```

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install psycopg python-dotenv
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_NAME=cadastro_produto
DB_USER=postgres
DB_PASSWORD=sua_senha
```

> **Importante:** não publique o arquivo `.env` no GitHub. Ele deve permanecer no `.gitignore`.

### 5. Crie a tabela no PostgreSQL

Exemplo:

```sql
CREATE TABLE estoque (
    id SERIAL PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    cod_produto VARCHAR(50) NOT NULL,
    valor NUMERIC(10,2) NOT NULL
);
```

### 6. Execute o programa

```bash
python main.py
```

## 🔎 Como funciona a pesquisa

A função de pesquisa recebe três valores:

```python
pesquisar(nome, codigo, valor)
```

A pesquisa utiliza o primeiro campo preenchido:

```text
Nome preenchido  → pesquisa pelo nome
Código preenchido → pesquisa pelo código
Valor preenchido  → pesquisa pelo valor
```

As consultas são executadas no `banco.py`, mantendo a responsabilidade de conexão e acesso ao banco separada da interface gráfica.

## 🖥️ Interface

A aplicação possui uma interface gráfica criada com Tkinter, com campos para cadastro e pesquisa, além de botões para executar as operações. 

## 📚 Objetivo do projeto

Este projeto foi desenvolvido como prática de:

- Python
- Funções
- Condicionais
- Manipulação de entradas com Tkinter
- CRUD e operações com banco de dados
- SQL
- PostgreSQL
- Integração entre Python e banco de dados
- Organização de um projeto em arquivos separados
- Uso de variáveis de ambiente
- Git e GitHub


## 👨‍💻 Autor

**Rener Moreira**

Projeto desenvolvido para prática e evolução dos conhecimentos em Python, PostgreSQL e desenvolvimento de aplicações desktop.

**Contatos**
E-mail: renermoreiratecnico@gmail.com
GitHub: renermoreira

