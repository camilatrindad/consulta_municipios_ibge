import requests
import tkinter as tk
from tkinter import messagebox, ttk

def buscar_municipios():
    uf = entrada_uf.get().upper().strip()

    if len(uf) != 2:
        messagebox.showerror("Erro", "Digite uma sigla válida (ex: SP, RJ)")
        return

    try:
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        texto.delete("1.0", tk.END)

        for municipio in dados:
            nome = municipio["nome"]
            microrregiao = municipio["microrregiao"]["nome"]
            mesorregiao = municipio["microrregiao"]["mesorregiao"]["nome"]

            texto.insert(tk.END, f"📍 Município: {nome}\n")
            texto.insert(tk.END, f"   Microrregião: {microrregiao}\n")
            texto.insert(tk.END, f"   Mesorregião: {mesorregiao}\n\n")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro na consulta:\n{e}")

# ================= JANELA =================
janela = tk.Tk()
janela.title("Consulta de Municípios - IBGE")
janela.geometry("650x520")
janela.configure(bg="#1e1e1e")

# ================= ESTILO =================
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",
                background="#1e1e1e",
                foreground="#ffffff",
                font=("Segoe UI", 11))

style.configure("TButton",
                background="#3a3a3a",
                foreground="#ffffff",
                font=("Segoe UI", 10),
                padding=6)

style.map("TButton",
          background=[("active", "#505050")])

style.configure("TEntry",
                fieldbackground="#2b2b2b",
                foreground="#ffffff")

# ================= TÍTULO =================
titulo = ttk.Label(
    janela,
    text="Consulta de Municípios por Estado",
    font=("Segoe UI", 17, "bold")
)
titulo.pack(pady=20)

# ================= INPUT =================
frame_entrada = tk.Frame(janela, bg="#1e1e1e")
frame_entrada.pack(pady=10)

ttk.Label(frame_entrada, text="UF do Estado:").grid(row=0, column=0, padx=5)

entrada_uf = ttk.Entry(frame_entrada, width=10, font=("Segoe UI", 11))
entrada_uf.grid(row=0, column=1, padx=5)

botao = ttk.Button(
    frame_entrada,
    text="Buscar",
    command=buscar_municipios
)
botao.grid(row=0, column=2, padx=10)

# ================= TEXTO COM SCROLL =================
frame_texto = tk.Frame(janela, bg="#1e1e1e")
frame_texto.pack(expand=True, fill="both", padx=20, pady=10)

scroll = ttk.Scrollbar(frame_texto)
scroll.pack(side="right", fill="y")

texto = tk.Text(
    frame_texto,
    bg="#121212",
    fg="#e6e6e6",
    insertbackground="#ffffff",
    font=("Consolas", 10),
    wrap="word",
    yscrollcommand=scroll.set
)
texto.pack(expand=True, fill="both")

scroll.config(command=texto.yview)

# ================= RODAPÉ =================
rodape = ttk.Label(
    janela,
    text="API pública do IBGE • Python + Tkinter",
    font=("Segoe UI", 9)
)
rodape.pack(pady=8)

janela.mainloop()
