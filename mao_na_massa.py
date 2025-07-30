#Esse é um modelo de Banco de Dados para gerenciar um E-Commerce utilizando o Pyhton e o SQLite3

import sqlite3 as conector

#Implementando a conexão ao banco de dados
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

#Implementando as Tabelas
def criar_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   preco REAL NOT NULL,
                   estoque INTEGER NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente_id INTEGER NOT NULL,
                   produto_id INTEGER NOT NULL,
                   quantidade INTEGER NOT NULL,
                   data_pedido TEXT NOT NULL,
                   FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                   FOREIGN KEY (produto_id) REFERENCES Produtos(id))''')
    
    conexao.commit()
    cursor.close()

#Implementando dados nas tabelas
def inserir_dados(conexao):
    cursor = conexao.cursor()

    produtos = [('Notebook', 2999.99, 10),
                ('Smartphone', 1999.99, 20),
                ('Tablet', 999.99, 30)]
    
    clientes = [('Alice', 'alice@exemplo.com'),
                ('Bob', 'bob@exemplo.com'),
                ('Charlie', 'charlie@exemplo.com')]
    
    pedidos = [(1,1,2, '2025-07-28'),
               (2,2,1, '2025-07-29'),
               (3,3,3, '2025-07-30')]
    
    cursor.executemany('INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)
    cursor.executemany('INSERT INTO Clientes (nome, email) VALUES (?, ?)', clientes)
    cursor.executemany('INSERT INTO Pedidos (cliente_id, produto_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)', pedidos)

    conexao.commit()
    cursor.close()

if __name__ == '__main__':
    conexao = conectar_banco('ecommerce.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    conexao.close()