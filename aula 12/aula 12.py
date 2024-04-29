"""
29/04/2024
09-Módulos e pacotes
SRP -> Singes responsibility principle
"""
# Pegar tudo no github do victor

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def main():
    n1 = float(input("Informe um número: "))
    oper = input("Informe a operação (+, -, *, /): ")
    n2 = float(input("Informe outro número: "))

    match oper:
        case "+":
            print(soma(n1, n2))

        case "-":
            print(subtracao(n1, n2))

        case "*":
            print(multiplicacao(n1, n2))

        case "/":
            print(divisao(n1, n2))