class registro_de_vendas:
    def __init__(self):
        self.idvenda = input("Digite ID da venda: ")
        self.idproduto = input("Digite ID do produto: ")
        self.idcliente = input("Digite ID do cliente: ")
        self.qtd = input("Digite a quantidade: ")
        self.data = input("Digite a data: ")
        
    def GravarTXT(self, registro):
        caminho = 'C:/Users/horlab208/Documents/Danilo Aires/Exercicios danilo/Orientação objeto/vendas.txt'
        arquivo = open(caminho,'a')
        arquivo.write("ID venda: " + registro.idvenda + '\nID Produto: ' + registro.idproduto + '\nID Cliente: ' + registro.idcliente + '\nQuantidade: ' + registro.qtd + '\nData: ' + registro.data + '\n-----------\n')
        arquivo.close()

while True:
    op = input("Deseja registrar nova venda? S/N ")
    if op == 'n' :
        break
    else:
        registro = registro_de_vendas()
        registro.GravarTXT(registro)
