class Usuario:
    def __init__(self, x, nome, email, telefone):
        self.x = x
        self.nome = nome
        self.email = email
        self.telefone = telefone

a = input("Deseja cadastrar um usuário (S/N): ")

while a == 'S':
    arquivo = open('C:/Users/horlab208/Desktop/Kin/OO/listaRafael/usuarios.txt', 'a')

    b = Usuario(input("Digite seu id: "), input('Digite seu nome: '), input('Digite seu email: '), input("Digite seu telefone: "))
    
    arquivo.write("Usuario: " + b.x + '\nNome: ' + b.nome + '\nEmail: ' + b.email + '\nTelefone: ' + b.telefone + '\n---------------\n')
    arquivo.close()
    
    a = input("Deseja cadastrar um usuário (S/N): ")