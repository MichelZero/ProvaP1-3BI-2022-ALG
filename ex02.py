#
# Autores:
# Michel Silva
# Cristiano
# 
# data: 21/11/2022
#
# 2. Faça um programa em linguagem Python que apresenta as raízes 
# de uma equação do segundo grau no formato ax^2+bx+c=0 no domínio 
# dos números reais. O programa deve receber como entrada os 
# coeficientes a, b e c da equação. Faça uso de seus conhecimentos de 
# Matemática para elaborar o programa. Lembre-se que uma equação do segundo 
# grau pode ter duas raízes distintas, duas raízes iguais ou não possuir 
# raízes reais. As raízes de uma equação do segundo grau podem ser obtidas 
# a partir da seguinte expressão:

# x=(-b±√∆)/2a,em que ∆ = b^2-4ac

# entrada de dados
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# processamento de dados
delta = b**2 - 4*a*c
if delta < 0:
    print("Não existem raízes reais")
elif delta == 0:
    x = -b/(2*a)
    print("A equação possui apenas uma raiz real: ", x)
else: # delta > 0
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    print("A equação possui duas raízes reais: ", x1, " e ", x2)
    
# Saida de dados
print("fim do programa")