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