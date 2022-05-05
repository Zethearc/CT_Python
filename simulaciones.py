# Simulaciones montecarlo

# Simulacion de Barajas

# import random
# import collections

# PALOS = ['espada', 'corazon', 'rombo', 'trebol']
# VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

# def crear_baraja():
#     barajas = []
#     for palo in PALOS:
#         for valor in VALORES:
#             barajas.append((palo, valor))

#     return barajas

# def obtener_mano(barajas, tamano_mano):
#     mano = random.sample(barajas, tamano_mano)
    
#     return mano

# def main(tamano_mano, intentos):
#     barajas = crear_baraja()

#     manos = []
#     for _ in range(intentos):
#         mano = obtener_mano(barajas, tamano_mano)
#         manos.append(mano)

#     pares = 0
#     for mano in manos:
#         valores = []
#         for carta in mano:
#             valores.append(carta[1])

#         counter = dict(collections.Counter(valores))
#         for val in counter.values():
#             if val == 3:
#                 pares += 1
#                 break

#     probabilidad_par = pares / intentos
#     print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')


# if __name__ == '__main__':
#     tamano_mano = int(input('De cuantas barajas sera la mano: '))
#     intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

#     main(tamano_mano, intentos)
    
# Cálculo de Pi

'''

Area del cuadrado: b*h
Area del circulo: pi * r^2

Entonces, si tenemos un cuadrado con altura de 2 y base 2
tendremos un circulo circunscrito de 1 de radio

Area del cuadrado: 4
Area del circulo: pi

Entonces, tenemos que.

agujas en circ = area circulo
agujas en cuad = area cuadrado

area circ = area cuad * agujas circulo
                agujas cuadrado
                
area circ = 4 * agujas circulo
            agujas cuadrado

'''

import random
import math
from Programas_estocasticos import desviacion_estandar, media

def aventar_agujas(numero_de_agujas):
    adentro_del_circulo = 0

    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1

    return (4 * adentro_del_circulo) / numero_de_agujas


def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimados, 5)}, sigma={round(sigma, 5)}, agujas={numero_de_agujas}')

    return (media_estimados, sigma)

def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2

    return media

if __name__ == '__main__':
    estimar_pi(0.01, 1000)