'''
Crea una función la cual reciba 2 listas del mismo tamaño
y retorne un diccionario, la primer lista tendrá las llaves
(keys) y la segunda los valores (values)
>>> print crear_dict(['a', 'e', 'i', 'o', 'u'], ['A', 'E', 'I', 'O', 'U'])
{'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
>>> print crear_dict(['uno', 'dos', 'tres'], [1, 2, 3])
{'uno': 1, 'dos': 2, 'tres': 3}
'''
def crear_dict(claves, valores):
    dict={}
    i=0
    if len(claves) == len(valores):
        while i < len(claves):
            dict[claves[i]] = valores[i]
            i=i+1
    return (dict)
    
print crear_dict(['a', 'e', 'i', 'o', 'u'], ['A', 'E', 'I', 'O', 'U'])
print crear_dict(['uno', 'dos', 'tres'], [1, 2, 3])

'''
Tarea:
Para practicar clases por favor hacer el siguiente ejercicio:

Definir una clase Tiempo, la cual tiene tres datos como parametros:
horas, minutos y segundos.
La clase Tiempo ademas debe tener dos metodos:
def mostrar(self): el cual mostrará la hora de la siguiente manera:
            >>> tiempo = Tiempo(3, 15, 32)
            >>> tiempo.mostrar()
            La hora es 3:15:32

def sumar_segundos(self, segundos), el cual recibirá una cantidad de
segundos los cuales se sumarán a la hora que se tiene guardada actualmente. 
Ejemplos:.
>>> tiempo = Tiempo(3, 15, 32)
>>>tiempo.sumar_segundos(8)
>>>tiempo.mostrar()
La hora es 3:15:40
>>>tiempo.sumar_segundo(40)
>>>tiempo.mostrar()
La hora es 3:16:20
>>>tiempo.sumar_segundos(3600)
>>>tiempo.mostrar()
La hora es 4:16:20
'''
class Tiempo:
    def __init__(self, hora, minuto, segundo):
        h = hora*3600
        m = minuto *60
        t= h + m + segundo
        h1 = int(t/3600)
        m1 = int((t - (h1*3600))/60)
        s1 = int(t- ((h1*3600) + (m1*60)))
        self.hora = h1
        self.minuto = m1
        self.segundo = s1
                
        
    def mostrar (self): 
        print "la hora es: " + str("{0:02d}".format(self.hora))+
               ":"+str("{0:02d}".format(self.minuto))+":" +
               str("{0:02d}".format(self.segundo))

    def sumar_segundos (self, segs):
        h = int(self.hora*3600)
        m = int(self.minuto *60)
        s = segs
        t= h + m + int(self.segundo) + s
        h1 = int(t/3600)
        m1 = int((t - (h1*3600))/60)
        s1 = int(t- ((h1*3600) + (m1*60)))
        self.hora = h1
        self.minuto = m1
        self.segundo = s1
    

tiempo = Tiempo(3, 15, 32)
tiempo.sumar_segundos(8)
tiempo.mostrar()
tiempo.sumar_segundos(40)
tiempo.mostrar()
tiempo.sumar_segundos(3600)
tiempo.mostrar()        
