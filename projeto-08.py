"""
import sqlite3 as conector

#Criando função para conectar ao banco de dados
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

#Criando as tabelas
def criar_tabelas(conexao):
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Locais (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   endereco TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Eventos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   data TEXT NOT NULL,
                   local_id INTEGER NOT NULL,
                   FOREIGN KEY(local_id) REFERENCES Locais(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Participantes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   evento_id INTEGER NOT NULL,
                   FOREIGN KEY(evento_id) REFERENCES Eventos(id))''')
    
    conexao.commit()

if __name__ == '__main__':
    conexao = conectar_banco('eventos.db')
    criar_tabelas(conexao)
    conexao.close()
"""

"""
import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("banco_alternativo.db")
cursor = conexao.cursor()

# Execução de um comando: SELECT... CREATE ...
comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
      VALUES (12345678900, 'João', '2000-01-31', 1);'''

cursor.execute(comando)

# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
"""
"""
import sqlite3 as conector
from modelo import Pessoa
try:
    #Abertura da conexão e criação do conector
    conexao = conector.connect("banco_alternativo.db")
    cursor = conexao.cursor()
    
    #Criação de um objeto do tipo Pessoa
    pessoa = Pessoa(60120519875, 'Lavinia', '2005-04-21', False)

    #Definição do comando com query parameter
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);'''
    cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro de Banco de dados {err}")

finally:
    #Fechamento das conexões
    cursor.close()
    conexao.close()
"""
"""
import sqlite3 as conector
from modelo import Pessoa, Marca, Veiculo


try:
    #Abertura da conexão e criação do cursor
    conexao = conector.connect("banco_alternativo.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    
    #Criação de um objeto do tipo Pessoa
    pessoa = Pessoa(30000000099, 'Silva', '1990-03-30', True)

    #Definição de um comando com query parameter
    comando1 = '''INSERT INTO Pessoa VALUES (:cpf,:nome,:data_nascimento,:usa_oculos);'''
    cursor.execute(comando1, vars(pessoa))
    print(vars(pessoa))
    
    # Inserção de dados na tabela Marca
    comando1 = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''

    marca1 = Marca(1, "Lamborghini", "LG")
    cursor.execute(comando1, vars(marca1))
    marca1.id = cursor.lastrowid
    veiculo1 = Veiculo("DEU2020", 2011, "Orange", 6.5, 25745019652, marca1.id)
    veiculo2 = Veiculo("PUN777", 2010, "Black", 5.2, 45420519860, marca1.id)
    veiculo3 = Veiculo("BEE4R22", 2017, "Silver", 5.5, 45420519875, marca2.id)
    veiculo4 = Veiculo("MUAHAHA", 2012, "Yellow", 5.2, 30000000099, marca2.id)
    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))
    cursor.execute(comando2, vars(veiculo4))

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro de Banco de Dados {err}")

finally: 
    #Fechamento das conexões
    cursor.close()
    conexao.close()

"""

#Atualização de um dado em uma tabela
"""
import sqlite3 as conector

try:
    # Abertura de conexão e aquisição de cursor
    conexao = conector.connect("banco_alternativo.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    # Definição dos comandos

    comando2 = '''UPDATE Pessoa SET oculos= ? WHERE cpf=30000000099;'''
    cursor.execute(comando2, (False,))

    comando3 = '''UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;'''
    cursor.execute(comando3, {"usa_oculos": True, "cpf": 25745019652})

    #Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro de Banco de Dados {err}")

finally:
    #Fechando as conexões
    cursor.close()
    conexao.close()

"""
#Remoção de dados de uma tabela
"""
import sqlite3 as conector

try:
    conexao = conector.connect("banco_alternativo.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    #Definição do comando DELETE
    comando = '''DELETE FROM Pessoa WHERE cpf= 60120519875;'''
    cursor.execute(comando)

    #Efetivação do comando 
    conexao.commit()

except conector.DatabaseError as err:
    print(f"Erro no Banco De Dados {err}")

finally:
    #Fechando conexões
    cursor.close()
    conexao.close()
"""

#Seleção de registros de uma tabela
"""
import sqlite3 as conector

try:
    #Abertura das conexões 
    conexao = conector.connect("banco_alternativo.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    #Definição dos registros
    cursor.execute('''SELECT nome, oculos FROM Pessoa''')

    #Recuperação de dados
    registros = cursor.fetchall()
    print("Tipo retornado pelo fetchall: ", type(registros))

    for registro in registros:
        print("Tipo:", type(registro), "- Conteúdo: ", registro)

except conector.DatabaseError as err:
    print(f"Deu ruim fiote no BD {err}")

finally:
    #Fechando as conexões
    cursor.close()
    conexao.close()
"""

#Vamos criar agora uma consulta para retornar às pessoas que usam óculos
"""
import sqlite3 as conector
from modelo import Pessoa

try:
    #Abertura das conexões
    conexao = conector.connect("banco_alternativo.db", detect_types=conector.PARSE_DECLTYPES)
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()
    '''
    #Funções conversoras
    def conv_bool(dado):
        return True if dado == 1 else False
    
    #Registro de conversores
    conector.register_converter("BOOLEAN", conv_bool)
    '''

    #Definição dos comandos
    cursor.execute('''SELECT * FROM Pessoa WHERE oculos=:usa_oculos''', {"usa_oculos": True})

    #Recuperação dos registros
    registros = cursor.fetchall()
    for registro in registros:
        pessoa = Pessoa(*registro)
        print("CPF:", type(pessoa.cpf), pessoa.cpf)
        print("Nome:", type(pessoa.nome), pessoa.nome)
        print("Nascimento:", type(pessoa.data_nascimento), pessoa.data_nascimento)
        print("Oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)
        print("\n")


except conector.DatabaseError as err:
    print(f"Deu Ruim ai no Seu BD {err}")

finally:
    #Fechando as conexões
    cursor.close()
    conexao.close()
"""

#Seleção de registro utilizando o JOIN
"""
import sqlite3 as conector
from modelo import Veiculo, Marca

try:
    #Abertura das conexões
    conexao = conector.connect("banco_alternativo.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    #Definindo os comandos
    cursor.execute('''SELECT Veiculo.placa, Veiculo.ano, Veiculo.cor, Veiculo.motor, Veiculo.proprietario, Marca.nome 
                    FROM Veiculo 
                    JOIN Marca ON Marca.id = Veiculo.marca''')
    
    print("Este é um método para exibir os dados de interesse: \n")

    #Recuperação dos registros
    reg_veiculos = cursor.fetchall()
    for reg_veiculo in reg_veiculos:
        veiculo = Veiculo(*reg_veiculo)
        print(f"Placa: {veiculo.placa}, Marca: {veiculo.marca}")

    print("\nEsta é outra maneira de aprensetar os dados de interesse: \n")

    #Definição de comandos
    cursor.execute('''SELECT * FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca''')

    #Recuperação dos registros
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        print(f"Placa: {veiculo.placa}, Marca: {veiculo.marca.nome}")
    

except conector.DatabaseError as err:
    print(f"Deu problema no seu BD chefe {err}")

finally:
    #Fechando as conexões
    cursor.close()
    conexao.close()
"""

#Seleção de registros relacionados
"""
import sqlite3 as conector
from modelo import Pessoa
from script19_4 import recuperar_veiculos

try:

    #Abertura das conexões
    conexao = conector.connect("banco_alternativo.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    #Definição de comandos
    cursor.execute('''SELECT * FROM Pessoa''')

    #Recuperação dos registros
    pessoas = []
    reg_pessoas = cursor.fetchall()
    for reg_pessoa in reg_pessoas:
        pessoa = Pessoa(*reg_pessoa)
        pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
        pessoas.append(pessoa)

    for pessoa in pessoas:
        print(pessoa.nome)
        for veiculo in pessoa.veiculos:
            print(veiculo.placa, veiculo.marca.nome)
            print("\t")

except conector.DatabaseError as err:
    print(f"Ops ! Parece que deu errado o BD {err}")

finally:
    #Fechando as conexões
    cursor.close()
    conexao.close()
"""