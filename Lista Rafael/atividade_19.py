class Funcionario:
    def __init__(self, Nome, HoraTrabalhada):
        self.nome = Nome
        self.horaTrabalhada = float(HoraTrabalhada)
        self.salario = 6.25 * self.horaTrabalhada


    def Escrever(self,arquivo1):
        arquivo1.write(self.nome + ":" + str(self.salario) +"\n")





lista = []
nome = "C:/Users/horlab208/Documents/GitHub/Atividade_Objetos/Lista Rafael/ponto.txt"
arquivo = open(nome, "r+")
while True:
    linha = arquivo.readline()
    if not linha:
        break
    else:
        listaVariavel = []
        listaVariavel.append(linha.split())
        lista.append(Funcionario(listaVariavel[0][0],listaVariavel[0][1]))

arquivo.close()
nome = "C:/Users/horlab208/Documents/GitHub/Atividade_Objetos/Lista Rafael/salarios.txt"
arquivo1 = open(nome,"w")

for i in lista:
    i.Escrever(arquivo1)

arquivo1.close()





