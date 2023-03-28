# Exercício 7: Solicita dois números ao usuário e exibe apenas o maior deles. Caso eles sejam iguais exiba a mensagem “Números Iguais”

num1 = float(input("Informe um número qualquer: "))
num2 = float(input("Informe um número qualquer: "))

if (num1 > num2):
    print(num1)
elif (num2 > num1):
    print(num2)
else:
    print("Números iguais")