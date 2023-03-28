# Exercício 6: Usuário informa dois números inteiros em que o primeiro é as horas e o segundo dos minutos

num1 = int(input("Informe um número inteiro qualquer: "))
num2 = int(input("Informe um outro número inteiro qualquer: "))

if (num1 >= 0 and num1 <= 23) and (num2 >= 0 and num2 <= 59):
    print("A hora é válida")
else:
    print("A hora é inválida")