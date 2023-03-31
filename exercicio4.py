# Exercício 4: Descobrir se um caractere é vogal ou consoante

# O .lower() transforma todos os caracteres em minúsculos para facilitar
letra = input("Informe uma letra qualquer: ").lower()

if (letra == "a" or letra == "e" or letra == "i" or 
    letra == "o" or letra == "u" ): 
        print(f"A letra é uma vogal")
else:
    print(f"A letra é uma consoante")

    '''
        Você também pode fazer com

        vogais = "aeiouAEIOU"

        if letra in vogais:
            print(f"A letra é uma vogal")
    '''