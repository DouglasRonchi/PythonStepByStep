# Funções

# Definir casas decimais
from functools import reduce
from typing import Union, List, Dict, Tuple

numero__um_float = 6
numero_dois_float = 8
resultado = numero_dois_float / numero__um_float
# print(f"Resultado {resultado:.4f}")


# print("Chamei a função")


# Chamar função e seu retorno / ou não | Escopo de variaveis
def chamar_funcao(number: int) -> List:
    match number:
        case 1:
            return []
        case _:
            return []
#
# print(chamar_funcao(1))


# nome = "Jose"
# def teste_escopo():
#     nome = "Douglas"
#     print(nome)
#
# teste_escopo()


# Parametros e TypeHints


# Type Hint de Saida


# Parametros com valores padrão

# def teste(nome: str = "DEFALUT") -> str:
#     return nome
#
# print(teste("Douglas"))

# defauld avaliados apenas uma vez

# def buffer(num, buff=[]):
#     buff.append(num)
#     print(buff)
#
#
# buffer(1)
# buffer(2)
# buffer(3)


# Args e Kwargs

# def media(*notas):
#     print(sum(notas) / float(len(notas)))
#
#
# notas = [10, 9, 8, 7]
# media(2, 6)
# media(2, 8)
# media(*notas)
#
# kwargs_for_method = {"name": "James", "age": 23, "telefone": "333333333"}
#
#
# def media(**kwargs):
#     print(kwargs.get('name'))
#     print(kwargs.get('age'))
#     print(kwargs.get('telefone'))
#
#
# media(**kwargs_for_method)

# Todas retornam algum valor (None = False)


# def funcao(chave: bool):
#     if chave:
#         print("Alguma coisa")
#         return "True"
#     print("Outra coisa")
#     return "False"
#
# print(funcao(False))
#
#



# lambda

# res = lambda x: x + 2


# print([(lambda x: x + 2)(x) for x in range(3)])


# print(res(1, 4))


# Map reduce e filter
# Map faz uma funcao para cada item seq (lista, tupla):
pow_2 = lambda a: a ** 2
# print(list(map(pow_2, [2, 4, 10, 100, 20])))
# TODO Trazer exemplo utilizado em algum projeto

# reduce:
# Função interna que aplica a função sobre o valor corrente retornado pela função anterior (func) junto com o próximo item da lista.
# retorna:  (((((1+2)+3)+4)+5) = 15

# soma = lambda a, b: a + b
# print(reduce(soma, [1, 2, 3, 4, 5]))


# filter:
# filtro = lambda a: a % 2 != 0
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list(filter(filtro, numeros)))




# Enumerate
# values = ["a", "a", "b", "c", "d"]
# for count, value in enumerate(values, start=0):
#     print(f"{count} {value}")


# Yield
def create_generator():
    mylist = range(30)
    for i in mylist:
        yield i * i


print(list(create_generator()))
