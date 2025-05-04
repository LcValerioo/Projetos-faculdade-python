from datetime import datetime
#Manipulçao de String

#Método STRIP
'''
#Exemplo 01
arquivo = open("dados1.txt", "r", encoding="utf-8")

conteudo = arquivo.read()

print("Tipo do conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo read: ")
print(repr(conteudo))

arquivo.close()
'''
'''
#Exemplo 02
arquivo = open("dados1.txt", "r", encoding="utf-8")

conteudo = arquivo.readline()

print("Conteúdo retornado pelo readline: ")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Próximo Conteúdo retornado: ")
print(repr(proximo_conteudo))

arquivo.close()
'''

'''
#Exemplo 03
arquivo = open("dados1.txt", "r", encoding="utf-8")

conteudo = arquivo.readlines()

print("Tipo do Conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo readlines: ")
print(repr(conteudo))

arquivo.close()
'''
'''
#Exemplo 04 -  fazendo a remoção de caracteres inuteis 

with open("dados1.txt", "r", encoding="utf-8") as arquivo:
    print("Representação Original: ")
    for linha in arquivo:
        print(repr(linha))

with open("dados1.txt", "r", encoding="utf-8") as arquivo:
    print("Representação da linha após o STRIP: ")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
'''
'''
#Exemplo 05 - Usando contador 

with open("dados1.txt", "r", encoding="utf-8") as arquivo:
    print("Total de linhas do arquivo original")
    contador = 0
    for linha in arquivo:
        if linha:
            contador += 1
    print("Total: ", contador)

with open("dados1.txt", "r", encoding="utf-8") as arquivo:
    print("Total REAL de linhas no arquivo (após o uso do Strip)")
    contador = 0
    for linha in arquivo:
        if linha.strip():
            contador += 1
    print("Total: ", contador)
'''

#Método COUNT e SPLIT

'''
#Exemplo 06 - COUNT

with open("dados1.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    contador = texto.count("Olá")
    print("Total de 'Olás': ", contador)
'''
'''
#Exemplo 07 - SPLIT

frase1 = "Eu amo comer amoras no café da manhã"
lista_termo1 = frase1.split()
print(lista_termo1)

frase2 = "Amora  abacaxi   abacate    banana"
lista_termo2 = frase2.split()
print(lista_termo2)

frase3 = "Carro,Moto,Avião"
lista_termo3 = frase3.split(',')
print(lista_termo3)
'''
'''
#Exemplo 08

frase = "Eu amo comer amoras no café da manhã"

#Resultado obritdo utilizadno o método count diretamente
print("Contagem direta: ", frase.count('amo'))

#Resultado obtido utilizando a quebra da frase em palavras
contador = 0
lista_termo = frase.split()
for termo in lista_termo:
    if termo == 'amo':
        contador += 1
print("Contagem correta: ", contador)
'''
'''
#Exemplo 09 

frase = "Eu amo comer amoras no café da manhã"
lista_termos = frase.split()
contagem = lista_termos.count("amo")
print("Contagem: ", contagem)
'''

#Método JOIN
'''
#Exemplo 10

minha_lista = ["Arroz", "Feijão", "Macarrão", "Buchada"]

texto1 = ", ".join(minha_lista)
with open("dados1.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto1)


texto2 = "\n".join(minha_lista)
with open("dados1.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto2)
'''

#Formatação de STRINGS
'''
#Exemplo 11

#Método format()
hoje = datetime.now()
data_formatada = hoje.strftime("Data: %d/%m/%y")
print(data_formatada)

#F-string
hoje = datetime.now()
data_formatada = f"Data: {hoje: %d/%m/%y}"
print(data_formatada)
'''
'''
#Exemplo 12

nome = "João"

minha_string = "Olá, "  + nome + "."
minha_fstring1= f"Olá, {nome}"
minha_fstring2= f"Olá, {nome.upper()}"
minha_fstring3= f"Quantos anos você tem? {10 + 8}"
minha_fstring4= f"O número 2 é maior que o número 1? {2 > 1}"
minha_fstring5= f"O número 2 está contido na lista [4, 5, 6]? {2 in [4, 5, 6]}"

print(minha_string)
print(minha_fstring1)
print(minha_fstring2)
print(minha_fstring3)
print(minha_fstring4)
print(minha_fstring5)
'''
'''
#Exemplo 13

frutas = ['Jabuticaba', 'Laranja', 'Uva', 'Banana']
for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número de Letras: {len(fruta): 3}"
    print(minha_fruta)

print()

pi = 3.1415
meu_numero = f"O número PI é: {pi:.1f}"
meu_numero_deslocado = f"O número PI deslocado é: {pi:6.1f}"
meu_numero_preciso = f"O número PI mais preciso é: {pi:.4f}"
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f"A data de hoje é {data}"
minha_data_formatada = f"A data de hoje formatada é {data: %d/%m/%y}"
print(minha_data)
print(minha_data_formatada)
'''