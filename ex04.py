#
# Autores:
# Michel Silva
# Cristiano
# 
# data: 21/11/2022


# 4. Em linguagem Python, escreva um programa que leia um número 
# inteiro e calcule a soma de todos os divisores desse número, com 
# exceção dele próprio. Ex. a soma dos divisores do 
# número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78.

# entrada de dados
valor = int(input("Digite um numero: "))
valorF = valor
valorW = valor
somaF = 0
somaW = 0

# processamento de dados
# usando o FOR
for i in range(1, valorF):
    if valorF % i == 0:
        somaF = somaF + i
        
# saida de dados para o FOR
print(f"A soma dos divisores de {valorF} é  {somaF}")

# usando o WHILE
""" while valorW > 1:
    valorW = valorW - 1
    if valorW % i == 0:  # erro aqui
        somaW = somaW + i """
while valorW > 1:
    valorW = valorW - 1
    if valorF % valorW == 0:
        somaW = somaW + valorW

# saida de dados para o WHILE
print(f"A soma dos divisores de {valor} é  {somaW}")