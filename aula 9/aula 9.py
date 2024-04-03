# Exercício 1
def alfabeto():
        return[chr(i) for i in range(97, 123)]

print(alfabeto())

print("-" * 30)

# Exercício 2
import random
def gera_chave():
        chave = {}
        letras = alfabeto()

        letras_cifradas = alfabeto()
        random.shuffle(letras_cifradas)

        for char, char_cifrado in zip(letras, letras_cifradas):
                chave[char] = char_cifrado

        return chave

print(gera_chave())

print("-" * 30)

# Exercício 3

def cripto(mensagem, chave):
    mensagem_cifrada = ""

    for char in mensagem:
           mensagem_cifrada += chave[char]

    return mensagem_cifrada

def decripto(mensagem, chave):
       chave_inversa = {}
       for ch, vl in chave.items():
        chave_inversa[vl] = ch

        return cripto(mensagem, chave_inversa)

# Pegar o resto no github do Victor
