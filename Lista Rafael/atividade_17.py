"""Atividade 17: Cadastro de Funcionários - Loidi 

Crie um módulo para cadastrar funcionários. Cada funcionário deve ter um ID, nome, cargo, email, telefone e salário. Os dados devem ser armazenados em um arquivo funcionarios.txt. """

class CadastrodeFuncionarios:
    def __init__(self, ID, nome, cargo, email, telefone, salario):
        self.ID = ID
        self.nome = nome
        self.cargo = cargo
        self.email = email
        self.telefone = telefone
        self.salario = salario
    
    def Cadastrar(self):
       caminho = 'C:/Users/horlab208/OneDrive - Serviço Nacional de Aprendizagem Comercial/Desktop/loidi/funcionarios.txt'
       arquivo = open(caminho, "a")
       arquivo.write(f"ID = {self.ID}\nNome = {self.nome}\nCargo = {self.cargo}\nEmail = {self.email}\nTelefone\n")
       arquivo.close()
    

cadastro=CadastrodeFuncionarios(int(input("Digite o ID: ")), input("Nome: "), input("Cargo: "), input("Email: "), input("Telefone: " ), float(input("Salario: ")))
#print(f"ID: {cadastro.ID}\nNome: {cadastro.nome}\nCargo: {cadastro.cargo}\nEmail: {cadastro.email}\nTelefone: {cadastro.telefone}\nSalario: {cadastro.salario}")   


cadastro.Cadastrar()

                                   