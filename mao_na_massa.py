#Esse é um modelo de Banco de Dados para gerenciar um E-Commerce utilizando o Pyhton e o SQLite3
"""
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
"""

#Esse é um modelo de Banco de Dados para gerenciar uma Livraria utilizando o Pyhton e o SQLite3
"""
import sqlite3 as conector
from modelo import Livro, Cliente, Pedido

#Criando conexões
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    conexao.execute("PRAGMA foreign_keys = on")
    return conexao

#Implementando as tabelas
def criar_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   preco REAL NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cliente_id INTEGER NOT NULL,
                   livro_id INTEGER NOT NULL,
                   quantidade INTEGER NOT NULL,
                   data_pedido TEXT NOT NULL,
                   FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                   FOREIGN KEY (livro_id) REFERENCES Livros(id))''')
    
    conexao.commit()
    cursor.close()

#Inserindo os dados nas tabelas
def inserir_dados(conexao):
    cursor = conexao.cursor()

    livros = [Livro('Pyhton para iniciantes', 'John Doe', 39.99),
              Livro('Algoritmos e Estruturas de Dados', 'Jane Smith', 49.99),
              Livro('Inteligência Artificial', 'Alan Turing', 59.99)]
    
    clientes = [Cliente('Joshep', 'jo-shep@gmail.com'),
                Cliente('Yavanna', 'yava_verde@gmail.com'),
                Cliente('Melkor', 'senhorsombrio@yahoo.com')]
    
    pedidos = [Pedido(1,1,2, '2025-07-28'),
               Pedido(2,2,1, '2025-07-29'),
               Pedido(3,3,3, '2025-07-30')]
    
    # Inserindo livros
    cursor.executemany('INSERT INTO Livros (titulo, autor, preco) VALUES (?, ?, ?)',
                    [(livro.titulo, livro.autor, livro.preco) for livro in livros])

    # Inserindo clientes
    cursor.executemany('INSERT INTO Clientes (nome, email) VALUES (?, ?)',
                    [(cliente.nome, cliente.email) for cliente in clientes])

    # Inserindo pedidos
    cursor.executemany('INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) VALUES (?, ?, ?, ?)',
                    [(pedido.cliente_id, pedido.livro_id, pedido.quantidade, pedido.data_pedido) for pedido in pedidos])


    conexao.commit()
    cursor.close()

#Implementando a visualização dos pedidos
def exibir_pedidos(conexao):
    cursor = conexao.cursor()

    query = '''
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Livros ON Pedidos.livro_id = Livros.id
    '''
    cursor.execute(query)
    pedidos = cursor.fetchall()
    print('Pedidos: ')

    for pedido in pedidos:
        print(pedido)

#Implementando a Função Main
if __name__ == '__main__':
    conexao = conectar_banco("livraria.db")
    criar_tabelas(conexao)
    inserir_dados(conexao)
    exibir_pedidos(conexao)
    conexao.close()
"""

#Aqui deixamos o SGBD interativo
"""
import sqlite3 as conector
from modelo import Livro, Cliente, Pedido

#Criando conexões
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    conexao.execute("PRAGMA foreign_keys = on")
    return conexao

#Implementando livro pegando dados do teclado
def inserir_livro(conexao):
    titulo = input("Digite o título do Livro: ")
    autor = input("Digite o autor do livro: ")
    preco = float(input("Digite o valor do livro: "))

    cursor = conexao.cursor()
    cursor.execute('INSERT INTO Livros (titulo, autor, preco) VALUES (?, ?, ?)', (titulo, autor, preco))
    conexao.commit()
    cursor.close()
    print("Livro Inserido com Sucesso!")

#Implementando clientes pegando dados do teclado
def inserir_cliente(conexao):
    cursor = conexao.cursor()

    nome = input("Digite o Nome do Cliente: ")
    email = input("Digite o E-mail do cliente: ")

    cursor.execute('INSERT INTO Clientes (nome, email) VALUES (?, ?)', (nome, email))
    conexao.commit()
    cursor.close()
    print("Cliente inserido com Sucesso!")

#Implementando o pedido
def inserir_pedido(conexao):
    cursor = conexao.cursor()

    cliente_id = int(input("Digite o ID do CLiente: "))
    livro_id = int(input("Digite o ID do Livro: "))
    quantidade = int(input("DIgite a quantidade que deseja comprar: "))
    data_pedido = input("Digite a data do pedido (YYYY-MM-DD): ")

    cursor.execute('''INSERT INTO Pedidos (cliente_id, livro_id, quantidade, data_pedido) 
                    VALUES (?, ?, ?, ?)''', (cliente_id, livro_id, quantidade, data_pedido))
    
    conexao.commit()
    cursor.close()
    print("Pedido concluído com Sucesso")

    #Implementando a visualização dos pedidos
def exibir_pedidos(conexao):
    cursor = conexao.cursor()

    query = '''
    SELECT Pedidos.id, Clientes.nome, Livros.titulo, Pedidos.quantidade, Pedidos.data_pedido FROM Pedidos
    JOIN Clientes ON Pedidos.cliente_id = Clientes.id
    JOIN Livros ON Pedidos.livro_id = Livros.id
    '''
    cursor.execute(query)
    pedidos = cursor.fetchall()
    print('Pedidos: ')

    for pedido in pedidos:
        print(pedido)

if __name__ == '__main__':
    conexao = conectar_banco("livraria.db")
    
    while True:
        print("\n=== MENU ===")
        print("1. Inserir Livro")
        print("2. Inserir Cliente")
        print("3. Inserir Pedido")
        print("4. Exibir Pedidos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            inserir_livro(conexao)
        elif escolha == '2':
            inserir_cliente(conexao)
        elif escolha == '3':
            inserir_pedido(conexao)
        elif escolha == '4':
            exibir_pedidos(conexao)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("---FIM DO PROGRAMA---")

    conexao.close()
"""