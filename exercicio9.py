# Exercicio 9: Informe se o triângulo é equilátero, isósceles ou escaleno

lado1 = float(input("Informe o primeiro lado do triângulo: "))
lado2 = float(input("Informe o segundo lado do triângulo: "))
lado3 = float(input("Informe o terceiro lado do triângulo: "))

if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
    print(f"O triângulo é equilátero.")
elif (lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado2 != lado1) or (lado3 == lado1 and lado3 != lado1) or (lado1 == lado3 and lado1 != lado2):
    print(f"O triângulo é isóceles.")
else:
    print(f"O triângulo é escaleno.")