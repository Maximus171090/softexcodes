# Descrição: Leia uma frase e mostre quantas vezes cada palavra aparece.
#Exemplo:
#Entrada: eu gosto de python e eu gosto de programar
#Saída:
#eu: 2
#gosto: 2
#de: 2
#python: 1
#e: 1
#programar: 1

#Dica: use split() para separar palavras e um dicionário para contar. Um for percorrendo 
# a lista de palavras resolve.

#Frequencia de Palavras

frase = input('Digite uma frase: ')

#Separar a frase em palavras (por espaços)
palavras = frase.lower().split()

#criar um dicionário para contar
frequencia = {}

#Percorrer as palavras e contar

for palavra in palavras: 
    if palavra in frequencia:
        frequencia[palavra] += 1
    else: frequencia[palavra] = 1

    # Mostrar Resultado
for palavra, qtd in frequencia.items():
    print(f' {palavra}: {qtd}')


    #Fim do Script