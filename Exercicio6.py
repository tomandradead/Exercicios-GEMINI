# Execicio 6: Encontrar o maior numero.


print("---Encontrar o Maior Numero---")
print("Por favor, digite 5 numeros aleatoriamente.")

maior_numero = None

for i in range(5):
    while True:
        try:
            numero_str = input(f"Digite o {i+1} numero:")
            numero = float(numero_str)
            if maior_numero is None or numero > maior_numero:
                break
        except ValueError:
            print("Entrada invalida. Por favor, digite um numero valido.")
            if maior_numero is not None:
                print(f"O MAIOR numero digitado foi: {maior_numero}")
            else:
                print(f"Nenhum numero valido foi digitado para comparar.")

                print("--- Fim do programa---")
