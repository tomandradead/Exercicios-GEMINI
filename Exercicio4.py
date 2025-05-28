# Exercicio 4: Somando numeros (Com Loop).

print("--- Somador de Numeros ---")
print("Digite os numeros que deseja somar. Digite 'fim' para ver o total.")

soma_total = 0

while True:
    entrada_usuario = input("Digite um numero (ou 'fim'):")

    if entrada_usuario.lower() == "fim":
        print("Saindo do programa de soma.")
        print(f"A soma total dos numeros digitados é: {soma_total}")
        break
    else:
        try:
            numero_digitado = float(entrada_usuario)
            soma_total += numero_digitado
        except ValueError:
            print("Entrada invalida. Por facor, digite um numero valido ou 'fim'.")

            print("---FIM DO PROGRAMA---")
