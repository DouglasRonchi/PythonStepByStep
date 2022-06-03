"""
Com o sistema de customers criado, vamos alterar e colocar os nossos códigos em funções

"""
import os
from time import sleep
from typing import NoReturn
from uuid import uuid4

customers = [{"Id": "1", "Nome": "Douglas"}]

print("###########    Sistema de Cadastro de Clientes    ###########")


def validate_customer() -> NoReturn:
    if len(customers) == 0:
        print("Nenhum customer cadastrado!")


def create_customer() -> NoReturn:
    customer = {}
    id_customer = str(uuid4())[0:5]
    customer["Id"] = id_customer
    name = input("Nome do customer: ").strip()
    customer["Nome"] = name
    customers.append(customer)
    print(f"Cliente {name} cadastrado com sucesso!")


def list_customers() -> NoReturn:
    [print(customer) for customer in customers]


def update_customer() -> NoReturn:
    print("Atualizar dados de um customer")
    id_customer = input("Digite o id do customer que deseja alterar: ").strip()
    changed = None
    for customer in customers:
        if id_customer == customer.get('Id'):
            name = input(f"Você quer alterar o name de {customer.get('Nome')} para qual name ? ").strip()
            customer['Nome'] = name
            print(f"Cliente {id_customer} changed com sucesso!")
            break
    if not changed:
        print(f"Id {id_customer} não encontrado!")


def delete_customer() -> NoReturn:
    print("Deletar um customer")
    id_customer = input("Digite o id do customer que deseja deletar: ").strip()
    deleted = None
    for customer in customers:
        if id_customer == customer.get('Id'):
            index = customers.index(customer)
            deleted = customers.pop(index)
            print(f"Cliente {id_customer} deletado com sucesso!")
            break
    if not deleted:
        print(f"Id {id_customer} não encontrado!")


def show_exit_message() -> NoReturn:
    print(f"Saindo do sistema em ", end=" ")
    for i in range(3, 0, -1):
        print(f"{i}... ", end=" ")
        sleep(1)


def is_running() -> bool:
    menu = show_menu_options()
    match menu:
        case 1:
            create_customer()
            return True
        case 2:
            validate_customer()
            list_customers()
            return True
        case 3:
            validate_customer()
            update_customer()
            return True
        case 4:
            validate_customer()
            delete_customer()
            return True
        case 0:
            show_exit_message()
            return False
        case _:
            print("Opção inválida!")
            return True


def clear_screen():
    os.system('cls')


def show_menu_options() -> int:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")
    return int(input("O que você deseja fazer ? ").strip())


while True:
    if not is_running():
        break
