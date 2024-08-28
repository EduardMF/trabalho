from usuarios import Usuarios
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Verdana", "8")

        # Create and pack frames
        self.container1 = Frame(master, pady=10)
        self.container1.pack()
        self.container2 = Frame(master, padx=20, pady=5)
        self.container2.pack()
        self.container3 = Frame(master, padx=20, pady=5)
        self.container3.pack()
        self.container4 = Frame(master, padx=20, pady=5)
        self.container4.pack()
        self.container5 = Frame(master, padx=20, pady=5)
        self.container5.pack()
        self.container6 = Frame(master, padx=20, pady=5)
        self.container6.pack()
        self.container7 = Frame(master, padx=20, pady=5)
        self.container7.pack()
        self.container8 = Frame(master, padx=20, pady=10)
        self.container8.pack()
        self.container9 = Frame(master, pady=15)
        self.container9.pack()

        # Widgets in container1
        self.titulo = Label(self.container1, text="Informe os dados :", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        # Widgets in container2
        self.lblidusuario = Label(self.container2, text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2, width=10, font=self.fonte)
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarUsuario)
        self.btnBuscar.pack(side=RIGHT)

        # Widgets in container3
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3, width=25, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        # Widgets in container4
        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4, width=25, font=self.fonte)
        self.txttelefone.pack(side=LEFT)

        # Widgets in container5
        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container5, width=25, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        # Widgets in container6
        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.container6, width=25, font=self.fonte)
        self.txtusuario.pack(side=LEFT)

        # Widgets in container7
        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7, width=25, show="*", font=self.fonte)
        self.txtsenha.pack(side=LEFT)

        # Widgets in container8
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirUsuario)
        self.bntInsert.pack(side=LEFT)
        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12,
                                 command=self.alterarUsuario)
        self.bntAlterar.pack(side=LEFT)
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12,
                                 command=self.excluirUsuario)
        self.bntExcluir.pack(side=LEFT)

        # Widgets in container9
        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.insertUser()
        self.clear_entries()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        self.lblmsg["text"] = user.updateUser()
        self.clear_entries()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.deleteUser()
        self.clear_entries()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.txtidusuario.get()
        result = user.selectUser(idusuario)
        if result == "Busca feita com sucesso!":
            self.txtidusuario.insert(INSERT, user.idusuario)
            self.txtnome.insert(INSERT, user.nome)
            self.txttelefone.insert(INSERT, user.telefone)
            self.txtemail.insert(INSERT, user.email)
            self.txtusuario.insert(INSERT, user.usuario)
            self.txtsenha.insert(INSERT, user.senha)
        self.lblmsg["text"] = result

    def clear_entries(self):
        """Clear all text entries."""
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    root.mainloop()