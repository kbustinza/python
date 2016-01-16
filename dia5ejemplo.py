def contar_letras(texto):
    dic ={}
    for letra in texto:
        if letra in dic.keys():
            dic[letra] = dic[letra]+1
        else:
            dic[letra] = 1
    return dic

class Punto ():
    def __init__(self, puntox, puntoy):
        self.x = puntox
        self.y = puntoy
        
    def distancia(self):
        return (self.x ** 2) + (self.y ** 2)

    def mostrar(self):
        print "(" + str(self.x) + "," + str(self.y) + ")"

