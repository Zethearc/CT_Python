# Programacion orientada a objetos en Python

'''

Uno de los elementos mas importates de los lenguajes de
programacion es la utilizacion de clases para organizar
programas en modulos y abstracciones de datos.

Por ejemplo, podemos representar a una persona con 
propiedades como nombre, edad, genero, etc. y los 
comportamientos de dicha persona como caminar, cantar,
comer, etc. De la misma manera podemos representar unos
propiedades como su marca, tamano, color, etc. y sus
comportamientos como reproducir musica, pausar y avanzar
a la siguiente cancion.

Puesto de otra manera, la programacion orientada a
objetos nos permite modelar cosas reales u concretas del
mundo y sus relaciones con otros objetos.

'''

# Clases en Python

'''

Las estructuras primitivas con las que hemos trabajado
hasta ahora nos permiten definir cosas sencillas, como
el costo de algo, el nombre de un usuario, las veces que
debe correr un bucle, etc. Sin embargo, existen ocasiones
cuando necesitamos definir estructuras mas complejas, por
ekemplo un hotel. Podriamos utilizar dos listas: una para
definir los cuartos y una segunda para definir si el 
cuarto se encuentra ocupado o no.

'''

cuartos_de_hotel =   [101,   102,    103,    201,    202,    203]
cuarto_ocupado =    [True,  False,  False,  True,   True,   False]

'''

Sin embargo, este tipo de organizacion rapidamente se sale
de control. Que tal que quisieramos añadir mas propiedades,
como si el cuarto ya fue aseado o no? Si el cuarto tiene
cama doble o sencilla? Esto nos lleva a una falta fuerte de
organizacion y es justamente el punto que justifica la
existencia de clases

Las clases nos permiten crear nuevos tipos que contiene
informacion arbitraria sobre un objeto. En el caso del hotel,
podriamos crear dos clases Hotel() y Cuarto() que nos
permitieran dar seguiento a las propiedades como numero de
cuartos, ocupacion, aseo, tipo de habitacion, etc.

Es importante resaltar que las clases solo proveen estructura.
Son un molde con el cual podemos construir objetos especificos.
La clase señala las propiedades que los hoteles que modelemos
tendra, pero no es ningun hotel especifico. Para eso necesitamos
las instancias

'''

# Instancias

'''

Mientras que las clases proveen la estrucura, las instancias
son los objetos reales que creamos en nuestro programa: un
hotel llamado Hilton Plaza. Otra forma de pensarlo es que las
clases son como formularios y una vez que se llena cada copia
del formulario tenemos las instancias que pertenecen a dicha
clase. Cada copia puede tener datos distintos, al igual que 
cada instancia es distinta de las demas. 
(Aunque todas pertenecen a una misma clase)

'''

'Para definir una clase, simplemente utilizamos el Keyword class'

class Hotel:
    pass

'Una vez que tenemos una clase llamada Hotel podemos generar una instancia'

hotel = Hotel()

# Atributos de la instancia

'''

Todas las clases crean objetos y todos los objetos tienen
atributos. Utilizamos el metodo especial __init__ para 
definir el estado inicial de nuestra instancia. Recibe como
primer parametro obligatorio "self" (que es simplemente una
referencia a la instancia)

'''

class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0


hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
# print(hotel.lugares_de_estacionamiento)

##resultado esperado "20"

# Metodos de instancia

'''

Mientras que los atributos de la instancia describen lo que 
representa el objeto, los metodos de instancia nos indican
que podemos hacer con las instancias de dicha clase y normalmente
operan en los mencionados atributos. Los metodos son equivalentes 
a funciones dentro de la definicion de la clase, pero todos reciben
self como primer argumentos

'''

class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0
    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


# hotel = Hotel(50, 20)
# print(hotel.ocupacion_total())
# hotel.anadir_huespedes(3)
# print(hotel.ocupacion_total())
# hotel.checkout(1)
# print(hotel.ocupacion_total())
# hotel.ocupacion_total()

'Ahora ya sabemos que son las clases '
