# '''Lo importante visto hasta ahora'''

# # Modulo de ordenamiento y busqueda

# '''

# En la actualidad existen muchas librerias y paquetes que
# tienen diferentes tipos de ordenamiento y busqueda. Asi,
# que lo que nosotros hemos aprendido son los conceptos de
# complejdiad algoritmica y empezar a comparar ciertos tipos
# de algoritmos. Donde en la mayoria de los casos no es tener
# computadoras mucho mas rapidas (En algunos casos si), en 
# muchos casos es tener metodos mas eficientes.

# '''

# # Decomposicion

# '''

# Ya que, sabemos usar clases y crear instancia a partir de
# ellas. Vamos a entender lo que es la decomposicion.

# Decomposicion.
#     Partir un problema en problemas mas pequeños
    
#     Las clases permiten crear mayores abstracciones en forma
#     de componentes
    
#     Cada clase se encarga de una parte del problema y el
#     programa se vuelve mas facil de mantener.
    
# Las clases nos permiten decomponer elementos de nuestro dia
# a dia en componentes mas pequeños. Entonces, podemos decomponer
# un problema que nos parece muy grande en subproblemas que resolvemos
# por clases que en conjunto nos permiten resolver este problema.

# '''

# # Ejemplo en codigo

# class Automovil:

#     def __init__(self, modelo, marca, color):
#         self.modelo = modelo
#         self.marca = marca
#         self.color = color
#         self._estado = 'en_reposo'              # Variable Privada
#         self._motor = Motor(cilindros=4)        # variable Privada

#     def acelerar(self, tipo='despacio'):
#         if tipo == 'rapida':
#             self._motor.inyecta_gasolina(10)
#         else:
#             self._motor.inyecta_gasolina(3)

#         self._estado = 'en_movimiento'


# class Motor:

#     def __init__(self, cilindros, tipo='gasolina'):
#         self.cilindros = cilindros
#         self.tipo = tipo
#         self._temperatura = 0

#     def inyecta_gasolina(self, cantidad):
#         pass
    
# '''Tarea terminar de decomponer este automovil'''

# # Abstraccion

# '''

# Abstraccion
#     Enfocarnos en la informacion relevante
    
#     Separar la informacion central de los detales secundarios
    
#     Podemos utilizar variables y metodos (Privados o Publicos)
    
# Cuando nosotros usamos objetos en la vida real. Nosotros no tenemos
# que preocuparnos la forma en que funcionan las cosas. Es mucho mas
# importante que sea funcional y entendible.

# Si tendriamos que saber que hace cada libreria y codigo esta seria
# una carrera imposible. En muchos casos no tenemos que saber su 
# manera interna de funcionar.

# '''

# Ejemplo en codigo

# class Lavadora:

#     def __init__(self):
#         pass

#     def lavar(self, temperatura='caliente'):
#         self._llenar_tanque_de_agua(temperatura)
#         self._anadir_jabon()
#         self._lavar()
#         self._centrifugar()

#     def _llenar_tanque_de_agua(self, temperatura):
#         print(f'Llenando el tanque con agua {temperatura}')

#     def _anadir_jabon(self):
#         print('Anadiendo jabon')

#     def _lavar(self):
#         print('Lavando la ropa')

#     def _centrifugar(self):
#         print('Centrifugando la ropa')


# if __name__ == '__main__':
#     lavadora = Lavadora()
#     lavadora.lavar()
    
'''Tarea generar una abstraccion de otro objeto de la vida real'''

# Funciones: Base de los decoradores

'''

El concepto de decorador en Python es algo que podríamos ubicar en un 
nivel “intermedio” en el manejo del lenguaje, por lo que es buena idea 
que tengas una base sólida, sobre todo en cuanto a funciones al momento 
de profundizar e implementarlas.

Los decoradores son una forma sencilla de llamar funciones de orden mayor, 
es decir, funciones que toman otra función como parámetro y/o retornan otra 
función como resultado. De esta forma un decorador añade capacidades a una 
función sin modificarla.

Un ejemplo de esto son las llantas de un automóvil. Si les colocas cadenas 
para la nieve, el automóvil aún puede andar y además extiende su 
funcionalidad para conducirse en otros terrenos.

'Recordando funciones'

Antes de abordar el tema de decoradores haremos un pequeño repaso por las 
funciones, las cuales retornan un valor ante la entrada de un argumento.

Analicemos este sencillo ejemplo donde una función que multiplica un número 
se eleva a la tercera potencia:

def elevar_cubo(numero):
    return numero * numero * numero

'Funciones como objetos de primera-clase'

# Otro concepto importante a tener en cuenta es que en Python las funciones 
# son objetos de primera-clase, es decir, que pueden ser pasados y utilizados 
# como argumentos al igual que cualquier otro objeto (strings, enteros, 
# flotantes, listas, etc.).
# '''

# def presentarse(nombre):
#  	return f"Me llamo {nombre}"

# def estudiemos_juntos(nombre):
#  	return f"¡Hey {nombre}, aprendamos Python!"

# def consume_funciones(funcion_entrante):
#  	return funcion_entrante("Mishell")

# '''
# Las primeras dos funciones son obvias en su resultado, donde nos mostrarán 
# un mensaje con el valor de la variable nombre. La tercera función puede ser 
# más compleja de predecir, ya que toma otra función como entrada. Veamos que 
# pasa cuando colocamos una función como atributo:
# '''

# print(consume_funciones(presentarse))
# print(consume_funciones(estudiemos_juntos))

# '''
# Pongamos atención en cómo la función consume_funciones() se escribe con 
# paréntesis para ser ejecutada, mientras que la función presentarse y 
# estudiemos_juntos solo hace referencia a estas.
# '''

# Funciones anidadas

'''
Al igual que los condicionales y bucles tambien puedes colocar funciones
dentro de otra funcion.

'''

def funcion_mayor():
 	print("Esta es una función mayor y su mensaje de salida.")

 	def librerias():
          print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

 	def frameworks():
          print("Algunos frameworks de Python son: Django, Dash y Flask.")

funcion_mayor()

'''
Debemos considerar que las funciones anidadas dentro de funcion_mayor 
no se ejecutan hasta que se llama a esta primera, siendo muestra del 
scope o alcance de las funciones. Si las llamamos obtendremos un error
'''
