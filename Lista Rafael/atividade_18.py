"""Atividade 18: Controle de Ponto Loidi 

Desenvolva um sistema de controle de ponto onde os funcionários devem registrar suas entradas e saídas. Os dados devem ser armazenados em um arquivo ponto.txt. """

class ControledePonto():
    def __init__(self, nome, entrada, saida):
        self.nome = nome
        self.entrada = entrada
        self.saida = saida

    def __str__(self):
        return f'Nome: {self.nome}\nEntrada: {self.entrada}\nSaida: {self.saida}'
    
    def escrever(self):
        with open('ponto2.txt', 'a') as arquivo:
            arquivo.write(f'{self.nome}\n{self.entrada}\n{self.saida}\
                              \n\n')
            arquivo.close()
            print('Dados gravados com sucesso!')

Ponto=ControledePonto (input("Digite seu nome: "), input("Digite horario de entrada: "), input("Digite horario da saida: ")) 
Ponto.escrever()       