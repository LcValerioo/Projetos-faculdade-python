import os
import shutil

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
'''
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
'''

#Manipulação de diretórios 
'''
#Criando diretório
try:
    os.mkdir(f"meu_diretorio")
    print(f"Diretório criado!")
except PermissionError as erro:
    print(f"Sem permissão para criar diretório")
    print(f"Descrição: {erro}")
except FileExistsError as erro:
    print(f"Diretório já existe")
    print(f"Descrição: {erro}")

'''
'''
#Excluindo Diretório
try:
    os.rmdir("meu_diretorio")
    print(f"Diretório Removido.")
except PermissionError as erro:
    print(f"Sem permissão para remover o diretório.")
    print(f"Descrição: {erro}")
except FileNotFoundError as erro:
    print(f"Diretório Inexistente.")
    print(f"Descrição: {erro}")
except OSError as erro:
    print("Outro erro.")
    print(f"O diretório está vazio ?")
    print(f"Descrição: {erro}")
'''

#Listando conteúdo de diretórios
'''
try:
    entradas = os.scandir("meu_diretorio")

    for obj in entradas:
        print(obj)
        print(f"Nome: {obj.name}")
        print(f"Caminho: {obj.path}")
        print(f"É Diretório: {obj.is_dir()}")
        print(f"É arquivo: {obj.is_file()}")
        if obj.is_file():
            print("Tamanho:", obj.stat().st_size, "B")
        print("=====================================")

except FileNotFoundError:
    print(f"O Caminho não existe.")
except NotADirectoryError:
    print(f"O caminho não é de um diretório.")

print("Termino do Programa")
'''

#organizando os arquivos pelas suas extensões

def criar_diretorios(diretorios):
       for diretorio in diretorios:
           if not os.path.exists(diretorio):
               try:
                   os.makedirs(diretorio)
                   print(f"Diretório {diretorio} criado.")
               except PermissionError:
                   print(f"Sem permissão para criar o diretório {diretorio}.")
               except Exception as e:
                   print(f"Erro inesperado ao criar {diretorio}: {e}")

def mover_arquivos(diretorio_origem):
       for arquivo in os.listdir(diretorio_origem):
           caminho_arquivo = os.path.join(diretorio_origem, arquivo)
           if os.path.isfile(caminho_arquivo):
               extensao = arquivo.split('.')[-1].lower()
               if extensao in ['pdf', 'txt', 'jpg']:
                   diretorio_destino = os.path.join(diretorio_origem, extensao)
                   try:
                       shutil.move(caminho_arquivo, diretorio_destino)
                       print(f"{arquivo} movido para {diretorio_destino}.")
                   except PermissionError:
                       print(f"Sem permissão para mover {arquivo}.")
                   except Exception as e:
                       print(f"Erro inesperado ao mover {arquivo}: {e}")
               else:
                   print(f"Extensão {extensao} de {arquivo} não é suportada.") 

def main():
       diretorio_trabalho = "diretorio_trabalho"
       diretorios = [os.path.join(diretorio_trabalho, 'pdf'),
                     os.path.join(diretorio_trabalho, 'txt'),
                     os.path.join(diretorio_trabalho, 'jpg')]
 
       # Criar diretórios se não existirem
       criar_diretorios(diretorios)
 
       # Mover arquivos para os diretórios correspondentes
       mover_arquivos(diretorio_trabalho)
 
if __name__ == "__main__":
    main()