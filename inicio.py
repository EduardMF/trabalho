from telaUsuario import TelaUser
from telaCidade import TelaCity
from tkinter import *
from tkinter import filedialog

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)

root.title('Projeto Banco de Dados')

root.state("zoomed")

filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)

menubar.add_cascade(label='Arquivo', menu=filemenu)
menubar.add_cascade(label='Cadastros', menu=filemenu2)
menubar.add_cascade(label='Ajuda', menu=filemenu3)

def Open():
    filedialog.askopenfilename()
def Save():
    filedialog.asksaveasfilename()
def Quit():
    root.destroy()
def Help():
    text = Text(root)
    text.pack()
    text.insert('insert', 'Ao clicar no botão da\n'
                          'respectiva cor, o fundo da tela\n'
                          'aparecerá na cor escolhida.')


def abrir_usuario():
    app = TelaUser(master=root)


def abrir_cidade():
    app = TelaCity(master=root)


filemenu.add_command(label='Abrir...', command=Open)
filemenu.add_command(label='Salvar como...', command=Save)

filemenu.add_command(label='Sair', command=Quit)
filemenu2.add_command(label='Usuários', command=abrir_usuario)
filemenu2.add_command(label='Cidades', command=abrir_cidade)
# filemenu2.add_command(label='Clientes', command=ColorBlack)
filemenu3.add_command(label='Ajuda', command=Help)
root.mainloop()