# Muestreo

'''

Hay ocasiones en la que no tenemos acceso a toda la poblacion
que queremos explorar.

Uno de los grandes descubrimientos de la estadistica es que las
muestras aleatorias tienden a mostrar las mismas propiedades de
la poblacion objetivo

El tipo de muestreo que hemos hecho hasta ahora es muestreo probabilistico

'''

# Muestreo

'''

Es un muestreo aleatorio cualquier miembro de la poblacion tiene
la misma probabilidad de ser escogido.

En un muestreo estratificado tomamos en consideracion las caracteristicas
de la poblacion para partirla en subgrupos y luego tomamos muestras
de cada subgrupo.
    Incvrementa la probabilidad de que el muestreo sea representativo 
    de la poblacion.

'''

# Teorema del limite central 

'''

Es uno de los teoremas mas importantes de la estadistica

Establece que muestras aleatorias de cualquier distribucion van
a tener una distribucion normal.

Permite entender cualquier distribucion como la distribucion normal
de sus medias y eso nos permite aplicar todo lo que sabemos de 
distribuciones normales

'''

# Datos experimentales

'''

Es la aplicacion del metodo cientifico

Es necesario comensar con una teoria o hipotesis sobre el resultado
al que se quiere llegar

Basado en la hipotesis se debe crear un experimento para validar o
falsear la hipotesis

Se valida o falsea una hipotesis midiendo la diferencia entre las 
mediciones experimentales y aquellas mediciones predichas por la
hipotesis.

'''

# Regresion lineal

'''

Permite aproximar una funcion a un conjunto de datos obtenidos de
manera experimental

No necesariamente permite aproximar funciones lineales, sino que sus 
variantes permiten aproximar cualquier funcion polinomica.

'''

import numpy as np

x = np.array([0,1,2,3,4,5,6,7,8])
y = np.array([1,2,3,5,4,6,8,7,9])

coeffs = np.polyfit(x,y,1)
print(coeffs[0],coeffs[1])

m = coeffs[0]
b = coeffs[1]

est_y = (m * x) + b

import matplotlib.pyplot as plt

plt.plot (x, est_y)
plt.scatter(x, y)
plt.show()