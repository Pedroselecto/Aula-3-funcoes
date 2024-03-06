# EXERCÍCIO 1: Faça uma função media(), que recebe os parâmetros posicionais ap1, ap2 e ac, e retorne a média de avaliações, utilizando a fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.

"""
Esse é o que eu fiz


def media():
    ap1 = float(input("Nota da ap1: "))
    ap2 = float(input("Nota da ap2: "))
    ac = float(input("Nota da ac: "))
    media = (ap1 + ap2) * 0.4 + ac * 0.2
    print("Sua média é", media)

media()
"""

"""

Esse é o que o professor fez


def media(ap1, ap2, ac):
    return(ap1 + ap2) * 0.4 + ac *0.2

def main():
    print(media(8, 7, 5))
    print(media(6, 6, 6))
    print(media(10, 0, 0))

main()
"""

# EXERCÍCIO 2: Monte um conversor de temperatura, que recebe uma temperatura em graus Fahrenheit e devolva a temperatura em graus Celsius. A fórmula para conversão é C / 5 = (F - 32) / 9.

def conversor(fahren):
    return(5/9) * (fahren - 32) #5/9 porque nós queremos descobrir o C, entao passamos ele para o lado multiplicando, ou seja, a fórmula que antes era C / 5 = (F - 32) / 9, se torna C = (5 / 9) * (F - 32)

def main():
    print(conversor(212))
    print(conversor(32))

main()

    