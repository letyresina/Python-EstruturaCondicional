# Exercício 10: salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

salarioFixo = float(input("Informe o salário fixo do funcionário: "))

valorVendas = float(input("Informe o valor das vendas do funcionário: "))

porcentagem = valorVendas * 0.3
valorVendasTotal = valorVendas + porcentagem

if(valorVendasTotal > 1.500):
    porcentagem2 = valorVendasTotal * 0.5
    valorVendasTotal2 = valorVendasTotal + porcentagem2
    salarioTotal = salarioFixo + valorVendasTotal2
    print(f"{salarioTotal}")
else:
    salarioTotal = salarioFixo + valorVendasTotal
    print(f"{salarioTotal}")