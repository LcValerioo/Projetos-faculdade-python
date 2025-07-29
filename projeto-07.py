#Implementando bancos de dados com Python

#Sqlite3
'''
import sqlite3 as conector

#abertura de conexão
conexao = conector.connect("URL SQLite")

#Aquisição de um curso
cursor = conexao.cursor()

#Execução de comandos: SELECT...CREATE...
cursor.execute("...")
cursor.fetchall()

#Efetivação do comando 
conexao.commit()

#Fechamento das conexões
cursor.close()
conexao.close()
'''

#MySQL
'''
import mysql.connector as conector

#Abertura de conexão
conexao = conector.connect("URL MySQL")

#Aquisição de um cursor
cursor = conexao.cursor()

#Executa comandos: SELECT...CREATE...
cursor.execute()
cursor.fetchall()

#Efetivação do comando
conexao.commit()

#Fechamento das conexões
cursor.close()
conexao.close()
'''
#PSYCOPG2
'''
import psycopg2 as conector

#Abertura de conexão
conexao = conector.connect("URL PostegreSQL")

#Aquisição de um cursor
cursor = conexao.cursor()

#Executa comandos: SELECT...CREATE...
cursor.execute()
cursor.fetchall()

#Efetivação do comando
conexao.commit()

#Fechamento das conexões
cursor.close()
conexao.close()
'''

#Criando tabelas no SGBD com Python
#Implementando a tabela Pessoa
"""
import sqlite3 as conector

try:
    #Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    
    #Execução do comando: SELECT...CREATE...
    comando = '''CREATE TABLE Pessoa (
                    cpf INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY (cpf)
                    );'''
    
    cursor.execute(comando)


    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro de Banco de dados {err}")

finally:
    #Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
"""
#Implementando a tabela Marca
"""
import sqlite3 as conector

try:
    #Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #Execução do comando: SELECT...CREATE...
    comando = '''CREATE TABLE Marca (
                    id INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                    );'''
    
    cursor.execute(comando)

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro de Banco de dados {err}")

finally:
    #Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
"""
#Implementando a tabela Veiculo

"""
import sqlite3 as conector

try:
    #Abertura de conexão e aquisição de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #Execução do comando: SELECT...CREATE...
    comando = '''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano INTEGER NOT NULL,
                cor TEXT NOT NULL,
                proprietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa),
                FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES Marca(id)
                );'''

    cursor.execute(comando)
    
    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro de Banco de dados {err}")

finally:
    #Fechamento das conexões
    if conexao:
        cursor.close()
        conexao.close()
"""

#Inserindo novos elementos na tabela
"""
import sqlite3 as conector

try: 
    #Abertura de conexão e criação de cursor
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #Execução de um comando
    comando = '''ALTER TABLE Veiculo
                    ADD motor REAL;'''
    
    cursor.execute(comando)

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro de Banco de dados {err}")

finally:
    #Fechamento das conexões
    cursor.close()
    conexao.close()
"""

#Excluindo tabelas
"""
import sqlite3 as conector

try:
    #Abertura de conexões
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    #Executando o comando DROP
    comando1 = '''DROP TABLE Veiculo;'''

    cursor.execute(comando1)

    comando2 = '''CREATE TABLE Veiculo (
                    placa CHARACTER(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    proprietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY (placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id));''')

    cursor.execute(comando2)

    conexao.commit()

except conector.DatabaseError as err:
        print(f"Erro de Banco de dados {err}")
    
finally:
    cursor.close()
    conexao.close()
"""
