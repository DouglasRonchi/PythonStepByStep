import re

# Strings

frase = "   hoje, é dia 1 de Abril, o dia da Mentira!, que legal,Abril eu tenho 29 anos    "
nome = "Arara"


# Inverter Frase:
# print(frase[::-1])

# Operações de string

# Para Maiusculas
# print(frase.upper())

# Para minusculas
# print(frase.lower())

# Joga a primeira letra da frase para Maiuscula
# print(frase.capitalize())

# Joga todas as palavras com a inicial maiuscula
# print(frase.title())

# Remove os espaçoes em branco no inicio e no final da frase
# print(frase.strip())

# Fatia a frase pelo valor do parametro e joga em uma lista
# lista_da_minha_frase = frase.split(",")

# lista = ["Alo", " ", "Brasil", "!"]

# frase_de_lista = "".join(lista)

# print(frase_de_lista)

# Buscar somente Digitos
# resultado = re.findall("\d", frase)


# resultado = re.findall("\D", frase)
# cpf = "000.000.000-00"
# resultado = re.findall("[0-9]", cpf)

# print(resultado)


# posicao = frase.find("Abril")
#
# print(posicao)
# print(frase[20:25])
# email = "test@test.com"
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#
# print(email)
# if re.search(regex, email):
#     print("É um email Válido")
# else:
#     print("Não é um email válido")

# PEP8 regras básicas
