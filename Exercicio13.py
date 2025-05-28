#Exercicio13: Contagem Regressiva:
#Imprima uma contagem regressiva de 10 até 1.
#Após a contagem, imprima "Fogo!".
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # Pausa de 1 segundo entre os números
print("Fogo!")
# Explicação:
# 1. Importamos o módulo `time` para usar a função de pausa.
# 2. Usamos um loop `for` para contar de 10 a 1, decrementando de 1 em cada iteração.
# 3. Dentro do loop, imprimimos o número atual.
# 4. Usamos `time.sleep(1)` para pausar a execução por 1 segundo entre as impressões.
# 5. Após o loop, imprimimos "Fogo!" para indicar o final da contagem regressiva.
# Observação: O código acima cria uma contagem regressiva visual, com uma pausa de 1 segundo entre cada número, tornando-o mais dinâmico e interessante.
