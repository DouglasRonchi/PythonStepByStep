from datetime import datetime
from math import sqrt as math_sqrt

print("Hello World!")

nome = "Douglas"
sobrenome = "Ronchi"
print(nome)
print(type(nome))

idade = 18
print(idade)
print(type(idade))

print("Com format -> Meu nome é {} {}".format(nome, sobrenome))
print(f"Com F String -> Meu nome é {nome} {sobrenome}")

# Operadores
modulo = 4 % 2
print(modulo)

exponenciacao = 2 ** 2
print(exponenciacao)

num1 = 2
num2 = 3

adicao = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
divisao_inteira = num1 // num2

# Ctrl+D -> Duplica a Linha
# Alt - J -> Seleciona os próximos conforme a seleção atual
# Ctrl + / -> Comenta a linha selecionada

print(f"Resultado da Adição {num1} + {num2} = {adicao}")
print(f"Resultado da subtracao {num1} + {num2} = {subtracao}")
print(f"Resultado da divisao {num1} + {num2} = {divisao}")
print(f"Resultado da divisao_inteira {num1} + {num2} = {divisao_inteira}")


adicao_str = str(num1) + str(num2)
print(f"Resultaddo da Adicão com strings = {adicao_str}")
print(type(adicao_str))

# Alt + ENTER -> Dá pra importar a lib
print(f"Data de hoje : {datetime.now()}")

raiz_quadrada = math_sqrt(num1)
print(f"Raiz quadrada de {num1} é igual a {raiz_quadrada}")


