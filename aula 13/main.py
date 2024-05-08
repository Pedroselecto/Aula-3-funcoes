from conta import Conta

c1 = Conta(1234, "João")
c2 = Conta(5678, "Maria")
c3 = Conta(1234, "João")

print(c1.titular)
print(c2.titular)

c1.depositar(50)

print(c1.saldo)
print(c2.saldo)

c1.sacar(20)
tenta_sacar = c2.sacar(20)

if tenta_sacar:
    print("Saque feito com sucesso")
else:
    print("Saldo insuficiente")

print(c1.saldo)
print(c2.saldo)

c2.depositar(50)

print(c1)
print(c2)
print(c1 == c2)
print(c1 == c3)

from agencia import Agencia
from gerente import Gerente

ger1 = Gerente("Zé", "ze@banco.com", "1234")
ag1 = Agencia(1, "Barra", ger1)

c1 = ag1.abrir_nova_conta("ana")
c2 = ag1.abrir_nova_conta("joão")

print(c1)
print(c2)

ag2 = Agencia(2, "centro", ger1)

c3 = ag2.abrir_nova_conta("antonio")
print(c3)