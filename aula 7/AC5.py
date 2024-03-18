import random

def main():
    vida_a = 100
    att_a = random.randint(10, 20)
    def_a = random.randint(1, 5)
    Vida_m = random.randint(60, 80)
    att_m = random.randint(20, 30)
    rodada = 1
    print("Rodada", rodada)
    print("Aventureiro: vida", vida_a, "- att", att_a, "- def", def_a)
    print("Monstro: vida", Vida_m, "- att", att_m)
    while vida_a > 0 and Vida_m > 0:
        rodada = rodada + 1
        print("Rodada", rodada)
        print("Aventureiro: vida", vida_a, "- att", att_a, "- def", def_a)
        print("Monstro: vida", Vida_m, "- att", att_m)
        
        Vida_m = Vida_m - random.randint(1, att_a)
        if Vida_m <= 0:
            print("O monstro foi derrotado!")
            break
        
        dano_m = random.randint(1, att_m) - def_a
        if dano_m <= 0:
            vida_a = vida_a - 0
        else:
            vida_a = vida_a - dano_m
        if vida_a <= 0:
            print("Aventureiro foi derrotado!")
            break


main()