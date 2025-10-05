import random

def senha(numero_chars=12):
    chars = ['1234567890', 
             'abcdefghijklmnopqrstuvwxyz', 
             'ABDCEFGHIJKLMNOPQRSTUVWXYZ', 
             '!@#$%&*()-+_=[]\|<>,.:;?/~^']
    
    senha = ''
    for _ in range(numero_chars):
        senha = senha + random.choice(chars[random.randint(0, 3)])

    senha = list(senha)
    random.shuffle(senha)
    senha = ''.join(senha)

    return senha

# testando saída da função
print(senha())

# def senha_com_valor(valor):

#     return