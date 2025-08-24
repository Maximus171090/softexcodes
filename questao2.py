# Verificar Palíndromo


# VeDescrição: Leia uma palavra/frase e diga se é palíndromo (mesma leitura ao contrário),
# ignorando espaços e diferenças de maiúsculas/minúsculas.


# Exemplo:
# Entrada: Socorram me subino onibus em marrocos
# Saída: É palíndromo


frase = input('Digite uma palavra ou frase: ')


# Remover espaços e deixar tudo minúsculo.

frase_formatada = frase.replace('','').lower()

#Inverter a String
frase_invertida = frase_formatada[::-1]

#Verificar se é Palídromo.

if frase_formatada == frase_invertida:
    print('É palídromo')
else:
    print('Não é palídromo')


    # Fim do Script.