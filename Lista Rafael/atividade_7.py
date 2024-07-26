'''
Atividade 7: Cadastro de Fornecedores - KENZO 
Crie um módulo para cadastrar fornecedores. 
Cada fornecedor deve ter um ID, nome, email, telefone e endereço. 
Os dados devem ser armazenados em um arquivo fornecedores.txt. 
'''

class Empresa:
    def __init__(self):
        self.fornecedores = []
    
    def Adicionar_Fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)
    
    def Cadastrar_Fornecedor(self):
        id = input("Digite o id do Fornecedor: ")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")
        endereco = input("Digite o endereço: ")
        fornecedor = Fornecedores(id, nome, email, telefone, endereco)
        empresa1.Adicionar_Fornecedor(fornecedor)
    
    def Visualizar_Fornecedor(self):
        for i in self.fornecedores:
            print(f"ID: {i.id}\nNome: {i.nome} \nEmail: {i.email} \nTelefone: {i.telefone} \nEndereço: {i.endereco}")
    
    def salvar_fornecedores_em_arquivo(self, nome_arquivo):
        caminho = "C:/Users/horlab208/Desktop/teste Atividade Rafael"
        caminho_completo = caminho + nome_arquivo
        with open(caminho_completo, 'a') as arquivo:
            for fornecedor in self.fornecedores:
                arquivo.write(f"ID: {fornecedor.id}\n")
                arquivo.write(f"Nome: {fornecedor.nome}\n")
                arquivo.write(f"Email: {fornecedor.email}\n")
                arquivo.write(f"Telefone: {fornecedor.telefone}\n")
                arquivo.write(f"Endereço: {fornecedor.endereco}\n")
                arquivo.write("-" * 40 + "\n")

class Fornecedores:
    def __init__(self, id, nome, email, telefone, endereco):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
   
empresa1 = Empresa()

while True:   
    opcao = input("Deseja Cadastrar Fornecedor? (S/N) ").lower()

    if opcao == "s":
        empresa1.Cadastrar_Fornecedor()
        empresa1.salvar_fornecedores_em_arquivo("Fornecedores.txt")
    elif opcao == "n":
        break
    else:
        print("Opção Inválida, Digite 'S' ou 'N'")
        



