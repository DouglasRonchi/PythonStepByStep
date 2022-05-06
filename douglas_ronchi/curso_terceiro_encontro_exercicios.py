import re

# 1 - Com Regex, conseguir mostrar o CPF 012.345.678-90 desta forma: 01234567890
# 2 - Faça um validador de Passwords aonde o usuario digite o seu password e o seu programa deve validar se é um password válido ou não, para isso use as regras:
# 	a - Deve conter mais de 8 caracteres
# 	b - Deve conter ao menos uma Letra Maiúscula
# 	c - Deve conter ao menos 2 numeros
# 	d - Deve conter pelo menos 1 caractere especial
# 	e - deve conter pelo menos 2 letras minusculas
# 3 - Na frase 'avistamos estáticos o elastico e o plastico' quero retornar os caracteres "a" ou "e" ou "i" que estejam seguidos de "st". Monte esta expressão utilizando Regex

# 1:


# cpf = "012.345.678-90"
#
# get_list = re.findall("\d", cpf)
# cpf_clean = "".join(get_list)
#
# print(f"cpf: {cpf_clean}")






# 2:
password = input("Digite uma senha: ")


def is_valid_password(password):
    pontos = 0
    mensagem = []
    valid = True
    # 	a - Deve conter mais de 8 caracteres
    if len(password) < 8:
        mensagem.append("Password deve conter mais de 8 caracteres")
        print(f"TOTAL DO PASSWORD = {pontos}")
        valid = False
    pontos += 2
    # 	b - Deve conter ao menos uma Letra Maiúscula
    if len(re.findall("[A-Z]", password)) < 1:
        mensagem.append("Password deve conter ao menos uma Letra Maiúscula")
        print(f"TOTAL DO PASSWORD = {pontos}")
        valid = False
    pontos += 2
    # 	c - Deve conter ao menos 2 numeros
    if len(re.findall("\d", password)) < 2:
        mensagem.append("Password deve conter ao menos 2 numeros")
        print(f"TOTAL DO PASSWORD = {pontos}")
        valid = False
    pontos += 4
    # 	d - Deve conter pelo menos 1 caractere especial
    if len(re.findall("\W", password)) < 1:
        mensagem.append("Password deve conter pelo menos 1 caractere especial")
        print(f"TOTAL DO PASSWORD = {pontos}")
        valid = False
    pontos += 2
    # 	e - deve conter pelo menos 2 letras minusculas
    if len(re.findall("[a-z]", password)) < 2:
        mensagem.append("Password deve conter pelo menos 2 letras minusculas")
        print(f"TOTAL DO PASSWORD = {pontos}")
        valid = False
    pontos += 2
    print(f"TOTAL DO PASSWORD = {pontos}")
    if valid:
        return True
    else:
        print(mensagem)
        return False


if is_valid_password(password):
    print(f"{password} é um password válido!")
else:
    print(f"{password} não é um password válido!")



# # 3:
# st = "st"
# frase = f'avi{st}amos e{st}áticos o ela{st}ico e o pla{st}ico'
#
# resultado = re.findall('(a|e|i)st', frase)
# print(resultado)
