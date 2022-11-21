#
# Autores:
# Michel Silva
# Cristiano
# 
# data: 21/11/2022
#


# Elabore um programa em linguagem Python que receba o número de cadastro (inteiro) de
# três clientes de uma loja e o valor em reais que cada um desses clientes pagou por sua compra.
# O programa deve apresentar as seguintes informações como saída:

# a)	O valor total pago pelos três clientes;
# b)	O valor médio das compras efetuadas;
# c)	O número de cadastro dos clientes que efetuaram compras com valor superior a 100 reais;
# d)	A quantidade de clientes que efetuaram compras com valor inferior a 50 reais.

# entrada de dados
quantValorSuperior = 0
quantValorInferior = 0
cadastro1 = int(input("Digite o número de cadastro do primeiro cliente: "))
cadastro2 = int(input("Digite o número de cadastro do segundo cliente: "))
cadastro3 = int(input("Digite o número de cadastro do terceiro cliente: "))
valor1 = float(input("Digite o valor pago pelo primeiro cliente: "))
valor2 = float(input("Digite o valor pago pelo segundo cliente: "))
valor3 = float(input("Digite o valor pago pelo terceiro cliente: "))

# processamento de dados
total = valor1 + valor2 + valor3
media = total / 3
if valor1 > 100:
    quantValorSuperior += 1
if valor2 > 100:
    quantValorSuperior += 1
if valor3 > 100:
    quantValorSuperior += 1
if valor1 < 50:
    quantValorInferior += 1
if valor2 < 50:
    quantValorInferior += 1
if valor3 < 50:
    quantValorInferior += 1

# saida de dados
print("O valor total pago pelos três clientes é: ", total)
print("O valor médio das compras efetuadas é: ", media)
print("O número de cadastro dos clientes que efetuaram compras com valor superior a 100 reais é: ", quantValorSuperior)
print("A quantidade de clientes que efetuaram compras com valor inferior a 50 reais é: ", quantValorInferior)
print("fim do programa")