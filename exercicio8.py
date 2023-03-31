# Exercício 8: Solicita 3 números e exibe na tela o menor deles, e se for igual, mostra a mensagem de "Números iguais"

num1 = float(input("Informe um número qualquer: "))
num2 = float(input("Informe um outro número qualquer: "))
num3 = float(input("Informe um outro número qualquer: "))

if (num1 < num2 and num1 < num3):
    print(f"O menor número é {num1}")
elif(num2 < num1 and num2 < num3):
    print(f"O menor número é {num2}")
elif(num3 < num1 and num3 < num2):
    print(f"O menor número é {num3}")
elif (num1 == num2) and (num2 == num3):
    print("Números iguais")
else:
    print("Dois números iguais")