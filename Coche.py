"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Jaime Rabasco
"""


class Vehiculo:
    color = 'rojo';
    fabricante = 'seat';
    num_serie = 1;


class Coche(Vehiculo):

    cilindrada = 1000;

    def __init__(self):
        """
        Autor: Luis Hidalgo Santaella
        Este es el constructor de la clase coche y devuelve un coche
        :rtype: object
        """
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def num_serie(self):
        """
        Autor: Luis Hidalgo Santaella
        Este es el metodo que hace referencia al número de serie y devuelve una cadena de números
        :rtype: object
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        self.__num_serie = value

    @property
    def color(self):
        """
        Autor: Luis Hidalgo Santaella
        Este metodo hace referencia al color del coche y devuelve un color
        :rtype: object
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        self.__color = value

    @property
    def cilindrada(self):
        """
        Autor: Luis Hidalgo Santaella
        Este metodo hace referencia a la cilindrada y devuelve un valor
        :rtype: object
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        Autor: Luis Hidalgo Santaella
        Este metodo hace referencia al fabricante y devuelve un valor
        :rtype: object
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value
