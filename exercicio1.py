# Exercício 1: Calcular média para saber se foi aprovado ou reprovado

print("Seja bem-vindo(a)")

nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a primeira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if (media >= 6):
    print(f"A média do aluno foi {media:.1f}, sendo aprovado.")
else:
    print(f"A média do aluno foi {media:.1f}, sendo reprovado.")