def exibir_historico(cliente_id, arquivo='atividade_em_grupo.py/vendas.txt'):

    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
        
        if not linhas:
            print("O arquivo está vazio.")
            return

        historico_encontrado = False
        for linha in linhas:

            campos = linha.strip().split(',')

            if len(campos) != 5:
                print("Formato de linha inválido:", linha)
                continue
            
            id_cliente, data, produto, quantidade, valor = campos

            if id_cliente == cliente_id:
                print(f"Data: {data}, Produto: {produto}, Quantidade: {quantidade}, Valor: {valor}")
                historico_encontrado = True

        if not historico_encontrado:
            print(f"Nenhuma compra encontrada para o cliente ID {cliente_id}.")
    
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


exibir_historico('1')  
