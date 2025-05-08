import os

print("Abrindo um arquivo")

'''
try:
    open("teste.pdf", "w", encoding="utf-8")
    print("Arquivo Aberto!")
except FileNotFoundError as erro:
    print("Arquivo Inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição", erro)
'''
'''
try:
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Permissão negada.")
except Exception as e:
    print(f"Erro inesperado: {e}")
'''
'''
#Utilizando a função Rename
nome_antigo = "arquivo_antigo.txt"
nome_novo = "arquivo_novo.txt"
try:
    os.rename(nome_antigo, nome_novo)
    print(f"O arquivo {nome_antigo} foi renomeado para {nome_novo}.")
except FileNotFoundError as erro:
    print(f"O arquivo {nome_antigo} não foi encontrado.")
    print(f"Descrição: {erro}")
except PermissionError as erro:
    print(f"Sem permissão para acessar o arquivo.")
    print(f"Descrição: {erro}")
except FileExistsError as erro:
    print(f"Arquivo destino já existe.")
    print(f"Descrição: {erro}")
'''
    


'''
#Utilizando a Função Remove
arquivo_a_remover = "teste.py"
try:
    os.remove(arquivo_a_remover)
    print(f"O arquivo {arquivo_a_remover} foi removido com sucesso.")
except FileNotFoundError as erro:
    print(f"O arquivo {arquivo_a_remover} não foi encontrado.")
    print(f"Descrição: {erro}")
except PermissionError as erro:
    print(f"Sem permissão para acessar o arquivo {arquivo_a_remover}.")
    print(f"Descrição: {erro}.")
except IsADirectoryError as erro:
    print(f"Remove serve apenas para arquivo.")
    print(f"Descrição: {erro}")
'''


import os
try:
    os.remove('arquivo.txt')
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Permissão negada.")
except IsADirectoryError:
    print("Não é possível remover, é um diretório.")
except Exception as e:
    print(f"Erro inesperado: {e}")

print("Termino do programa")
