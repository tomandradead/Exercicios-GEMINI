                    ## Exercicio 8 - Calculo de Idade em Dias

#idade = int(input("Digite a sua idade:"))
#print("Voce viveu ate o momento " + str(idade * 365) + "dias". format(idade * 365))

#O codigo acima funciocou, porem, necessita de ajustes.
#Codigo ajustado:

idade = int(input("Digite a sua idade: "))
dias = idade * 365
print(f"Voce viveu até o momento {dias} dias.")
# Explicação:# 1. A entrada do usuário é lida como um inteiro.
# 2. Multiplicamos a idade por 365 para obter o número de dias.     

