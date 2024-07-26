class Funcionarios:
    
    def __init__(self,nome,cargo,salario, horastrabalhadas):
        self.Nome = nome
        self.Cargo= cargo
        self.Salario = salario
        self.HorasTrabalhadas = horastrabalhadas
    
    def Escrever(self,arquivo1):
        arquivo1.write("-"*60 + "\n" +"nome:"+ self.Nome + "\n" + "cargo:" + self.Cargo +"\n" + "salario:"+ self.Salario +"\n"+ "horas trabalhadas:"+str(self.HorasTrabalhadas) + "\n" + "-"*60+ "\n")
lista = []
print("digite as informações solicitadas, para sair digite na horasTrabalhadas um numero negativo:")
while True:
    print("-"*60)
    nome = input("digite seu nome:")
    cargo = input("digite seu cargo:")
    salario = input("digite seu salario:")
    horastrabalhadas = int(input("digite suas horas trabalhadas:"))
    if horastrabalhadas<0:
        break

    else:
        lista.append(Funcionarios(nome,cargo,salario,horastrabalhadas))

nome ="C:/Users/horlab208/Documents/GitHub/Atividade_Objetos/Lista Rafael/relatorio_rh.txt"
arquivo1 = open(nome,"w")
for i in lista:
    i.Escrever(arquivo1)
