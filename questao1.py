



# Questão 1 - Contar vogais e Consoantes.

# Ler a frase do Usuário.

frase = input('Digite uma frase: ')

# Define as vogais

vogais = 'aeiou'

# Contadores

qtd_vogais = 0
qtd_consoantes = 0

# Percorre cada caractere da frase
for caractere in frase.lower():  # Deixa tudo em minúsculo.

    if caractere.isalpha(): # Considera Letras
        if caractere in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

            # Mostra o Resultado
            


# PARA SAIR DE DENTRO DO "FOR" ESTAVA FAZENDO MUITAS LINHAS.
            

print(f'vogais: {qtd_vogais} | consoantes: {qtd_consoantes}')