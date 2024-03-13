"""
Programaçao estruturada
2024.1
13/03/2024

- While -> quando não sabemos quantas vezes vamos executar a repetição.
- For -> Quando queremos acessar todos os elementos de uma coleção de dados.

"""


def contagem_regressiva(num):
    while num >= 0: #while faz a função se repetir enquanto a especificação escrita for verdadeira, nesse caso, o comando vai se repetir enquanto o número for maior ou igual a zero.
        print(num)
        num -= 1 # num = num -1

# contagem_regressiva(5)
# print ("-" * 30)

# Evitar loops infinitos

def contagem_regressiva3(num):
    for cont in range(num, -1, -1):
        print(cont)

contagem_regressiva3(3)
print("-" * 30)

print(list(range(5)))
print(list(range(2, 5))) 
print(list(range(1, 10, 2))) # conta de 1 a 10 indo de 2 em 2
print ("-" * 30)

def ola_varias_vezes(num):
    for _ in range(num):  # Não coloca a variável "cont" pois ela não teria utilidade e gastaria memória atoa, então usa o coringa "_" no lugar.
        print("olá")

ola_varias_vezes(5)
print("-" * 30)

def le_nomes():
    texto = "1" # Coisa aleatória só pra declarar a variável.
    while texto != "":
        texto = input("Informe o seu nome, ou digite um número: ")
        if texto.isnumeric():
            continue # interrompe o loop atual (volta pro while, logo, não chega no "print(texto)" e o texto não é imprimido)
        print(texto)

# le_nomes()

def le_nome():
    while True:
        nome = input("Informe o seu nome: ")
        if nome:
            break # Interrompe a estrutura de repetição. Usado para parar a repetição.
    print(nome)

# le_nome()

def e_primo(num):
    for div in range(2, num):  # Se não for primo, ele vai entrar no bloco onde o break está e não vai deixar o código chegar no "print(é primo)" e se for primo, ele vai passar direto e ir para o Else.
        if not num % div:
            print(num, "não é primo.")
            break
    else:
            print(num, "é primo.")
    print("Fim da função")

# e_primo(7)
# e_primo(8)
# e_primo(31)
# e_primo(56)

def conta_pares(min, max):
    if min % 2: # Indentificar se é par (módulo de 2)
        min += 1
    for num in range (min, max + 1, 2):
        if num >= max - 1:
            print(num)
        else:
            print(num, end=" - ")

conta_pares(2, 8) # 2 - 4 - 6 - 8
conta_pares(2, 9) # 2 - 4 - 6 - 8
conta_pares(1, 9) # 2 - 4 - 6 - 8
conta_pares(1, 8) # 2 - 4 - 6 - 8

print("-" * 30)

def fatorial(num):
    fat = 1
    for mult in range(1,num + 1):
        fat *= mult

    return fat

print(fatorial(5))