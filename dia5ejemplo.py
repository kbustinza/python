def contar_letras(texto):
    dic ={}
    for letra in texto:
        if letra in dic.keys():
            dic[letra] = dic[letra]+1
        else:
            dic[letra] = 1
    return dic

class Punto ():
    def __init__(self): #es el constructor
        self.x = 3
        self.y = 5
