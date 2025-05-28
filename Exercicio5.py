# Exercicio 5: Média de Notas (Com Lista).

notas_do_aluno = []

for i in range(4):
    while True:
        try:
            nota_str = input(f"Digite a nota {i+1}:")
            nota = float(nota_str)

            if 0 <= nota <= 10:
                notas_do_aluno.append(nota)
                break
            else:
                print("Nota invalida. Por favor, digite um numero para a nota.")

        except ValueError:
            print("Entrada invalida. Por favor, digite um numero par a nota.")


def calcular_media(lista_de_notas):
    if len(lista_de_notas) == 0:
        return 0.0

    soma = sum(lista_de_notas)
    quantidade = len(lista_de_notas)
    media = soma / quantidade
    return media


media_final = calcular_media(notas_do_aluno)

print(f"A média das notas é: {media_final:.2f}")

if media_final >= 7.0:
    print("!---APROVADO---!")
else:
    print("REPROVADO")

print("---FIM DO PROGRAMA---")
