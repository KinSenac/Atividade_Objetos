#Crie um codigo para registrar pagamentos de faturas. Cada pagamento deve ter um ID, data, ID da fatura, valor pago e ID do cliente. 
#Os dados devem ser armazenados em um arquivo pagamentos.txt.

lista=[]

class Pagamento:
    def __init__(self, id_pagamento, valor_pago, id_cliente, id_data, id_fatura):
        self.id_pagamento = id_pagamento
        self.valor_pago = valor_pago
        self.id_cliente = id_cliente
        self.id_fatura = id_fatura 
        self.id_data = id_data
        
    def escrever (self,arquivo):
        arquivo.write("\n"+ "-"*30 + "\n" + "ID DO CLIENTE: " + self.id_cliente + "\n" + "ID do pagamento: " + self.id_pagamento + "\n" + " VALOR PAGO " + str (self.valor_pago) + "\n" + "DATA " + self.id_data + "\n" + "FATURA" + str (self.id_fatura) +"\n" + "-"*30 + "\n" )

        
    
    
while True:
    
    id_pagamento =  input ("Digite o ID do pagamento:")
    valor_pago = float(input("Digite o valor pago:"))
    id_cliente = input("Digite o nome do cliente: ")
    Id_data = input("Digite a data da fatura: ")
    id_fatura =int(input("Digite a fatura:"))
    if id_fatura < 0:
        break 
    else:
        lista.append(Pagamento(id_pagamento,valor_pago, id_cliente, Id_data, id_fatura))

nome = "C:/Users/horlab208/Desktop/exercicio 15/pagamentos.txt"
arquivo = open(nome,"w")

for i in lista:
    i.escrever(arquivo)
