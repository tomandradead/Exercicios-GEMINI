#Exercicio11: Comparador de Numeros.
# Compara dois números e imprime o maior ou se são iguais.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f"O maior número é {numero1}.")
elif numero2 > numero1:
    print(f"O maior número é {numero2}.")
else:
    print("Os números são iguais.")
# Explicação:
# 1. A entrada do usuário é lida como um float para permitir números decimais.
# 2. Comparamos os dois números.
# 3. Se o primeiro número for maior, imprimimos que ele é o maior.
# 4. Se o segundo número for maior, imprimimos que ele é o maior.
# 5. Se os números forem iguais, imprimimos que são iguais.
# Observação: O código acima permite a comparação de números decimais e trata o caso em que os números são iguais.

