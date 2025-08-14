import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd

#Dicionario de usuarios (credenciados)
usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"},
}

def abri_tela_login():
    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Usuário:").pack()
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack()

    tk.Label(login_win, text="Senha:").pack()
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack()

    def validar_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            tipo_usuario = usuario[usuario]["tipo"]
            login_win.destroy()
            iniciar_sistema(tipo_usuario, usuario)
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")

    tk.Button(login_win, text="Entrar", command=validar_login).pack()
    login_win.mainloop()

def iniciar_sistema(tipo_usuario, usuario):
    janela = tk.Tk()
    janela.title("Sistema de Notas")
    janela.geometry("820x600")

    colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
    treeMedias = ttk.Treeview(janela, columns=colunas, show="headings")

    for coluna in colunas:
        treeMedias.heading(coluna, text=coluna)
        treeMedias.column(coluna, width=100)

    treeMedias.pack(padx=10, pady=10)
    scrollbar = ttk.Scrollbar(janela, orient="vertical", command=treeMedias.yview)
    scrollbar.pack(side="right", fill="y")

    carregar_dados(treeMedias, usuario, tipo_usuario)

    if tipo_usuario == "professor":
        tk.Button(janela, text="Cadastrar Aluno", command=lambda: cadastrar_aluno(treeMedias)).pack()
        tk.Button(janela, text="Excluir Aluno", command=lambda: excluir_aluno(treeMedias)).pack()
    
    janela.mainloop()

def carregar_dados(tree, usuario, tipo_usuario):
    try:
        df = pd.read_excel("planilhaAlunos.xlsx")
        tree.delete(*tree.get_children())

        if tipo_usuario == "professor":
            for _, row in df.iterrows():
                tree.insert("", "end", values={row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"], })
        else:
            df_alunos = df[df["Alunos"] == usuario]
            for _, row in df.iterrows():
                tree.insert("", "end", values={row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"], })
    except FileNotFoundError:   
        print("Nenhum dados Encontrado.")

def cadastrar_aluno(tree):
    nome = simpledialog.askstring("Cadastro", "Nome do Aluno:")
    nota1 = simpledialog.askstring("Cadastro", "Nota 1:")
    nota2 = simpledialog.askstring("Cadastro", "Nota 2:")
    media, situacao = verifica_situacao(nota1, nota2)

    tree.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))
    salvar_dados(tree)

def excluir_aluno(tree):
    if usuarios["professor"]["tipo"] != "professor":
        messagebox.showwarning("Acesso Negado", "Somente professores podem excluir registros.")
        return
    
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Nenhum aluno selecionado para exclusão.")
        return
    
    tree.delete(selected_item)
    salvar_dados(tree)

def salvar_dados(tree):
    dados = []
    for line in tree.get_children():
        valores = tree.item(line)["values"]
        dados.append(valores)

    df = pd.DataFrame(data=dados, columns=("Aluno", "Nota1", "Nota2", "Média", "Situação"))
    print("Dados salvos com sucesso.")

def verifica_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if(media >= 7.0):
            return media, "Aprovado"
    elif(media >=5.0):
        return media, "Recuperação"
    else:
        return media, "Reprovado"

abri_tela_login()