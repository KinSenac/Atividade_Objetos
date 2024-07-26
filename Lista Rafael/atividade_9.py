""" ANDRÉ MARTINS BRANDÃO ™
Atividade 9: Controle de Estoque Mínimo
Implemente uma função para verificar se a quantidade em estoque de um produto está abaixo de um valor mínimo 
e, se sim, registrar um alerta em um arquivo alertas.txt. 
"""
quantidade_estoque_minimo=2
def ControleEstoqueMinimo(quantidade_estoque_minimo,id_produto,quantidade_estoque):
    if quantidade_estoque<quantidade_estoque_minimo:
        nome_file = "alertas.txt"
        try:
            arquivo = open(nome_file, "a", encoding='utf-8')
            arquivo.write(f"{id_produto},{quantidade_estoque},ESTOQUE BAIXO\n")
            print(f"Alerta para o produto {id_produto} cadastrado com sucesso.") 
            arquivo.close()
        except FileNotFoundError:
            print(f"Arquivo {nome_file} não encontrado.") 

ControleEstoqueMinimo(quantidade_estoque_minimo,5,1)

