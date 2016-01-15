'''Escribe una funcion que reciba un numero y una lista
y retorne una lista con la multiplicacion escalar
(cada elemento de la lista multiplicado por el numero)
>>> mult_escalar(5, [1, 2])
   [5, 10]
>>> mult_escalar(3, [1, 0, -1])
   [3, 0, -3]
>>> mult_escalar(7, [3, 0, 5, 11, 2])
   [21, 0, 35, 77, 14] '''

def mult_escalar(escalar, lista):
    resp_lista =[]
    for elem in lista:
        a= elem*escalar
        resp_lista.append(a)
    print (resp_lista)

'''
Escribe una funcion que reciba una lista de numero y
retorne una lista solo con los elementos pares
>>> solo_pares([1, 3, 4, 6, 7, 8])
   [4, 6, 8]
>>> solo_pares([2, 4, 6, 8, 10, 11, 0])
   [2, 4, 6, 8, 10, 0]
>>> solo_pares([1, 3, 5, 7, 9, 11])
   []
>>> solo_pares([4, 0, -1, 2, 6, 7, -4])
   [4, 0, 2, 6, -4]
'''
def solo_pares (lista):
    resp_lista = []
    for elem in lista:
        if elem % 2 == 0:
            resp_lista.append(elem)
    print (resp_lista)

mult_escalar(5, [1, 2])
mult_escalar(3, [1, 0, -1])
mult_escalar(7, [3, 0, 5, 11, 2])
solo_pares([1, 3, 4, 6, 7, 8])
solo_pares([2, 4, 6, 8, 10, 11, 0])
solo_pares([1, 3, 5, 7, 9, 11])
solo_pares([4, 0, -1, 2, 6, 7, -4])
