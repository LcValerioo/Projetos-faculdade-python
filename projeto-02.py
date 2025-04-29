import os

#Abrindo o arquivo no modo escrita
arquivo = open('dados1.txt', 'w', encoding="utf-8")

#Exibindo os atributos do arquivo
print("Nome do arquivo: ", arquivo.name)
print("Modo de abertura: ", arquivo.mode)
print("Arquivo Está fechado ?", arquivo.closed)

#Escrevendo no arquivo
arquivo.write("Olá, mundo!")

#Fechando o arquivo
arquivo.close()

#Verificando se o arquivo está fechado
print("Arquivo está fechado agora? ", arquivo.closed)

#Exibindo caminhos relativos e absolutos

relpath = os.path.relpath('dados1.txt')
abspath = os.path.abspath('dados1.txt')

print("Caminho Relativo: ", relpath)
print("Caminho Absoluto: ", abspath)