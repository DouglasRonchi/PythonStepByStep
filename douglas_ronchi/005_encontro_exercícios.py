"""
Crie um sistema de cadastro de clientes que seja possível, criar, listar, atualizar e deletar um cliente.

Sistema em DOS, utilizando o que aprendemos até agora, armazene em memória em um lista!

"""

clientes = []

while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    menu = input("O que você deseja fazer ? ")
    match menu:
        case "1":
            nome = input("Nome do cliente: ")
            cliente = {"Nome": nome}
            clientes.append(cliente)
            print(f"Cliente {nome} cadastrado com sucesso!")
        case "2":
            print([cliente for cliente in clientes])
            input("Pressione Enter para voltar...")
