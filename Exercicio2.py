# Exercicio 2 = Calculadora Simples.

numero1 = int(input("Digite o primeiro numero:"))
operação = input("Digite a operação (+, -, * ou /)")
numero2 = int(input("Digite o segundo numero:"))


if operação == "+":
    print(numero1 + numero2)
elif operação == "-":
    print(numero1 - numero2)
elif operação == "*":
    print(numero1 * numero2)
elif operação == "/":
    print(numero1 / numero2)
else:
    print("Voce digitou algum caractere errado !")
