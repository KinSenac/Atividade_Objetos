'''Atividade 14: Relatório de Faturamento - LUCAS 

Desenvolva uma função para gerar relatórios de faturamento mensais.
Os relatórios devem incluir o total faturado e ser salvos em um arquivo relatorio_faturamento.txt.'''
import random

class FaturamentoMensal:

    def __init__(self, mes):
        self.mes = mes
        self.valor = []
        

    def GerarFaturamento(self):
        faturamento = random.randint(1000, 9999)
        self.valor.append(faturamento)


op = input('Deseja verificar o faturamento de algum MÊS? S/N ')

while op == 'S':

    faturamento = open('C:/Users/horlab208/Documents/LUCAS GUILHERME ROCHA DE ASSIS/ATIVIDADE RAFAEL/Atividade_Objetos/Lista Rafael/relatorio faturamento.txt', 'a')
    mesreferente = FaturamentoMensal(input('Digite o nome do MÊS que deseja verificar o FATURAMENTO: '))
    mesreferente.GerarFaturamento()
    faturamento.write(f'O MÊS SOLICITADO FOI: {mesreferente.mes}''\n'f'O FATURAMENTO FOI DE R$: {mesreferente.valor}')
    faturamento.close

    op = input('Deseja verificar o faturamento de algum MÊS? S/N ')