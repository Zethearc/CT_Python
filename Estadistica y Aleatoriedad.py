# Programación Dinámica y Estocástica

# Objetivos

'''

- Aprender cuando utilizar programacion dinamica y sus beneficios.
- Entender la diferencia entre programos deterministas y estocasticos.
- Aprender a utilizar programacion estocastica.
- Aprender a crear simulaciones computacionales validas.

Aprenderemos a diferenciar la programacion estocastica de la deterministica.

'''

# Programacion dinamica

'''

Desde ya el nombre no tiene nada que ver con lo que es en realidad.
'El nombre "Programacion dinamica" se escogio para esconder a
patrocinadores gubernamentales el hecho que en realidad se estaba
haciendo Matematicas. La frase Programacion Dinamica es algo que 
ningun congresista puede oponerse.' -Richard Bellman

# Uso de programacion dinamica

Subestructura optima. Una solucion global optima se puede encontrar
al combinar soluciones optimas de subproblemas locales.

Proglemas empalmados. Una solucion optima que involucra resolver
el mismo problema en varias ocasiones.

'''

# Memoization

'''

La memorizacion es una tecnica para guardar computos previos y evitar
realizarlos nuevamente.

Normalmente se utiliza un diccionario, donde las consultas se pueden
hacer en O(1).

Intercambia tiempo por espacio.

'''

# Numeros de Fibonacci

'Fn = Fn-1 + Fn-2'

#https://uniwebsidad.com/libros/algoritmos-python/capitulo-18/un-ejemplo-de-recursividad-poco-eficiente

import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado

        return resultado

if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)
    
# Caminos Aleatorios

'''

Es un tipo de simulación que elige aleatoriamente una decision dentro
de un conjunto de decisiones validas.

Se utiliza en muchos campos del conocimiento cuando los sistemas no son
deterministas e incluyen elementos de aleatoriedad.

'''


from borracho import BorrachoTradicional
from Campo import Campo 
from coordenada import Coordenada 

from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)