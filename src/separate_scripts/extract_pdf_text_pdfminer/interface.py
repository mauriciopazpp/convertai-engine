import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

def run_script():
    pdf_path = pdf_path_var.get()
    start_page = start_page_var.get()
    end_page = end_page_var.get()
    page_height = page_height_var.get()
    header = header_var.get()
    footer = footer_var.get()
    debug = debug_var.get()

    if not pdf_path:
        messagebox.showerror("Erro", "O caminho do PDF é obrigatório.")
        return

    command = [
        "python3", "run.py",
        f"--pdf_path={pdf_path}"
    ]

    if start_page:
        command.append(f"--start_page={start_page}")
    if end_page:
        command.append(f"--end_page={end_page}")
    if page_height:
        command.append(f"--page_height={page_height}")
    if header:
        command.append(f"--header={header}")
    if footer:
        command.append(f"--footer={footer}")
    if debug:
        command.append("--debug")

    command.append("> files/output/output.txt")

    try:
        result = subprocess.run(" ".join(command), shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        messagebox.showinfo("Sucesso", "Script executado com sucesso.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", "Ocorreu um erro ao executar o script.")
        print(e.stderr)

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_path_var.set(file_path)

def center_window(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

root = tk.Tk()
root.title("Executor de Script")

tk.Label(root, text="Caminho do PDF:").grid(row=0, column=0, sticky=tk.W)
pdf_path_var = tk.StringVar(value="files/input/arte-da-guerra.pdf")
tk.Entry(root, textvariable=pdf_path_var, width=50).grid(row=0, column=1)
tk.Button(root, text="Selecionar PDF", command=select_pdf).grid(row=0, column=2)

tk.Label(root, text="Iniciar na página:").grid(row=1, column=0, sticky=tk.W)
start_page_var = tk.StringVar(root, "56")
tk.Entry(root, textvariable=start_page_var).grid(row=1, column=1)

tk.Label(root, text="Executar até a página:").grid(row=2, column=0, sticky=tk.W)
end_page_var = tk.StringVar(root, "57")
tk.Entry(root, textvariable=end_page_var).grid(row=2, column=1)

tk.Label(root, text="Altura do livro:").grid(row=3, column=0, sticky=tk.W)
page_height_var = tk.StringVar(root, "29.7")
tk.Entry(root, textvariable=page_height_var).grid(row=3, column=1)

tk.Label(root, text="Tamanho do cabeçalho:").grid(row=4, column=0, sticky=tk.W)
header_var = tk.StringVar(root, "1.76")
tk.Entry(root, textvariable=header_var).grid(row=4, column=1)

tk.Label(root, text="Tamanho do rodapé:").grid(row=5, column=0, sticky=tk.W)
footer_var = tk.StringVar(root, "1.76")
tk.Entry(root, textvariable=footer_var).grid(row=5, column=1)

tk.Label(root, text="Debug:").grid(row=6, column=0, sticky=tk.W)
debug_var = tk.BooleanVar(root, True)
tk.Checkbutton(root, variable=debug_var).grid(row=6, column=1)

tk.Button(root, text="Executar", command=run_script).grid(row=7, columnspan=3)

# Centralizar a janela
center_window(root)

root.mainloop()
