# Gerar acrônimo

frase = input("Digite o nome do curso/expressão: ")

stopwords = {'de', 'da', 'do', 'das', 'dos', 'e'}

palavras = frase.lower().split()

iniciais = []

for p in palavras:
    if p and p not in stopwords:
        iniciais.append(p[0].upper())


acronimo = ''.join(iniciais)
print(acronimo)


# Fim do Script