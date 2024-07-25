import cryptocode

chave = "423338233093093"


# MensagemCriptografada = cryptocode.encrypt(mensagem, chave)
# MensagemDescriptografada = cryptocode.decrypt(MensagemCriptografada, chave)



class Login:
    def __init__(self, email, senha):
        self.email = email
        self.senha = cryptocode.encrypt(senha, chave)
    
a = input("Deseja realizar login (S/N): ")

while a == 'S':
    arquivo = open('C:/Users/horlab208/Desktop/Kin/OO/listaRafael/auth.txt', 'a')

    b = Login(input("Digite seu email: "), input('Digite sua senha: '))
    
    arquivo.write("Email: " + b.email + '\nSenha: ' + b.senha + '\n---------------\n')
    
    arquivo.close()
    
    a = input("Deseja realizar login (S/N): ")
    
    