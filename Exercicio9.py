#Exercicio9: Calculo de area de um retangulo

retangulo = float(input("Digite o comprimento e a largura do retangulo:"))
area = retangulo * retangulo
print(f"A area do retangulo é {area} metros quadrados.")
# Explicação:
# 1. A entrada do usuário é lida como um float. 
# # 2. Multiplicamos o comprimento pela largura para obter a área do retângulo.
# # 3. A área é impressa em metros quadrados.
# # Observação: O código acima assume que o usuário insere o comprimento e a largura como um único número.
# Para corrigir isso, podemos solicitar ao usuário que insira o comprimento e a largura separadamente.  
## Código corrigido:
comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))
area = comprimento * largura
print(f"A área do retângulo é {area} metros quadrados.")
# Explicação:
# 1. A entrada do usuário é lida como um float para o comprimento e a largura.
# 2. Multiplicamos o comprimento pela largura para obter a área do retângulo.
# 3. A área é impressa em metros quadrados.
# Observação: O código acima agora solicita ao usuário que insira o comprimento e a largura separadamente, o que é mais claro e evita confusões.
# # Exercicio9: Calculo de area de um retangulo.
