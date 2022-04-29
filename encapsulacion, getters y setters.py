# Encapsulación, getters and setters

# Encapsulacion

'''

Permite agrupar datos y su comportamiento.
Controla el accesos a dichos datos
Previene modificaciones no autorizadas

'''

# Ejemplo

class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
    
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, region):
        if region in self.__pais:
            self.__region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self.__pais}')

'''

casilla = CasillaDeVotacion(123, ['Ambato', 'Latacunga'])
casilla.region
'None'
casilla.region = 'Ambato'
casilla.region

'''

# Herencia

'''

Permite modelar una jerarquia de clases
Permite compartir comportamiento comun en la jerarquia
Al padre se le conoce como superclase y al hijo como subclase

'''

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())
    
# Polimorfismo

'''

La habilidad de tomar varias formas
En Python, nos permiten cambiar el comportamineto de una 
superclase para adaptarlo a la subclase

'''

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')
    
    def saluda(self, persona):
        print(f'Hola, {persona.nombre} soy {self.nombre}')


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()
    
# ¿Por qué graficar?

'''

Reconocimiento de patrones
Prediccion de una serie
Simplifica la interpretacion y las conclusiones acerca de los datos

'''

'''

Graficado simple

Bokeh permite construir graficas complejas de manera rapida y
con comandos simples

Permite exportar a varios formatos como html, notebooks, imagenes, etc.

Bokeh se pueden utilizar en el servido con Flask y Django

'''

# Libreria

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    
    total_vals = int(input('Cuantos valores quieres graficar?'))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}'))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)