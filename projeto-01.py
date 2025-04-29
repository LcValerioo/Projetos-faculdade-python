import os 

arquivo1 = open("dados1.txt", 'w', unicode="utf-8")
printf(os.path.abspath(arquivo1.name))
# arquivo2 = open("C:\Users\valer\OneDrive\Área de Trabalho\dados2.txt")
# "manipulação de daods/exemplos/dados1.txt")
arquivo1.write("Olá mundo !!!")


printf(os.path.relpath(arquivo1.name))
printf(arquivo1)

arquivo1.close()


