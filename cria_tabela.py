#Bibliotecas que serão utilizadas
#pip install psycopg2
#pip install faker
#pip install tk

import psycopg2 

#Criar conexão
conexao = psycopg2.connect(
    database = "postegresDB", 
    user = "admin",
    password = "admin1234",
    host = "127.0.0.1",
    port = "5432"
)
print("Conexão com o Banco de Dados aberta com sucesso!")

#Criando o cursor
cursor = conexao.cursor()

if __name__ == '__main__':
    #Criação da tabela produto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PRODUTO (
                CODIGO SERIAL PRIMARY KEY,
                NOME VARCHAR(100) NOT NULL,
                PRECO NUMERIC(10,2)NOT NULL);
    ''')

    #just in case
    conexao.commit()
    print("Tabela criada com Sucesso!")

    conexao.close()