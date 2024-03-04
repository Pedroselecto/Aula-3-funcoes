"""

Programação estruturada - 04/03/2024
            Funções
- Evitar duplicidade de código
- Organizar melhor o código

Princípios SOLID
SRP - Single Responsibility Principle

Encapsulamento (junta várias funções assim como um remédio guarda diversos elementos)
"""

def traco(largura):
    print("." * 30)
# def --> definir (ou declarar) uma função.
def cabecalho(titulo, largura, caract_traco="."):
    traco(largura, caract_traco)
    print(titulo)
    traco(largura, caract_traco)

print("Olá")
# Uso ou chamada da função
"""
cabecalho("Relatório de vendas", 30)
cabecalho("folha de pagamento", 25, caract_traco=".")
cabecalho("lista de fornecedores", caract_traco="=")
print(print("Olá)"))
"""
# Ele pega os parâmetros na ordem, logo, no primeiro exemplo, o "titulo" está se relacionando ao "Relatório de vendas" e a largura ao número 30.
# Também é possível declarar com qual parâmetro está mexendo, como no segundo exemplo (é o mais recomendável).

"""

Entrada de dados
Processamento
Saída de dados
"""

# Escopo de variáveis
x = 1 # escopo global: aplica para todo código

def func1(x):
    x = 5 # escopo local: Essa variável pe 5 apenas para a função
    print(x)

print(x)
func1(x)
print(x)

# Evitar o uso de variáveis globais
# A não ser que sejam constantes