#
# Autores:
# Michel Silva
# Cristiano
# 
# data: 21/11/2022
#
# 3. Elabore um programa em Python que receba dez números inteiros do usuário 
# e, em seu final, exiba o maior número informado. 

# entrada de dados
maior = -1000000
manor = 1000000 
contador = 0 # contador de repetições do laço, para que o laço seja executado 10 vezes

# processamento de dados
while contador < 10: # enquanto o contador for menor que 10, contador vai de 0 a 9 e o laço é executado 10 vezes
    numero = int(input("Digite um numero: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    contador = contador + 1

# Saida de dados
print("O maior numero é: ", maior)
print("O menor numero é: ", menor)
print("fim do programa")
