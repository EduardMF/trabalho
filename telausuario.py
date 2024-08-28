# classe que modela o usuário
from tkinter import *
from usuarios import Usuarios

class TelaUser:

    def __init__(self, master=None):

        self.fonte = ("Verdana", "13")

        # 1
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        # 2
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()


        # 3
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()


        # 4
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()


        # 5
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()


        # 6
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()


        # 7
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()


        # 8
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        # 9
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()



        # # # USANDO CONTAINER 2 # # #
        # Label do Titulo
        self.titulo = Label(self.container1, text="Informe os dados abaixo: ")
        self.titulo["font"] = ("Calibri", "14", "bold")
        self.titulo.pack()

        # Label do ID do usuario
        self.idLabel = Label(self.container2, text="ID: ", font=12)
        self.idLabel.pack(side=LEFT)

        # Input para o ID do usuario
        self.idEntry = Entry(self.container2, font=self.fonte, width=5)
        self.idEntry.pack(side=LEFT)

        # Botão para buscar o ID do usuario | 'command' obrigatório
        self.btnBuscarId = Button(self.container2, text="Buscar", font=self.fonte, command=self.buscarUsuario, width=5)
        self.btnBuscarId.pack(side=RIGHT)



        # # # USANDO CONTAINER 3 # # #
        # Label do Nome do usuario
        self.nomeLabel = Label(self.container3, text="Nome: ", font=self.fonte, width=10)
        self.nomeLabel.pack(side=LEFT)

        # Input para o nome do usuario
        self.nomeEntry = Entry(self.container3, font=self.fonte, width=25)
        self.nomeEntry.pack()



        # # # USANDO CONTAINER 4 # # #
        # Label do Telefone do usuario
        self.telefoneLabel = Label(self.container4, text="Telefone: ", font=self.fonte, width=10)
        self.telefoneLabel.pack(side=LEFT)

        # Input do Telefone do usuario
        self.telefoneEntry = Entry(self.container4, font=self.fonte, width=25)
        self.telefoneEntry.pack(side=LEFT)




        # # # USANDO CONTAINER 5 # # #
        # Label do email do usuario
        self.emailLabel = Label(self.container5, text="E-mail: ", font=self.fonte, width=10)
        self.emailLabel.pack(side=LEFT)

        # Input do email do usuario
        self.emailEntry = Entry(self.container5, font=self.fonte, width=25)
        self.emailEntry.pack(side=LEFT)



        # # # USANDO CONTAINER 6 # # #
        # Label do nome de Usuario (username)
        self.usernameLabel = Label(self.container6, text="Username: ", font=self.fonte, width=10)
        self.usernameLabel.pack(side=LEFT)

        # Input para nome de usuario
        self.usernameEntry = Entry(self.container6, width=25, font=self.fonte)
        self.usernameEntry.pack(side=LEFT)



        # # # USANDO CONTAINER 7 # # #
        # Label da senha do usuario
        self.senhaLabel = Label(self.container7, text="Senha: ", font=self.fonte, width=10)
        self.senhaLabel.pack(side=LEFT)

        # Input para senha do usuario
        self.senhaEntry = Entry(self.container7, width=25, show="*", font=self.fonte)
        self.senhaEntry.pack(side=LEFT)




        # # # USANDO CONTAINER 8 # # #
        # Botoes que irão manipular as informaçoes
        self.btnInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirUsuario)
        self.btnInsert.pack(side=LEFT)

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarUsuario)
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirUsuario)
        self.btnExcluir.pack(side=LEFT)




        # # # USANDO CONTAINER 9 # # #
        # Mensagem de PopUp na tela
        self.msg = Label(self.container9, text="", font=self.fonte)
        self.msg.pack()



    # Funçoes

    def inserirUsuario(self):

        user = Usuarios()

        user.nome = self.nomeEntry.get()
        user.telefone = self.telefoneEntry.get()
        user.email = self.emailEntry.get()
        user.usuario = self.usernameEntry.get()
        user.senha = self.senhaEntry.get()

        self.msg["text"] = user.insertUser()

        self.idEntry.delete(0, END)
        self.telefoneEntry.delete(0, END)
        self.nomeEntry.delete(0, END)
        self.emailEntry.delete(0, END)
        self.usernameEntry.delete(0, END)
        self.senhaEntry.delete(0, END)

    def alterarUsuario(self):

        user = Usuarios()

        user.nome = self.nomeEntry.get()
        user.telefone = self.telefoneEntry.get()
        user.email = self.emailEntry.get()
        user.usuario = self.usernameEntry.get()
        user.senha = self.senhaEntry.get()

        self.msg["text"] = user.updateUser()

        self.idEntry.delete(0, END)
        self.nomeEntry.delete(0, END)
        self.telefoneEntry.delete(0, END)
        self.emailEntry.delete(0, END)
        self.usernameEntry.delete(0, END)
        self.senhaEntry.delete(0, END)

    def excluirUsuario(self):

        user = Usuarios()

        user.nome = self.nomeEntry.get()
        user.telefone = self.telefoneEntry.get()
        user.email = self.emailEntry.get()
        user.usuario = self.usernameEntry.get()
        user.senha = self.senhaEntry.get()

        self.msg["text"] = user.deleteUser()

        self.idEntry.delete(0, END)
        self.nomeEntry.delete(0, END)
        self.telefoneEntry.delete(0, END)
        self.emailEntry.delete(0, END)
        self.usernameEntry.delete(0, END)
        self.senhaEntry.delete(0, END)

    def buscarUsuario(self):

        user = Usuarios()

        idusuario = self.idEntry.get()

        self.msg["text"] = user.selectUser(idusuario)

        self.idEntry.delete(0, END)
        self.idEntry.insert(INSERT, user.idusuario)

        self.nomeEntry.delete(0, END)
        self.nomeEntry.insert(INSERT, user.nome)

        self.telefoneEntry.delete(0, END)
        self.telefoneEntry.insert(INSERT, user.telefone)

        self.emailEntry.delete(0, END)
        self.emailEntry.insert(INSERT, user.email)

        self.usernameEntry.delete(0, END)
        self.usernameEntry.insert(INSERT, user.usuario)

        self.senhaEntry.delete(0, END)
        self.senhaEntry.insert(INSERT, user.senha)


if __name__ == "__main__":
    root = Tk()
    TelaUser(root)
    root.mainloop()