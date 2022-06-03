"""
Dependências:
Criando ambientes virtuais para projetos Python com o Virtualenv

Como instalar uma dependência com PIP e usar em seu projeto
install
install -r requirements.txt

Remover pacotes:
freeze
uninstall


Ordem de Imports :
1 - Bibliotecas padrão da linguagem Python (sem necessidade de instalação)
2 - Bibliotecas de terceiros (instalável a partir de algum repositório)
3 - Bibliotecas/módulos próprios (criados pelo próprio desenvolvedor)

TypeHints Referência !
"""

# import re
# from math import cos, sin, pi

# import pandas

# from models.modelo import Model

# Orientação a Objetos

# Declarando classes

#
# class Pessoa:
#     pass
#
#
# # Atributos e métodos da classe
#
#
# class PessoaFisica:
#     pass
#     # Atributos e métodos da classe
#

# Construtor

# class Pessoa:
#     def __init__(self, nome: str, sexo, cpf: str):
#         self.nome = nome
#         self.sexo = sexo
#         self.cpf = cpf
#
#
# pessoa = Pessoa("Fulano", "M", "024584215")
# print(pessoa.nome)

# print("123125452".zfill(4))

#
# # Instanciando
#
# class Pessoa:
#     def __init__(self, nome, sexo, cpf):
#         self.nome = nome
#         self.sexo = sexo
#         self.cpf = cpf
#
#
# if __name__ == "__main__":
#     pessoa1 = Pessoa("João", "M", "123456")
#     print(pessoa1.nome)


# # Métodos

# class Pessoa:
#     def __init__(self, nome, sexo, cpf, ativo: bool = False):
#         self.nome = nome
#         self.sexo = sexo
#         self.cpf = cpf
#         self.ativo = ativo
#
#     def mudar_o_status(self, ativar_ou_nao: bool):
#         self.ativo = ativar_ou_nao
#         print("A pessoa foi desativada com sucesso")
#
#
# if __name__ == "__main__":
#     pessoa1 = Pessoa("João", "M", "123456", True)
#     pessoa1.mudar_o_status(True)
#     print(pessoa1.ativo)
#
# # Atributos Protegidos
from math import cos, sin, pi

"""
Ativo é acessivel por todo mundo

Public: Atributos e métodos definidos como públicos poderão ser invocados, acessados e modificados através
 de qualquer lugar do projeto;

Private: Atributos e métodos definidos como privados só poderão ser invocados, acessados e modificados
 somente por seu próprio objeto.

Protected: Atributos e métodos definidos como protegidos só poderão ser invocados, acessados e modificados
por classes que herdam de outras classes através do conceito de Herança, visto na última aula. Sendo assim,
 apenas classes “filhas” poderão acessar métodos e atributos protegidos.

No Python, diferente das linguagens completamente voltadas ao paradigma da orientação à objetos (Java, C#, etc.),
 estes atributos existem, mas não da forma “convencional”.
"""
#
#
# class Pessoa:
#     def __init__(self, nome, sexo, cpf):
#         self.nome = nome
#         self.sexo = sexo
#         self.cpf = cpf
#
#     def desativar(self):
#         self.__ativo = False
#         print("A pessoa foi desativada com sucesso")
#
#
# if __name__ == "__main__":
#     pessoa1 = Pessoa("João", "M", "123456")
#     pessoa1.desativar()

# # Getters and setters
# """
# caso precisemos acessar os atributos privados de uma classe,
# o Python oferece um mecanismo para construção de propriedades em uma classe
# """
#
#
# class Pessoa:
#     def __init__(self, nome, sexo, cpf, ativo):
#         self.__nome = nome
#         self.__sexo = sexo
#         self.__cpf = cpf
#         self.__ativo = ativo
#
#     def desativar(self):
#         self.__ativo = False
#         print("A pessoa foi desativada com sucesso")
#
#     def get_nome(self):
#         return self.__nome
#
#     def set_nome(self, nome):
#         self.__nome = nome
#
#
# if __name__ == "__main__":
#     pessoa1 = Pessoa("João", "M", "123456", True)
#     pessoa1.desativar()
#     pessoa1.__ativo = True
#     print(pessoa1.ativo)
#
#     # Utilizando geters e setters
#     pessoa1.set_nome("José")
#     print(pessoa1.get_nome())
#
# # Herança
"""
A Herança é um conceito do paradigma da orientação à objetos que determina que
uma classe (filha) pode herdar atributos e métodos de uma outra classe (pai) e, assim,
evitar que haja muita repetição de código.
"""

# class Animal:
#     def __init__(self, nome, cor):
#         self.__nome = nome
#         self.__cor = cor
#
#     def comer(self):
#         print(f"O {self.__nome} está comendo")
#
#
# class Gato(Animal):
#     def __init__(self, nome, cor):
#         super().__init__(nome, cor)
#
#
# class Cachorro(Animal):
#     def __init__(self, nome, cor):
#         super().__init__(nome, cor)
#
#
# class Coelho(Animal):
#     def __init__(self, nome, cor):
#         super().__init__(nome, cor)
#
#
# gato = Gato("Bichano", "Branco")
# cachorro = Cachorro("Totó", "Preto")
# coelho = Coelho("Pernalonga", "Cinza")
#
# gato.comer()
# cachorro.comer()
# coelho.comer()
#
# Polimorfismo
# """
# Polimorfismo, em Python, é a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua
# superclasse, e o programa saber qual método deve ser invocado, especificamente (da super ou sub).
# """
#
#
# class Super:
#     def hello(self):
#         print("Olá, sou a superclasse!")
#
#     def hello_world(self):
#         print("Olá, sou a hello_world!")
#
#
# teste = Super()
# teste.hello()
#
#
# class Sub(Super):
#     def olaola(self):
#         print("Olaola")
#
#     def hello(self):
#         print("Olá, sou a subclasse!")
#
#
# teste = Sub()
# teste.hello()
#
#
# class Subsub(Sub):
#     def hello(self):
#         print("Olá, sou a subsubclasse!")
#
#
# teste = Subsub()
# teste.hello_world()


#
# ##################################################################################
#
# # StaticMethod e ClassMethod
# Class
"""
Eles têm acesso ao estado da classe, pois recebe um parâmetro de classe que aponta para a
classe e não para a instância do objeto.

Ele pode modificar um estado de classe que se aplicaria a todas as instâncias da classe.
"""
# Static
"""

"""
from datetime import date


# class Name:
#     def __init__(self, name):
#         self.string_name = name
#
#
# class Person:
#     def __init__(self, name: Name, age):
#         self.name = name
#         self.age = age

    # @classmethod
    # def from_birth_year(cls, name, year):
    #     return cls(name, date.today().year - year)
    #
    # @staticmethod
    # def is_adult(age):
    #     return age > 18

#
# douglas = Name("Douglas")
# person = Person(douglas, 21)
#
# print(person.name.string_name)

# person1 = Person('mayank', 21)
# person2 = Person.from_birth_year('mayank', 1996)
#
# print(person1.age)
# print(person2.age)
#
#
# print(Person.is_adult(22))

#
# # Usages
#
# # classmethod is mostly used for alternative constructors.
#
# # staticmethod does not use the state of the object, or even the structure of the class itself.
# # It could be a function external to a class. It only put inside the class for grouping functions
# # with similar functionality (for example, like Java's Math class static methods)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def frompolar(cls, radius, angle):
#         """The `cls` argument is the `Point` class itself"""
#         return cls(radius * cos(angle), radius * sin(angle))
#
#     @staticmethod
#     def angle(x, y):
#         """this could be outside the class, but we put it here
#             just because we think it is logically related to the class."""
#         return y - x
#
#
# p1 = Point(3, 2)
# p2 = Point.frompolar(3, pi/4)
#
# print(p1.x)
# print(p2.x)
#
# angle = Point.angle(3, 2)
# print(angle)
