import random

def verifica_senha_forte(senha, chars):
    numeros = set(chars[0])
    minusculas = set(chars[1])
    maiusculas = set(chars[2])
    especiais = set(chars[3])

    tem_numero = any(c in numeros for c in senha)
    tem_minuscula = any(c in minusculas for c in senha)
    tem_maiuscula = any(c in maiusculas for c in senha)
    tem_especial = any(c in especiais for c in senha)

    return tem_numero and tem_minuscula and tem_maiuscula and tem_especial

def senha(numero_chars=12):
    chars = ['1234567890', 
             'abcdefghijklmnopqrstuvwxyz', 
             'ABDCEFGHIJKLMNOPQRSTUVWXYZ', 
             '!@#$%&*()-+_=[]\|<>,.:;?/~^']
    
    senha_forte = False
    while not senha_forte:

        senha = ''
        for _ in range(numero_chars):
            senha = senha + random.choice(chars[random.randint(0, 3)])
        
        senha_forte = verifica_senha_forte(senha, chars)

    return senha


# testando saída da função
print(senha())

# def senha_com_valor(valor):

#     return