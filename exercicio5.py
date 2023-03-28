# Exercício 5: Saber se o número é negativo, positivo ou zero

numero = int(input("Informe um número inteiro qualquer: "))

if (numero < 0):
    print(f"O número {numero} é negativo.")
elif (numero > 0):
    print(f"O número {numero} é positivo.")
else:
    print(f"O número {numero} é zero.")