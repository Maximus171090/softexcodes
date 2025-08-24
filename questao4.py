# Verificador de senha forte


import re

senha = input('Digite senha para ser verificada:')

# Criterios de validação.

tem_maiuscula = any(c.isupper() for c in senha)

# Pelo menos 1 letra maiúscula
tem_minuscula = any(c.islower() for c in senha)

# Pelo menos 1 letra minúscula
tem_numero = any(c.isdigit() for c in senha)

# Pelo menos 1 número

tem_especial = bool(re.search(r'[!@#%^&*(),.?\:{}|<>]', senha))

# Pelo menos 1 Caractere especial

tamanho_ok = len(senha) >= 8

# Pelo menos 8 Caracteres

# Verificação final

if all([tem_maiuscula, tem_minuscula, tem_numero, tem_especial, tamanho_ok]):
    print('ok! Senha Forte!')
else:
    print('Senha Fraca!')
    print('Regras: mínimo 8 caracteres, incluir maiúsculas, minúscluas, número, e carectere especial.')

    # Fim do Script