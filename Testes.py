import main

i = 1
while i <= 4:
    print(i)
    i = i + 1

i = 1
while i <= 15:
    print(i * "*")
    i = i + 4

def chegouNoFimPorFalha():
    global numero_de_erros
    numero_de_erros = numero_de_erros + 1
    if numero_de_erros < limite_de_erros:
        return False
    else:
        return True

def chegouNoFimPorFalha():
    repetição = numero_de_erros
    numero_de_erros = numero_de_erros + 1
    if numero_de_erros < limite_de_erros:
        return False
    else:
        return True