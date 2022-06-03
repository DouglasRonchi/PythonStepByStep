"""
Orientação a Objeto Simples

"""
import os
from time import sleep
from typing import NoReturn
from uuid import uuid4

from pydantic import BaseModel


class Customer(BaseModel):
    id: str
    name: str


customers = [Customer(**{"id": "1", "name": "Douglas"})]


class Repository:
    @staticmethod
    def validate_customer() -> NoReturn:
        if len(customers) == 0:
            print("Nenhum customer cadastrado!")

    @staticmethod
    def create_customer() -> NoReturn:
        id_customer = str(uuid4())[0:5]
        name = input("Nome do customer: ").strip()
        customers.append(Customer(**{"id": id_customer, "name": name}))
        print(f"Cliente {name} cadastrado com sucesso!")

    @staticmethod
    def list_customers() -> NoReturn:
        [print(f"{customer.id} - {customer.name}") for customer in customers]

    @staticmethod
    def update_customer() -> NoReturn:
        print("Atualizar dados de um customer")
        id_customer = input("Digite o id do customer que deseja alterar: ").strip()
        changed = None
        for customer in customers:
            if id_customer == customer.id:
                name = input(f"Você quer alterar o name de {customer.name} para qual name ? ").strip()
                customer.name = name
                print(f"Cliente {id_customer} changed com sucesso!")
                break
        if not changed:
            print(f"Id {id_customer} não encontrado!")

    @staticmethod
    def delete_customer() -> NoReturn:
        print("Deletar um customer")
        id_customer = input("Digite o id do customer que deseja deletar: ").strip()
        deleted = None
        for customer in customers:
            if id_customer == customer.id:
                index = customers.index(customer)
                deleted = customers.pop(index)
                print(f"Cliente {id_customer} deletado com sucesso!")
                break
        if not deleted:
            print(f"Id {id_customer} não encontrado!")


class Program:
    def __init__(self):
        self.repo = Repository

    def show_exit_message(self) -> NoReturn:
        print(f"Saindo do sistema em ", end=" ")
        for i in range(3, 0, -1):
            print(f"{i}... ", end=" ")
            sleep(1)

    def is_running(self) -> bool:
        menu = self.show_menu_options()
        match menu:
            case 1:
                self.repo.create_customer()
                return True
            case 2:
                self.repo.validate_customer()
                self.repo.list_customers()
                return True
            case 3:
                self.repo.validate_customer()
                self.repo.update_customer()
                return True
            case 4:
                self.repo.validate_customer()
                self.repo.delete_customer()
                return True
            case 0:
                self.show_exit_message()
                return False
            case _:
                print("Opção inválida!")
                return True

    def clear_screen(self):
        os.system('cls')

    def show_menu_options(self) -> int:
        print("\n")
        print("=============================")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Sair")
        return int(input("O que você deseja fazer ? ").strip())

    def start(self):
        print("###########    Sistema de Cadastro de Clientes    ###########")
        while True:
            if not self.is_running():
                break


Program().start()
