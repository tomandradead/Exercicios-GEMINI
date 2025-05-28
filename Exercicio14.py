#Exercicio14: Soma de Números Pares:
#Use um loop para somar todos os números pares de 1 a 50.
#Imprima o resultado da soma.
soma = 0
for numero in range(1, 51):
    if numero % 2 == 0:  # Verifica se o número é par
        soma += numero  # Adiciona o número par à soma
print(f"A soma dos números pares de 1 a 50 é: {soma}")
# Explicação:
# 1. Inicializamos uma variável `soma` com 0 para armazenar o resultado.
# 2. Usamos um loop `for` para iterar sobre os números de 1 a 50.
# 3. Dentro do loop, verificamos se o número atual é par usando o operador módulo (`%`).
# 4. Se o número for par, adicionamos ele à variável `soma`.
# 5. Após o loop, imprimimos o resultado da soma dos números pares.
# Observação: O código acima utiliza um loop para percorrer os números de 1 a 50 e soma apenas os números pares, demonstrando o uso de condicionais e loops em Python.

