# ¿Cómo funciona Python?

# Lenguajes compilados vs interpretados

'''
Compiled
void main(){
    cout<< "Hello World"
    }

110 11100 01 100100 111100

Interpreted

def my_func():
    print("Hola mundo")

0 LOAD_GLOBAL       0 (print)
2 LOAD_CONST        1 ('Hola Mundo')
4 CALL_FUNCTION     1
6 POP_TOP
8 LOAD_CONST        0 (None)
10 RETURN_VALUE

Esto es leido por una maquina virtual

'''

# Que es el garbage collector

'''

En python tenemos una seccion especial que es el recolector de
basura. Toma las variables que no esten en uso y las elimina.

'''

# Que es la carpeta __pycache__

'''

Cuando estamos programando y tenemos codigo ya ejecutado este cache
nos sirve para almacenar el codigo convertido a lenguaje de maquina
y no tener que hacerlo denuevo.

'''