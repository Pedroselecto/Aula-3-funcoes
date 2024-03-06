"""

Programação Estruturada
06/03/2024

Estruturas de decisão
- if/elif/else
- match/case
"""

def saudacao(turno):
    if turno == "M":
        print("Bom dia!")
    else:                     #else é como um "Senão". (Se turno não for = a M, printa o Boa tarde.)
        print("Boa tarde!")
saudacao("T")
saudacao("M")
saudacao("N")

print("-" * 30)

def saudacao(turno):
    if turno == "M":
        print("Bom dia!")
    elif turno =="T":         #elif serve para adicionar mais possibilidades.
        print("Boa tarde!")
    elif turno =="N":
        print("Boa noite!")
    else:
        print("Informação inválida")

saudacao("T")
saudacao("M")
saudacao("N")
saudacao("A")

print("-" * 30)

def saudacao2(turno):
    if turno== "M":
        return "Bom dia!"    #O return encerra o código, por isso não precisa do elif nas que estão abaixo.
    if turno == "T":
        return "Boa tarde!"
    if turno == "N":
        return "Boa noite!"
    
    return "Informação inválida!"  # Como o return encerra o código, o sistema já considera como se fosse um else logo antes. Pesquisar sobre depois.

print("-" * 30)

# Ternários
def e_par(num):
    return "É par" if num % 2 == 0 else "É ímpar"

def le_nome():
    nome = input("Informe o seu nome: ")
    if nome == "":
        print ("nome inválido")

    return nome

def avaliacao(conceito):
    if conceito == "Bom" or conceito == "Ótimo" or conceito == "Excelente":
        return "Aprovado"
    return "Reprovado"

def avaliacao2(conceito):
    match conceito:
        case "Bom":
            print("Aprovado")
        case "Ótimo":
            print ("Aprovado")
        case "Excelente":
            print("Aprovado")
        case _: #default case, opcional
            print("Reprovado")

def avaliacao3(conceito):
    match conceito:
        case "Bom" | "Ótimo" | "Excelente":
            print("Aprovado")
        case _:
            print("Reprovado")