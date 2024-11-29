import tkinter as tk
from tkinter import messagebox

# Função para calcular o saldo e o nível do herói
def calcular_saldo(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 10 < vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel

# Função para salvar o resultado em um arquivo de texto
def salvar_resultado(nome_arquivo, saldo_vitorias, nivel):
    with open(nome_arquivo, "w") as file:
        file.write(f"O Herói tem um saldo de {saldo_vitorias} e está no nível de {nivel}.\n")

# Função chamada ao clicar no botão "Calcular"
def on_calcular():
    try:
        vitorias = int(entry_vitorias.get())
        derrotas = int(entry_derrotas.get())
        saldo_vitorias, nivel = calcular_saldo(vitorias, derrotas)
        salvar_resultado("resultado_rankeadas.txt", saldo_vitorias, nivel)
        messagebox.showinfo("Resultado", f"O Herói tem um saldo de {saldo_vitorias} e está no nível de {nivel}.\nAs informações foram salvas no arquivo 'resultado_rankeadas.txt'.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos para vitórias e derrotas.")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Partidas Rankeadas")
root.geometry("300x200")

# Rótulo e campo de entrada para vitórias
tk.Label(root, text="Número de Vitórias:").pack(pady=5)
entry_vitorias = tk.Entry(root)
entry_vitorias.pack(pady=5)

# Rótulo e campo de entrada para derrotas
tk.Label(root, text="Número de Derrotas:").pack(pady=5)
entry_derrotas = tk.Entry(root)
entry_derrotas.pack(pady=5)

# Botão para calcular o saldo e nível
tk.Button(root, text="Calcular", command=on_calcular).pack(pady=20)

# Iniciar o loop principal da interface
root.mainloop()
