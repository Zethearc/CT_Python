# # Programación estocástica

# '''

# Un programa es deterministico si cuando se corre con el mismo 'input'
# produce el mismo 'output'

# Los programas deterministicos son muy importantes, pero existen problemas
# que no pueden resolverse de esta manera.

# La programacion estocastica permite introducir aleatoriedad a nuestros
# programas para crear simulaciones que permiten resolver otro tipo de
# problemas

# Los programas estocasticos se aprovecha de que las distribuciones 
# probabilisticas de un problema se conocen o pueden ser estimada.

# '''

# # Cálculo de probabilidades

# '''

# La probabilidad es una medida de la certidumbre asociada a un evento o
# suceso futuro y suele expresarse como un numero entre 0 y 1

# Una probabilidad de 0 significa que un suceso jamas sucedera

# Una probabilidad de 1 significa que un suceso esta garantizado de suceder
# en el futuro

# P(A) + P(~A) = 1
#     Ley del complemento

# P(A y B) = P(A) * P(B)
#     Ley multiplicativa (Mutuamente exclusivos)
    
# P(A o B) = P(A) + P(B) (Mutuamente exclusivos)
# P(A o B) = P(A) + P(B) - P(A y B) (No exclusivos)
#     Ley Aditiva

# '''

# import random

# def tirar_dado(numero_de_tiros):
#     secuencia_de_tiros = []

#     for _ in range(numero_de_tiros):
#         tiro = random.choice([1, 2, 3, 4, 5, 6])
#         secuencia_de_tiros.append(tiro)

#     return secuencia_de_tiros

# def main(numero_de_tiros, numero_de_intentos):
#     tiros = []
#     for _ in range(numero_de_intentos):
#         secuencia_de_tiros = tirar_dado(numero_de_tiros)
#         tiros.append(secuencia_de_tiros)

#     tiros_con_1 = 0
#     for tiro in tiros:
#         if 1 in tiro:
#             tiros_con_1 += 1

#     probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
#     print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')



# if __name__ == '__main__':
#     numero_de_tiros = int(input('Cuantas tiros del dado: '))
#     numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

#     main(numero_de_tiros, numero_de_intentos)
    
# Inferencia Estadistica

'''

Con las simulaciones podemos calcular las probabilidades de eventos
complejos sabiendo las probabilidaes de eventos simples

Que pasa cuando no sabemos las probabilidaes de eventos simples?

Las tecnicas de la inferencia estadistica nos permiten 
inferir/concluir las propiedaeds de una poblacion a partir de una 
muestra aleatoria.

'''
'''

El principio guia de la inferencia estadistica es una muestra aleatoria
tiende a exhibir las mismas propiedades que la poblacion de la cual
fue extraida. John Guttag

'''

# Por que funciona?

'''

En pruebas independientes repetidas con la misma probabilidad p de un
resultado, la fraccion de desviaciones de p converge a cero conforme
la cantidad de pruebas se acerca al infinito.

P(lim_(n->inf) ^x_n = u) =1

'''

# Falacia del apostador

'''

La falacia del apostador señala que despues de un evento extremo,
ocurriran eventos menos extremos para nivelar la media.

La regresion a la media señala que despues de un evento aleatorio
extremo, el siguiente evento problamente sera menos extremo

'''

# Media 

'''

Es una medida de tendencia central

Comunmente es conocida como el promedio

La media de una poblacion se denota con el simbolo u(mu). La media de
una muestra se denota ^x


'''

# import random

# def media(X):
#     return sum(X) / len(X)

# if __name__ == '__main__':
#     X = [random.randint(1,21) for i in range (20)]
#     mu = media(X)
    
#     print(X)
#     print(mu)
    
# Varianza y desviacion estandar

# Varianza

'''

La varianza mide que tan propagados se encuentran un conjunto de
valores aleatorios de su media.

Mientras que la media nos da una idea de donde se encuentras los 
valores, la varianza nos dice que tan dispersos se encuentran.

La varianza siempre debe entenderse con respecto a la media.

'''

# Desviacion estandar

'''

La desviacion estandar es la raiz cuadrada de la varianza.

Nos permite entender, tambien, la propagacion y se debe entender 
siempre relacionado a la media.

La ventaja sobre la varianza es que la desviacion estandar esta en
las mismas unidades que la media.

'''

import random
import math

def media(X):
    return sum(X) / len(X)


def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def desviacion_estandar(X):
    return math.sqrt(varianza(X))


if __name__ == '__main__':
    X = [random.randint(5, 15) for i in range(100)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo X: {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviacion estandar = {sigma}')
    
# Distribucion normal

'''

Es una de las distribuciones mas recurrentes en cualquier tamaño

Se define completamente por su media y su desviacion estandar.

Permite calcular intervalos de confianza con la regla empirica

'''

# Regla empirica

'''

Tambien conocida como la regla 68-95-99.7

Señala cual es la dispercion de los datos en una distribucion 
normal a uno, dos y tres sigmas.

Permite calcular probabilidades con la densidad de la
distribucion normal.

'''

# Simulaciones de montecarlo

'''

Permite crear simulaciones para predecir el resultado de un problema

Permite convertir problemas deterministicos en problemas estocasticos

Es utilizado en una gran diversidad de areas, desde la ingenieria hasta
la biologia y el derecho.

'''