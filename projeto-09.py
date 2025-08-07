#Criação de aplicação GUI
"""
import tkinter as tk

def submit():
    #Recupera os dados dos campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    #imprime os dados no console
    print(f"Nome: {nome}")
    print(f"Email: {email}")

#Implementa a janela principal
root = tk.Tk()
root.title("Formulário de Inscrição")

#implementa um frame para conter os widgets
frame = tk.Frame()
frame.pack(padx=10, pady=10)

#Campo de entrada para "Nome"
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

#Campo de entrada para "Email"
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

#Botão de submissão
submit_button = tk.Button(frame, text='Submeter', command=submit)
submit_button.grid(row=5, columnspan=2, pady=10)

#inicializa o loop da GUI
root.mainloop()
"""

#Desenvolvendo exemplos de apliaçãoes GUI

#Widget Window (tk.Tk())
"""
#Nesse exemplo é implementado uma janela dimensionavel 
import tkinter as tk
janela = tk.Tk()
janela.title(" Aplicação GUI")
janela.mainloop()
"""
"""
#Nesse exemplo é implementado uma janela não dimensionavel 
import tkinter as tk
janela = tk.Tk()
janela.title(" Aplicação GUI NÃO Dimensionável")
janela.resizable(False, False) #O primeiro paramentro determina se a largura será dimensionavel, já o segundo determina se altura será.
janela.mainloop()
"""

#Widget Label
"""
import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Label")
ttk.Label(janela, text="Eu não sei o que é ttk").grid(column=0, row=0)
janela.mainloop()
"""
#Widget Button
"""
import tkinter as tk
contador = 0
def contador_label(lblRotulo):
   def funcao_contar():
      global contador
      contador = contador + 1
      lblRotulo.config(text=str(contador))
      lblRotulo.after(1000, funcao_contar)
      funcao_contar()
janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()
"""

#Widget Entry
"""
import tkinter as tk
def mostrar_nomes():
    print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)
tk.Label(janela,text="Sobrenome").grid(row=1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(janela, text='Sair', command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()
"""

#Widget Radiobutton
"""
import tkinter as tk
janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela,text="Escolha uma Linguagem de Programação:", justify=tk.LEFT, padx=20).pack()
tk.Radiobutton(janela, text="Python", padx=25, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx=25, variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C", padx=25, variable=v, value=3).pack(anchor=tk.W)
tk.Radiobutton(janela, text="HTML5", padx=25, variable=v, value=4).pack(anchor=tk.W)
tk.Radiobutton(janela, text="CSS", padx=25, variable=v, value=5).pack(anchor=tk.W)
btnAcao = tk.Button(janela, text='Clique aqui para Sair', width=20, command=janela.destroy)
btnAcao.pack(anchor=tk.W)
janela.mainloop()
"""

#Widgets Checkbox
"""
import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
def escolha_carreira():
    print("Gerencial: %d\nTécnica: %d" % (var1.get(), var2.get()))
ttk.Label(janela, text="Escolha sua vocação:").grid(row=0, sticky=tk.W)
var1 = tk.IntVar()
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)
var2 = tk.IntVar()
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W)
ttk.Button(janela, text='Sair', command=janela.quit).grid(row=3, sticky=tk.W, pady=4)
ttk.Button(janela, text='Mostrar', command=escolha_carreira).grid(row=4, sticky=tk.W, pady=4)
janela.mainloop()
"""

#Widget Text
"""
import tkinter as tk
janela = tk.Tk()
t = tk.Text(janela, height=2, width=30)
t.pack()
t.insert(tk.END, "Este é o tão famigerado Texto\nOMG\n")
#Widget Message
mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"
msg = tk.Message(janela, text = mensagem_para_usuario)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
#Executando a janela
tk.mainloop()
"""
#Widget Slider
"""
import tkinter as tk
from tkinter import ttk
def mostrar_valores():
    print(w1.get(), w2.get())
janela = tk.Tk()
w1 = ttk.Scale(janela, from_=0, to=50)
w1.pack()
w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
w2.pack()
ttk.Button(janela, text='Mostrar a Escala', command=mostrar_valores).pack()
janela.mainloop()
"""
#Widget Dialog
"""
import tkinter as tk
from tkinter import messagebox as mb
def resposta():
   mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")
def verificacao():
   if mb.askyesno('Verificar', 'Realmente quer sair?'):
      mb.showwarning('Yes', 'Ainda não foi implementado')
   else:
      mb.showinfo('No', 'A opção de Sair foi cancelada')
tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)
tk.mainloop()
"""

#Widget Combobox
"""
import tkinter as tk
from tkinter import ttk
# Criação de uma janela tkinter
janela = tk.Tk()
janela.title('Combobox')
janela.geometry('500x250')
# Componente Label
ttk.Label(janela, text = "Combobox Widget",background = 'green', foreground ="white",font = ("Times New Roman", 15)).grid(row = 0, column = 1)
# Componente Label
ttk.Label(janela, text = "Selecione um mês :",font = ("Times New Roman", 10)).grid(column = 0,row = 5, padx = 10, pady = 25)
# Componente Combobox
n = tk.StringVar()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)
# Adição de itens no Combobox
escolha['values'] = (' Janeiro',' Fevereiro',' Março',' Abril',' Maio',' Junho',' Julho',' Agosto',' Setembro',' Outubro',' Novembro',' Dezembro')
escolha.grid(column = 1, row = 5)
escolha.current()
janela.mainloop()
"""

import tkinter as tk
from tkinter import messagebox

def submit():
    #Recuperar os dados dos campos de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    #Verifica qual RadioButton está selecionado 
    linguagem_escolhida = linguagem_var.get()

    #Imprime os dados no console
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Linguagem Escolhida: {linguagem_escolhida}")

    #Mostrar uma caixa de mensagem com os dados
    messagebox.showinfo("Dados Submetidos", f"Nome: {nome}\nEmail: {email}\nLinguagem Escolhida: {linguagem_escolhida}")

#Cria a janela principal
root = tk.Tk()
root.title("Formulário de Inscrição")

#Cria um frame para conter os Widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

#Label para o Campo "Nome"
nome_label = tk.Label(frame, text="Nome:")
nome_label.grid(row=0, column=0, sticky="e")

#Campo de entrada para "Nome"
nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

#Label para o campo "Email"
email_label = tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0, sticky="e")

#Campo de entrada para "Email"
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

#Variavel para armazenar a escolha da linguagem
linguagem_var = tk.StringVar(value="Python")

#Radiobutton para "Python"
pyhton_radio = tk.Radiobutton(frame, text="Python", variable=linguagem_var, value="Python")
pyhton_radio.grid(row=2, column=0)

#Radiobutton  para "Java"
java_radio = tk.Radiobutton(frame, text="Java", variable=linguagem_var, value="Java")
java_radio.grid(row=2, column=1)

#Botão de submissão
submit_button = tk.Button(frame, text="Submeter", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

#Inicializando o Loop da GUI
root.mainloop()