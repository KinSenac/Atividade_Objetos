import random
from datetime import datetime, timedelta

class Fatura:
    def __init__(self, itens_vendidos, quantidade, preco_total):
        self.id_venda = []
        self.id_cliente = []
        self.data_vencimento = []
        self.itens_vendidos = itens_vendidos
        self.quantidade = quantidade
        self.preco_total = preco_total

    def GerarIDVenda(self):
        idvenda = random.randint(1, 9999)
        self.id_venda.append(idvenda)
    
    def GerarIDCliente(self):
        idcliente = random.randint(10000, 99999)
        self.id_cliente.append(idcliente)

    def GerarDataVencimento(self):
        data_atual = datetime.now()      
        vencimento = data_atual + timedelta(days=10)
        self.data_vencimento = vencimento

    def ItensVendidos(self):
        itens = input('Digite o nome dos ITENS comprados: ')
        self.itens_vendidos = itens
        pass

    def Qtd(self):
        qtd = input('Digite a QUANTIDADE de itens comprados: ')
        self.quantidade = qtd
        pass

    def PrecoTotal(self):
        preco = int(input('Digite o valor total da compra R$: '))
        self.preco_total = preco
        pass

    def PegarIDVenda(self):
        pass

boleto = input('Deseja gerar um BOLETO? S/N: ')
while boleto == 'S':
    fatura = open('C:/Users/horlab208/Documents/LUCAS GUILHERME ROCHA DE ASSIS/ATIVIDADE RAFAEL/Atividade_Objetos/Lista Rafael/faturas.txt', 'a')
    vendas = Fatura(input('Digite o nome dos ITENS comprados: '), input('Digite a QUANTIDADE de itens comprados: '), int(input('Digite o valor total da compra R$: ')))
    vendas.GerarIDCliente()
    vendas.GerarIDVenda()
    vendas.GerarDataVencimento()
    fatura.write(f'"ID do CLIENTE": {vendas.id_cliente}''\n'f'ID da VENDA: {vendas.id_venda}''\n'f'ITENS COMPRADOS: {vendas.itens_vendidos}''\n'
                f'A QUANTIDADE foi de: {vendas.quantidade}''\n'f'O VALOR da FATURA é de R$: {vendas.preco_total}'
                '\n'f'O VENCIMENTO de sua FATURA é: {vendas.data_vencimento}' )
    fatura.close()

    boleto = input('Deseja gerar um BOLETO? S/N: ')