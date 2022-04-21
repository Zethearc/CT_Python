# Tipos de datos abstractos

'''

En Python todo es un objeto y tiene un tipo.
    Representacion de datos y formas de intereactuar
    con ellos

Formas de interactuar con un objeto:
    Creacion
    Manipulacion
    Destruccion
    
Ventajas:
    Decomposicion
    Abstraccion
    Encapsulacion

'''

# Definicion de clase

# class <nombre_de_la_clase> (<super_clase>):
#     def __init__(self, <params>):
#         <expresion>
#     def <nombre_del_metodo>(self, <params>):        
#         <expresion>

# Ejemplo

class persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

# Uso del ejemplo

david = persona('David', 35)
erika = persona('Erika', 32)

print(david.saluda(erika))

# Instancia

'''

Los atributos de clase nos permiten:
    Representar datos
    Procedimientos para interacturar con los mismo (metodos)
    Mecanismos para esconder la representacion interna

Se accede a los atributos con la notacion de punto

Puede tener atributos privados. Por convencion comienzan con "_"

'''

class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))