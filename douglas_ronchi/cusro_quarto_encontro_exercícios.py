# Exercícios

# Crie uma conta no github caso não tenha, e crie um repositório lá com o nome do nosso projeto, no próximo encontro
# vamos subir esses arquivos
"""
Para subir os arquivos, devemos clonar nosso repositorio para nossa máquina:
no terminal rode:
git clone *link para o projeto* (sem os * ok ?)

Aí copie os seus arquivos para dentro desta pasta e rode:

- Adiciona todos os arquivos no commit
git add .

- Empacota os arquivos para enviar para o gi
git commit -m"Primeira Subida no GitHub"

- Envia os arquivos commitados (Empacotados) para o GitHub
git push

"""

# Escreva uma função chamada cumsum que receba uma lista de números e retorne
# a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma
# dos primeiros i+1 elementos da lista original. Por exemplo:
#
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

# HandsOn
"""
Podemos fazer na mão usando yield (É um return, mas diferente, fica aí a pesquisa :P)
"""
def cumsum(lis):
    def acumu(lis):
        total = 0
        for x in lis:
            total += x
            yield total

    return list(acumu(lis))


resultado = cumsum([1, 2, 3])

print(resultado)

# With NumPy
"""
Ou podemos usar o pacote numpy - Lembre-se que não precisamos reinventar a roda
"""
import numpy as np

resultado_numpy = np.cumsum([1, 2, 3])

print(resultado_numpy)

# Escreva uma função chamada is_sorted que tome uma
# lista como parâmetro e retorne True se a lista estiver
# classificada em ordem ascendente, e False se não for o caso. Por exemplo:

# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False
# LINGUAGEM DE REFERENCIA
"""
Utilizamos o deepcopy por que ele faz uma cópia sem referencia, o python é uma linguagem de referencia
ou seja, ele referencia um local na memória para as variáveis, experimente retirar o deepcopy, e a função 
não funcionará conforme o esperado, vou falar mais sobre isso ainda!
"""
from copy import deepcopy

lista_sorted = [1, 2, 2]
lista_non_sorted = ['b', 'a']

def is_sorted(lista: list):
    lista_de_varificacao = deepcopy(lista)
    lista.sort()
    return lista == lista_de_varificacao

print(is_sorted(lista_sorted))
print(is_sorted(lista_non_sorted))

# Escreva uma função chamada has_duplicates que tome uma lista e retorne True
# se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.

"""
Fiz duas funções, uma para mostrar como remover os duplicados com o set()
lembre {} é um set, e não aceita duplicados
{x for x in lista} esse modo é chamado de generators (Uma pesquisa básica já entende o conceito)
Mas basicamente ele gera um set, uma lista, uma tupla, etc... 
"""
def remove_duplicates(lista: list):
    return list({x for x in lista})

print(remove_duplicates([1, 2, 2, 3]))


"""
Então aqui eu verifico:
O len da lista
E o len dessa mesma lista transformada em set() (Que não aceita duplicados)
Se for diferente é por que tinha duplicados :)
"""
def has_duplicates(lista: list):
    return len(lista) != len(set(lista))

print(has_duplicates([1, 2, 2, 3]))

# Crie um dicionário que guarda 4 notas de alunos, e faça a média dessas notas

alunos = []
notas = []

# alunos.append(input("Digite o nome do aluno: "))
# notas.append(input("Digite a 1 nota do aluno: "))
# notas.append(input("Digite a 2 nota do aluno: "))
# notas.append(input("Digite a 3 nota do aluno: "))
# notas.append(input("Digite a 4 nota do aluno: "))
alunos = ["Douglas"]
notas = [2, 5, 7, 8]

resultado = {}
resultado['Nome'] = alunos[0]
resultado['Notas'] = [nota for nota in notas]

from statistics import mean
resultado['Media'] = mean(list([nota for nota in notas]))

print(resultado)
