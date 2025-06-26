# Lista que armazenará os produtos. Cada produto será uma tupla (nome, código, data)
estoque = []

# Loop principal do sistema, que continua até o usuário escolher sair (opção 4)
while True:
    # Menu de opções exibido ao usuário
    opcao_usuario = int(input("""\033[34m\nQual operação deseja realizar?

[1] -> Cadastrar produto
[2] -> Remover produto              
[3] -> Consultar estoque
[4] -> Sair do sistema                    
\nDigite um número de 1 a 4!\n
Opção: \033[m"""))

    # ---------------------- OPÇÃO 1: CADASTRAR PRODUTO ----------------------
    if opcao_usuario == 1:
        # Pergunta quantos produtos o usuário deseja cadastrar
        quantidade = int(input("Quantos produtos deseja cadastrar? "))
        
        # Para cada produto, coleta os dados e adiciona ao estoque
        for i in range(quantidade):
            produto = input("Digite o nome do produto: ")
            codigo = input("Digite o código do produto: ")
            data = input("Digite a data do cadastro: ")

            # Cria uma tupla com as informações do produto
            item = (produto, codigo, data)

            # Adiciona o produto à lista de estoque
            estoque.append(item)

    # ---------------------- OPÇÃO 2: REMOVER PRODUTO ----------------------
    elif opcao_usuario == 2:
        # Verifica se o estoque está vazio
        if not estoque:
            print("\nEstoque vazio!\n")
        else:
            # Mostra os produtos no estoque
            print("\nProdutos no estoque:")
            for item in estoque:
                print(item)

            # Pede o nome do produto a ser removido
            remover = input("\nDigite o nome do produto a remover: ")

            # Assume que o produto ainda não foi encontrado
            encontrado = False

            # Percorre o estoque procurando o produto pelo nome (posição 0 da tupla)
            for item in estoque:
                if item[0] == remover:
                    estoque.remove(item)     # Remove o item do estoque
                    encontrado = True        # Marca como encontrado
                    print("\nProduto removido com sucesso!\n")
                    break                    # Interrompe o laço (só remove o primeiro encontrado)

            # Caso o produto não tenha sido encontrado na lista
            if not encontrado:
                print("\nProduto não encontrado.\n")

    # ---------------------- OPÇÃO 3: CONSULTAR ESTOQUE ----------------------
    elif opcao_usuario == 3:
        # Verifica se há produtos no estoque
        if not estoque:
            print("\nEstoque vazio.\n")
        else:
            print("\nProdutos cadastrados no estoque:\n")
            for item in estoque:
                nome, codigo, data = item
                total = len(estoque)
                print(f"Produto: {nome} | Código: {codigo} | Data: {data}")
                print(f"\nQuantidade total de produtos no estoque: {total}\n")
            print("")  # Linha em branco para espaçamento

    # ---------------------- OPÇÃO 4: SAIR DO SISTEMA ----------------------
    elif opcao_usuario == 4:
        print("\033[1;31m\nSaindo do sistema... Até logo!\n\033[m")
        break  # Encerra o loop e finaliza o programa

    # ---------------------- OPÇÃO INVÁLIDA ----------------------
    else:
        print("\033[1;31m\nOpção inválida! Por favor, escolha entre 1 e 4.\n\033[m")