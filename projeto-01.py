import os
'''
#Abrindo o arquivo no modo escrita utilizando o metodo OPEN
arquivo = open('dados1.txt', 'w', encoding="utf-8")

#Exibindo os atributos do arquivo
print("Nome do arquivo: ", arquivo.name)
print("Modo de abertura: ", arquivo.mode)
print("Arquivo Está fechado ?", arquivo.closed)

#Escrevendo no arquivo utilizando o metodo WRITE
arquivo.write("Olá, mundo!")

#Fechando o arquivo usando o metodo CLOSE
arquivo.close()

#Verificando se o arquivo está fechado usando o metodo CLOSED
print("Arquivo está fechado agora? ", arquivo.closed)

#Exibindo caminhos relativos e absolutos

relpath = os.path.relpath('dados1.txt')
abspath = os.path.abspath('dados1.txt')

print("Caminho Relativo: ", relpath)
print("Caminho Absoluto: ", abspath)

'''

#Verificando o conteudo de um arquivo usando o metodo READ
'''
arquivo = open("dados1.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

print("Tipode conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo read: ")
print(repr(conteudo))

arquivo.close()
'''
'''
arquivo = open("dados1.txt", "r", encoding="utf-8")

conteudo = arquivo.readline()

print("Tipo de Conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo readline: ")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo Conteúdo retornado: ")
print(repr(proximo_conteudo))

arquivo.close()
'''
'''
arquivo = open("dados1.txt", "r", encoding="utf-8")

conteudo = arquivo.readlines()

print("Tipo de conteúdo: ", type(conteudo))
print(repr(conteudo))

arquivo.close()
'''
'''
#Exibindo as informações do arquivo usando laço de repetição FOR
arquivo = open("dados1.txt", "r", encoding="utf-8")

print("Iterando sobre o arquivo")
for linha in arquivo:
    print(repr(linha))

arquivo.close()
'''
'''
#Exbindo os conteudos de um arquivo mais de uma vez no mesmo codigo
arquivo = open("dados1.txt", "r", encoding="utf-8")

conteudo = arquivo.read()
print("Todo o conteúdo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Releitura de todo o conteúdo do arquivo")
print(repr(conteudo_releitura))

arquivo.close()

arquivo_reaberto = open("dados1.txt", "r", encoding="utf-8")

conteudo_reaberto = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo novamente")
print(repr(conteudo_reaberto), '\n')

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo após o SEEK")
print(repr(conteudo_seek))

arquivo_reaberto.close()
'''

#Escrevendo conteúdo em um arquivo
'''
#Aqui estamos sobreescrevendo o conteudo que já existe dentro do arquivo

arquivo_escrita = open("dados_write.txt", "w", encoding="utf-8")
arquivo_escrita.write("Conteúdo da primeira linha.")
arquivo_escrita.write("\nConteúdo da segunda linha.")
arquivo_escrita.close()
'''
'''
linhas = ["Conteúdo da primeira linha.", 
            "\nConteúdo da segunda linha."]

arquivo_escrita = open("dados1.txt", "w", encoding="utf-8")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()
'''
'''
#Aqui estamos acrescentando um novo conteudo ao conteudo já existente do arquivo
arquivo_escrita = open("dados1.txt", "a", encoding="utf-8")

arquivo_escrita.write("\nConteudo adicional.")

arquivo_escrita.close()
'''

#Utilizando o operador WITH 
print("Iterando sobre o arquivo")

with open("dados1.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo", arquivo.name)
    
