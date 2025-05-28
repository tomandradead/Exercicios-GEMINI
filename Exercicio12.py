#Exercicio12: Sistema de Pontuação.
#Peça ao usuario para inserir uma pontuação de 0 a 100.
#Se a pontuação for de 90 a 100, imprima "Excelente!".
#Se for de 70 a 89, imprima "Bom.".
#Se for de 50 a 69, imprima "Regular.".
#Abaixo de 50, imprima "Insuficiente.".

pontuacao = float(input("Digite sua pontuação (0 a 100): "))
if 90 <= pontuacao <= 100:
    print("Excelente!")
elif 70 <= pontuacao < 90:
    print("Bom.")
elif 50 <= pontuacao < 70:
    print("Regular.")
elif pontuacao < 50:
    print("Insuficiente.")
else:
    print("Pontuação inválida. Por favor, insira um valor entre 0 e 100.")
# Explicação:
# 1. A entrada do usuário é lida como um float para permitir pontuações decimais.
# 2. Verificamos a faixa da pontuação usando condições encadeadas.
# 3. Dependendo da faixa, imprimimos a mensagem correspondente.
# Observação: O código trata pontuações fora do intervalo de 0 a 100 como inválidas.
# 4. As condições são organizadas de forma a garantir que cada faixa seja verificada corretamente.
# 5. A pontuação é validada para garantir que esteja dentro do intervalo esperado.
# 6. O código é claro e fácil de entender, com mensagens apropriadas para cada faixa de pontuação.
# 7. O uso de `elif` garante que apenas uma condição seja avaliada como verdadeira, evitando múltiplas impressões.
# 8. O código é eficiente e não executa verificações desnecessárias após encontrar a condição verdadeira.
# 9. A estrutura do código é simples, facilitando a manutenção e futuras modificações.
# 10. O código pode ser facilmente adaptado para incluir mais faixas de pontuação ou mensagens, se necessário.
# 11. A entrada do usuário é validada para garantir que a pontuação esteja dentro do intervalo esperado.

