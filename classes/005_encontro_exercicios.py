"""
Crie um sistema de cadastro de clientes que seja possível, criar, listar, atualizar e deletar um cliente.

Sistema em DOS, utilizando o que aprendemos até agora, armazene em memória em um lista!

"""
from time import sleep
from uuid import uuid4

# clientes = [{"Id": "1", "Nome": "Douglas"}]
clientes = []

print("###########    Sistema de Cadastro de Clientes    ###########")
while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")
    menu = input("O que você deseja fazer ? ").strip()
    match menu:
        case "1":
            cliente = {}
            id_cliente = str(uuid4())[0:5]
            cliente["Id"] = id_cliente
            nome = input("Nome do cliente: ").strip()
            cliente["Nome"] = nome
            clientes.append(cliente)
            print(f"Cliente {nome} cadastrado com sucesso!")
        case "2":
            if len(clientes) == 0:
                print("Nenhum cliente cadastrado!")
            [print(cliente) for cliente in clientes]
        case "3":
            print("Atualizar dados de um cliente")
            id_cliente = input("Digite o id do cliente que deseja alterar: ").strip()
            alterado = None
            for cliente in clientes:
                if id_cliente == cliente.get('Id'):
                    nome = input(f"Você quer alterar o nome de {cliente.get('Nome')} para qual nome ? ").strip()
                    cliente['Nome'] = nome
                    print(f"Cliente {id_cliente} alterado com sucesso!")
                    alterado = True
                    break
            if not alterado:
                print(f"Id {id_cliente} não encontrado!")
        case "4":
            print("Deletar um cliente")
            id_cliente = input("Digite o id do cliente que deseja deletar: ").strip()
            deletado = None
            for cliente in clientes:
                if id_cliente == cliente.get('Id'):
                    index = clientes.index(cliente)
                    deletado = clientes.pop(index)
                    print(f"Cliente {id_cliente} deletado com sucesso!")
                    break
            if not deletado:
                print(f"Id {id_cliente} não encontrado!")
        case "0":
            print("Saindo do sistema em 3...")
            sleep(1)
            print("Saindo do sistema em 3... 2...")
            sleep(1)
            print("Saindo do sistema em 3... 2... 1...")
            sleep(1)
            break

