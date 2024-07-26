""" ANDRÉ MARTINS BRANDÃO ™
Desenvolva um sistema para registrar compras de produtos. Cada compra deve ter um ID, 
data, ID do fornecedor, ID do produto e quantidade comprada. Os dados devem ser armazenados em um arquivo compras.txt.
"""
class Compras:
    def __init__(self, id, data, id_fornecedor, id_produto, quantidade):
        self.id = id
        self.data = data
        self.id_fornecedor = id_fornecedor
        self.id_produto = id_produto
        self.quantidade = quantidade

    def GravarEmArquivo(self):
        nome_file = "compras.txt"
        try:
            arquivo = open(nome_file, "a", encoding='utf-8')
            arquivo.write(f"{self.id},{self.data},{self.id_fornecedor},{self.id_produto},{self.quantidade}\n")
            print(f"Dados Cadastrado com sucesso.") 
            arquivo.close()
        except FileNotFoundError:
            print(f"Arquivo {nome_file} não encontrado.") 

registrar_compra=Compras(int(input("Digite o ID: ")),input("Digite a Data: "),int(input("Digite o ID do fornecedor: ")),int(input("Digite o ID do produto: ")),int(input("Digite a Quantidade: ")))
registrar_compra.GravarEmArquivo()

