# Exercício 2:

def exercicio(num1, num2):
    if num1 > num2:
        print(num1)
    elif num2> num1:
        print(num2)

exercicio(4, 5)

print("-" * 30)

# Exercicio 4:

def vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("vogal")
    else:
        print("Não é vogal")

vogal("u")

print("-" * 30)

# Exercício 5
# Esse é o que eu fiz:
def mediaf(ap1, ap2, ap3):
    total = ap1 + ap2 + ap3
    media = total / 6
    if media >= 7:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
    elif media == 10:
        print("Aprovado com distinção")
    else:
        print("Nota inválida")

# Esse é o do professor

def mediaf(ap1, ap2, ap3):
    media = (ap1 + ap2 + ap3) / 3
    if media < 0 or media < 10:
        print("Nota inválida")
    elif media >= 7:
        print("Aprovado")
    elif media == 10:
        print("Aprovado com distinção")
    else:
        print("Reprovado")



