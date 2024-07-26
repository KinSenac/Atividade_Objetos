def Cadastrar_cliente():
    id = int(input("Digite seu ID:  "))
    nome = input("Digite seu nome:  ")
    email = input("Digite seu email:  ")
    telefone = input("Digite o seu telefone:  ")
    endereço = input("Digite o seu endereço:   ")
    with open('clientes.txt', 'w') as arquivo:
        arquivo.write((f"Seu ID é {id} ,o seu nome é {nome} o seu email é {email} , seu telefone é {telefone} e o seu endereço {endereço} "))
        print("Cliente cadastrado")

while True:
    Cadastrar_cliente()
    continuar = input("Cadastrar outro usuario para sim digite (s), para não digite (n)")
    if continuar.lower()!= 's':
        break







# Crie um módulo para cadastrar clientes. Cada cliente deve ter um ID, nome, email, telefone e endereço. Os dados devem ser armazenados em um arquivo clientes.txt. 