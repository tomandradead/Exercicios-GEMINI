# Exercicio 1 = Calcular se um numero é par ou impar.

numero = int(input("Digite um numero inteiro:"))


resto = numero % 2

if resto == 0:
    print("O numero é PAR!")
else:
    print("O numero é IMPAR!")
