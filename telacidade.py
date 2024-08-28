# classe que modela cidade
from tkinter import *
from cidades import Cidades

class TelaCity:

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
        self.titulo = Label(self.container1, text="Informe os dados da Cidade: ")
        self.titulo["font"] = ("Calibri", "14", "bold")
        self.titulo.pack()

        # Label do ID da cidade
        self.idLabel = Label(self.container2, text="ID: ", font=12)
        self.idLabel.pack(side=LEFT)

        # Input para o ID da cidade
        self.idEntry = Entry(self.container2, font=self.fonte, width=5)
        self.idEntry.pack(side=LEFT)

        # Botão para buscar o ID da cidade | 'command' obrigatório
        self.btnBuscarId = Button(self.container2, text="Buscar", font=self.fonte, command=self.buscarCidade, width=5)
        self.btnBuscarId.pack(side=RIGHT)



        # # # USANDO CONTAINER 3 # # #
        # Label do Nome da Cidade
        self.nomeLabel = Label(self.container3, text="Nome: ", font=self.fonte, width=10)
        self.nomeLabel.pack(side=LEFT)

        # Input para o nome da Cidade
        self.nomeEntry = Entry(self.container3, font=self.fonte, width=25)
        self.nomeEntry.pack()



        # # # USANDO CONTAINER 4 # # #
        # Label do UF da cidade
        self.ufLabel = Label(self.container4, text="UF: ", font=self.fonte, width=10)
        self.ufLabel.pack(side=LEFT)

        # Input do Telefone do usuario
        self.ufEntry = Entry(self.container4, font=self.fonte, width=25)
        self.ufEntry.pack(side=LEFT)


        # # # USANDO CONTAINER 8 # # #
        # Botoes que irão manipular as informaçoes
        self.btnInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirCidade)
        self.btnInsert.pack(side=LEFT)

        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarCidade)
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirCidade)
        self.btnExcluir.pack(side=LEFT)



        # # # USANDO CONTAINER 9 # # #
        # Mensagem de PopUp na tela
        self.msg = Label(self.container9, text="", font=self.fonte)
        self.msg.pack()



    # Funçoes
    def inserirCidade(self):

        cid = Cidades()

        cid.nome = self.nomeEntry.get()
        cid.uf = self.ufEntry.get()

        self.msg["text"] = cid.insertCidade()

        self.nomeEntry.delete(0, END)
        self.ufEntry.delete(0, END)

    def alterarCidade(self):

        cid = Cidades()

        cid.nome = self.nomeEntry.get()
        cid.uf = self.ufEntry.get()

        self.msg["text"] = cid.updateCidade()

        self.idEntry.delete(0, END)
        self.ufEntry.delete(0, END)

    def excluirCidade(self):

        cid = Cidades()

        cid.nome = self.nomeEntry.get()
        cid.uf = self.ufEntry.get()

        self.msg["text"] = cid.deleteCidade()

        self.idEntry.delete(0, END)
        self.ufEntry.delete(0, END)

    def buscarCidade(self):

        cid = Cidades()

        idcidade = self.idEntry.get()

        self.msg["text"] = cid.selectCidade(idcidade)

        self.nomeEntry.delete(0, END)
        self.nomeEntry.insert(INSERT, cid.nome)

        self.ufEntry.delete(0, END)
        self.ufEntry.insert(INSERT, cid.uf)


if __name__ == "__main__":
    root = Tk()
    TelaCity(root)
    root.mainloop()