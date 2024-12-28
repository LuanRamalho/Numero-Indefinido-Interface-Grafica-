import tkinter as tk
from tkinter import messagebox

class ListaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Gerenciador de Lista de Números")
        self.geometry("400x450")
        self.configure(bg='#7A0070')
        
        # Label e entrada para o número de elementos
        tk.Label(self, text="Digite a quantidade de elementos:", bg='#7A0070', fg="#90FFC7", font=('Arial', 18, "bold")).pack(pady=10)
        self.qtd_elementos_var = tk.IntVar()
        self.qtd_entry = tk.Entry(self, textvariable=self.qtd_elementos_var, font=('Arial', 12))
        self.qtd_entry.pack(pady=10)
        
        # Listbox para exibir os elementos
        self.lista_box = tk.Listbox(self, width=50, height=10, font=('Arial', 12))
        self.lista_box.pack(pady=10)
        
        # Campo de entrada para novos números
        self.novo_elemento_var = tk.StringVar()
        tk.Entry(self, textvariable=self.novo_elemento_var, font=('Arial', 12)).pack(pady=5)
        
        # Botão para adicionar itens à lista
        tk.Button(self, text="Adicionar", command=self.adicionar_item, bg='#87CEFA', font=('Arial', 12, "bold")).pack(pady=5)
        
        # Botão para remover itens da lista
        tk.Button(self, text="Excluir", command=self.excluir_item, bg='#FFA07A', font=('Arial', 12, "bold")).pack(pady=5)
        
    def adicionar_item(self):
        qtd = self.qtd_elementos_var.get()
        if qtd == 0:
            messagebox.showerror("Erro", "Defina a quantidade antes de adicionar itens.")
            return
        
        if len(self.lista_box.get(0, tk.END)) >= qtd:
            messagebox.showerror("Erro", "Limite de elementos atingido.")
            return
        
        novo_elemento = self.novo_elemento_var.get().strip()
        if novo_elemento.isdigit() or (novo_elemento.startswith('-') and novo_elemento[1:].isdigit()):
            self.lista_box.insert(tk.END, novo_elemento)
            self.novo_elemento_var.set("")
        else:
            messagebox.showerror("Erro", "Digite apenas números válidos.")
    
    def excluir_item(self):
        selecionado = self.lista_box.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para excluir.")
        else:
            self.lista_box.delete(selecionado)

if __name__ == "__main__":
    app = ListaApp()
    app.mainloop()
