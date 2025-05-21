# Lista para armazenar os produtos
estoque = []

# Função para adicionar produto
def adicionar_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(produto)
    print(f"Produto {nome} adicionado com sucesso!")

# Função para listar produtos
def listar_produtos():
    """
    Exibe a lista de produtos no estoque.

    Se o estoque estiver vazio, informa ao usuário. Caso contrário, exibe cada produto com seu nome, quantidade e preço formatado.
    """
    if not estoque:
        print("Estoque vazio.")
    else:
        for i, produto in enumerate(estoque):
            print(f"{i+1}. {produto['nome']} - Qtd: {produto['quantidade']} - Preço: R${produto['preco']:.2f}")

# Função para remover produto
def remover_produto():
    listar_produtos()
    if estoque:
        try:
            indice = int(input("Digite o número do produto para remover: ")) - 1
            if 0 <= indice < len(estoque):
                removido = estoque.pop(indice)
                print(f"Produto {removido['nome']} removido.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Função para exibir o menu
def exibir_menu():
    print("\n1. Adicionar produto")
    print("2. Listar produtos")
def menu():
    """
    Displays the main menu and handles user input to perform actions
    such as adding, listing, or removing products from the inventory.
    """
    print("4. Sair")

# Função principal do menu
def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()