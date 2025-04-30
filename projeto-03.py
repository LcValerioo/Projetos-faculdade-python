#Manipulando arquivo-texto
'''
    *Esse programa visa capturar texto via console e armazenar em variaveis locais;
    *Após a inserção das frases, o algoritmo vai manipular os dados dentro do Código
    onde os espaços em branco serão removidos e as Letras ficarão todas em maiúsculas.
'''
def main():
    #Inicio do programa e declaração de variaveis
    print("Digite suas frases. Difite 'sair' para terminar e salvar o arquivo.")
    frases = []
    dados_modificados = []

    #Laço de iteração booleana para capturar as frases via console
    while True:
        #Condicional que verifica a continuidade do laço
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada) #incrementando as frases à lista

    #Escrevendo as frases no meu_arquivo.txt
    with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
        for frase in frases:
            arquivo.write(frase + "\n")

    print("Arquivo original criado. Agora vamos manipular os dados.")
    
    #Lendo dados do arquivo e fazendo as manipulações
    with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper()) #Exemplo de manipulação: convertendo para maisculas as letras com o UPPER e retirando os espaços em branco das extremidades da lista com o STRIP
    
    #Sobrescrevendo o arquivo já manipulado
    with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")
        print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
    main()