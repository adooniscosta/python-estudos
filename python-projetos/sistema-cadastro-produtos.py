produtos = []

def cadastrar_produto():
    nome = input('Nome do produto: ')
    preco = float(input('Valor do produto: '))
    quantidade = int(input('Quantidade: '))

    produto = {
        'nome': nome,
        'preco': preco,
        'quantidadade': quantidade
    }
    return produto


while True:
    print('=================================')
    print(' CADASTRO DE PRODUTOS')
    print('=================================')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Sair')
    while True:
        opcao = int(input('Escolha: '))
        if opcao == 1 or opcao == 2 or opcao == 3:
            break
        else:
            print('Opcão invalida! Digite 1 ou 2.')

    if opcao == 1:
         while True:
            produtos.append(cadastrar_produto())
            print('Produto cadastrado!')
            print('Deseja cadastrar um produto?')
            print('1 - Sim')
            print('2 - Voltar ao menu')
            escolha = int(input('Escolha: '))
            if escolha == 2:
                break
    elif opcao == 2:
        for produto in produtos:
            print(f'Produto: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidadade']}')
    elif opcao == 3:
        print('Programa encerrado!')
        quit()






