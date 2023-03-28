# Exercício 3: se o número inteiro for negativo, transformo ele em positivo

numero = int(input("Informe um número inteiro qualquer: "))

if (numero < 0):
    print(f"O número é {numero*-1}")
else:
    print(f"O número é {numero}")