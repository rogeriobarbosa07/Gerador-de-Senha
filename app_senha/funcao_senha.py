import random

def senha():
    chars = ['1234567890', 
             'abcdefghijklmnopqrstuvwxyz', 
             'ABDCEFGHIJKLMNOPQRSTUVWXYZ', 
             '!@#$%&*()-+_=[]\|<>,.:;?/~^']
    
    senha = ''
    for _ in range(3):
        senha = senha + random.choice(chars[0])
        senha = senha + random.choice(chars[1])
        senha = senha + random.choice(chars[2])
        senha = senha + random.choice(chars[3])

    senha = list(senha)
    random.shuffle(senha)
    senha = ''.join(senha)

    return senha

print(senha()) 

# def senha_com_valor(valor):

#     return