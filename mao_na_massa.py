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

#Implementando a atualização de dados
def atualizar_dado(conexao):
    print("\n-- Atualizar --")
    print("1. Livro")
    print("2. Cliente")
    print("3. Pedido")
    tipo = input("Escolha o tipo para atualizar: ")

    cursor = conexao.cursor()

    if tipo == '1':
        id_livro = int(input("ID do livro a atualizar: "))
        novo_titulo = input("Novo título: ")
        novo_autor = input("Novo autor: ")
        novo_preco = float(input("Novo preço: "))
        cursor.execute('UPDATE Livros SET titulo = ?, autor = ?, preco = ? WHERE id = ?',
                       (novo_titulo, novo_autor, novo_preco, id_livro))

    elif tipo == '2':
        id_cliente = int(input("ID do cliente a atualizar: "))
        novo_nome = input("Novo nome: ")
        novo_email = input("Novo e-mail: ")
        cursor.execute('UPDATE Clientes SET nome = ?, email = ? WHERE id = ?',
                       (novo_nome, novo_email, id_cliente))

    elif tipo == '3':
        id_pedido = int(input("ID do pedido a atualizar: "))
        novo_cliente = int(input("Novo ID do cliente: "))
        novo_livro = int(input("Novo ID do livro: "))
        nova_qtd = int(input("Nova quantidade: "))
        nova_data = input("Nova data (YYYY-MM-DD): ")
        cursor.execute('''UPDATE Pedidos SET cliente_id = ?, livro_id = ?, quantidade = ?, data_pedido = ? 
                          WHERE id = ?''',
                       (novo_cliente, novo_livro, nova_qtd, nova_data, id_pedido))
    
    else:
        print("Opção inválida de tipo.")
        return

    conexao.commit()
    cursor.close()
    print("Atualização concluída com sucesso!")

#Implementando a exclusão de dados
def excluir_dado(conexao):
    print("\n-- Excluir --")
    print("1. Livro")
    print("2. Cliente")
    print("3. Pedido")
    tipo = input("Escolha o tipo para excluir: ")

    cursor = conexao.cursor()

    if tipo == '1':
        id_livro = int(input("ID do livro a excluir: "))
        cursor.execute('DELETE FROM Livros WHERE id = ?', (id_livro,))
    elif tipo == '2':
        id_cliente = int(input("ID do cliente a excluir: "))
        cursor.execute('DELETE FROM Clientes WHERE id = ?', (id_cliente,))
    elif tipo == '3':
        id_pedido = int(input("ID do pedido a excluir: "))
        cursor.execute('DELETE FROM Pedidos WHERE id = ?', (id_pedido,))
    else:
        print("Opção inválida de tipo.")
        return

    conexao.commit()
    cursor.close()
    print("Exclusão realizada com sucesso!")

if __name__ == '__main__':
    conexao = conectar_banco("livraria.db")
    criar_tabelas(conexao)
    
    while True:
        print("\n=== MENU ===")
        print("1. Inserir Livro")
        print("2. Inserir Cliente")
        print("3. Inserir Pedido")
        print("4. Exibir Pedidos")
        print("5. Atualizar Dados")
        print("6. Excluir Dados")
        print("7. Sair")

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
            atualizar_dado(conexao)
        elif escolha == '6':
            excluir_dado(conexao)
        elif escolha == '7':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conexao.close()

    print("---FIM DO PROGRAMA---")

    conexao.close()
"""
"""
import psycopg2
from psycopg2 import Error

def connect_to_db():
    try:
        #Conectar ao banco de dados
        connection = psycopg2.connect(
            host='localhost',
            database='postgresDB',
            user='admin',
            passowrd='admin123'
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar no Banco de Dados PostgreSQL: {e}")
        return None
    
def create_table():
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS public."AGENDA"
            (
                id integer NOT NULL,
                nome text COLLATE pg_catalog."default" NOT NULL,
                telefone char(12) COLLATE pg_catalog."default" NOT NULL
            )
            TABLESPACE pg_default;
            ALTER TABLE public."AGENDA"
                OWNER to admin;
                    ''')
            conn.commit()
        except Error as e:
            print(f"Erro ao criar Tabela: {e}")
        finally:
            cursor.close()
            conn.close()

    
def create_contact(nome, telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            INSERT INTO public."AGENDA" (nome, telefone)
            VALUES (%s,%s) RETURNING id;
            ''', (nome, telefone))
            contact_id = cursor.fetchone()[0]
            conn.commit()
            print(f"Contato adicionado com ID: {contact_id}")
        except Error as e:
            print(f"Erro ao adicionar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def read_contacts():
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            SELECT id, nome, telefone FROM public."AGENDA";
            ''')
            contacts = cursor.fetchall()
            for contact in contacts:
                print(f"ID: {contact[0]}, Nome: {contact[1]}, Telefone: {contact[2]}")
        except Error as e:
            print(f"Erro ao ler contatos: {e}")
        finally:
            cursor.close()
            conn.close()

def update_contact(contact_id, novo_nome, novo_telefone):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            UPDATE public."AGENDA"
            SET nome = %s, telefone = %s
            WHERE id = %s;
            ''', (novo_nome, novo_telefone, contact_id))
            conn.commit()
            print(f"Contado atualizado com Sucesso!")
        except Error as e:
            print(f"Erro ao atualizar contato: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_contact(contact_id):
    conn = connect_to_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute('''
            DELETE FROM public."AGENDA"
            WHERE id = %s;
            ''', (contact_id))
            conn.commit()
            print(f"Contato deletado com Sucesso!")
        except Error as e:
            print(f"Erro ao excluir contato: {e}")
        finally:
            cursor.close()
            conn.close()

def main():
    create_table()

    while True:
        print("\nMenu:")
        print("1. Adicionar novo contato")
        print("2. Mostrar todos os contatos")
        print("3. Atualizar um contato")
        print("4. Deletar um contato")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        #A partir do python 3.10 é possivel utilizar o match/case
        if choice == '1':
            nome = input("Digite um Nome: ")
            telefone = input("Digite um telefone: ")
            create_contact(nome, telefone)
        elif choice == '2':
            read_contacts()
        elif choice == '3':
            contact_id = int(input("Digite o ID do contato para atualizar: "))
            novo_nome = input("Novo Nome: ")
            novo_telefone = input("Novo Telefone: ")
            update_contact(contact_id, novo_nome, novo_telefone)
        elif choice == '4':
            contact_id = int(input("Digite o ID do contato para Deletar: "))
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção invalida. Por Favor, tente novamente.")

if __name__ == '__main__':
    main()
"""