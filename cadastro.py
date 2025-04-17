# cadastro.py

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para cadastrar no banco
def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    endereco = entry_endereco.get()
    valor = entry_valor.get()
    parcelas = entry_parcelas.get()

    # Validações simples
    if not nome or not cpf or not valor or not parcelas:
        messagebox.showerror("Erro", "Preencha os campos obrigatórios!")
        return

    try:
        valor = float(valor)
        parcelas = int(parcelas)
    except ValueError:
        messagebox.showerror("Erro", "Valor deve ser número decimal e Parcelas número inteiro.")
        return

    # Conectar e salvar no banco
    conn = sqlite3.connect('cooperativa.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cooperativados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            endereco TEXT,
            valor REAL,
            parcelas INTEGER
        )
    ''')

    cursor.execute("INSERT INTO cooperativados (nome, cpf, endereco, valor, parcelas) VALUES (?, ?, ?, ?, ?)",
                   (nome, cpf, endereco, valor, parcelas))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

    # Limpa os campos
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_parcelas.delete(0, tk.END)

# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Cooperativados")
janela.geometry("400x300")

# Widgets (componentes da tela)
tk.Label(janela, text="Nome*").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="CPF*").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_cpf = tk.Entry(janela, width=30)
entry_cpf.grid(row=1, column=1)

tk.Label(janela, text="Endereço").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_endereco = tk.Entry(janela, width=30)
entry_endereco.grid(row=2, column=1)

tk.Label(janela, text="Valor*").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_valor = tk.Entry(janela, width=30)
entry_valor.grid(row=3, column=1)

tk.Label(janela, text="Parcelas*").grid(row=4, column=0, padx=10, pady=5, sticky='e')
entry_parcelas = tk.Entry(janela, width=30)
entry_parcelas.grid(row=4, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar, bg="green", fg="white").grid(row=5, column=1, pady=20)

# Rodar a janela
janela.mainloop()
