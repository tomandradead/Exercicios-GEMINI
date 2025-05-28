# Exercicio 3 = Verificador de idade para votação.

ano = int(input("Qual é o ano do seu nascimento?:"))
ano2 = 2024 - ano

if ano2 <= 16:
    print("Voce ainda nao é obrigado(a) a votar !")
elif ano2 >= 80:
    print("Voce nao é mais Obrigado a votar!")
else:
    print("Voce é obrigado a votar!")
