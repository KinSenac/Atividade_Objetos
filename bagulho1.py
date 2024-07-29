class Produto:

    def __init__(self) :

        self.nome = input("Digite o nome do produto para adicionar: ")
        self.Id = input("Digite o Id do produto ")
        self.descricao = input("Digite a descrição do produto ")
        self.preco = float(input("Digite o preço do produto "))
        self.quantidade = int(input("Digite a quantidade do produto "))
    
    def GravarTXT(self):
        caminho = 'C:/Users/eskatista/Desktop/sópracontrariar/produtos.txt'
        with open(caminho, 'a') as arquivo:
            arquivo.write(f'{self.Id}, {self.nome}, {self.quantidade}, {self.preco}, {self.descricao}')


    def AtualizarQuantidade(self):
        ProdutoEncontrado = False
        caminho = 'C:/Users/eskatista/Desktop/sópracontrariar/produtos.txt'
        caminho_temp = 'C:/Users/eskatista/Desktop/sópracontrariar/temp_produtos.txt'

        Idproduto = input("Digite o Id do produto que foi vendido ")

        with open(caminho, 'r') as arquivo:
            for i in arquivo:
                self.Id, self.nome, self.quantidade = i.strip().split(', ')
                if self.Id == Idproduto:
                    ProdutoEncontrado = True
                    QtdVendida = int(input(f"Digite a quantidade de {self.nome} que foi vendida "))
                    self.quantidade -= QtdVendida
                    arquivo.write(f'{self.nome}, {self.Id}, {self.preco}, {self.nova_quantidade}, {self.descricao}\n')
                produto_encontrado = True
                    

        if not ProdutoEncontrado:
            print("Produto não encontrado")

while True:
    op = input("Deseja cadastrar produto(S/N): ")
    if op == 'N':
        break
    else:
        produto = Produto()
        produto.GravarTXT()
        produto.AtualizarQuantidade()
