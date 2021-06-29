import numpy as np
from copy import deepcopy
from typing import List, TypeVar, NoReturn, Optional, Tuple


H_2 = 1/np.sqrt(2) * np.array([[1, 1],
                               [1, -1]])
V = np.array([[1, 0],
             [0, 1j]])


class QuantumQube():

    matrix: np.ndarray

    def __init__(self, matrix: np.ndarray):
        self.__matrix = matrix
        self.__color_matrix = QuantumQube.get_color_matrix(matrix)
        if not self.is_reducible():
            raise ValueError('The given QuantumQube is not reducible')

    @property
    def color_matrix(self) -> np.ndarray:
        return self.__color_matrix

    @property
    def matrix(self) -> np.ndarray:
        return self.__matrix

    @staticmethod
    def get_color(z: complex) -> int:
        """
        colours:
        (par, par) -> red -> 1
        (impar, impar) -> blue -> 2
        (par, impar) -> purple -> 3
        (impar, par) -> green -> 4
        :param z: a complex number
        :return: the colour (int)
        """
        if z.real % 2:
            if z.imag % 2:
                return 1
            else:
                return 3
        elif z.imag % 2:
            return 4
        else:
            return 2

    @staticmethod
    def get_color_matrix(matrix: np.ndarray) -> np.ndarray:
        color_matrix = np.zeros(matrix.shape)

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                color_matrix[i][j] = QuantumQube.get_color(value)

        return color_matrix

    def get_submatrices(self, inplace: bool = False) -> Tuple[np.ndarray, np.ndarray,
                                                      np.ndarray, np.ndarray]:
        """
        Se divide la matriz en cuatro submatrices conservando la matriz original. Notación:
        número del cuadrante: [1, 2]
                              [3, 4]
        :param inplace: si es True, devolverá una copia de las matrices. Si está desactivado, todos los cambios que se
                        realicen a las submatrices afectarán a 'self.__matrix' y viceversa. Desactivado por defecto.
        :return: (cuadrante 1, cuadrante 2, cuadrante 3, cuadrante 4)
        """
        n = len(self.__matrix)
        if inplace:
            a = self.__matrix[:n // 2, :n // 2]
            b = self.__matrix[:n // 2, n // 2:]
            c = self.__matrix[:n // 2, :n // 2]
            d = self.__matrix[:n // 2, :n // 2]
        else:
            a = deepcopy(self.__matrix[:n // 2, :n // 2])
            b = deepcopy(self.__matrix[:n // 2, n // 2:])
            c = deepcopy(self.__matrix[:n // 2, :n // 2])
            d = deepcopy(self.__matrix[:n // 2, :n // 2])

        return a, b, c, d

    def is_reducible(self) -> bool:
        return True

    #definimos las funciones que representaran las transformaciones
    def permutacion_filas(self, tipo_permutacion: int) -> NoReturn:
        """
        el valor entero dado por la variable tipo_permutacion nos indicara que filas se permutan
        1 -> filas 0 y 1
        2 -> filas 1 y 2
        3 -> filas 2 y 3
        """
        self.__matrix[[tipo_permutacion - 1, tipo_permutacion], :] = self.__matrix[[tipo_permutacion, tipo_permutacion - 1], :]

        #actualizamos los colores
        self.__color_matrix = QuantumQube.get_color_matrix(self.__matrix)
        
    def permutacion_columnas(self, tipo_permutacion: int) -> NoReturn:
        """
        el valor entero dado por la variable tipo_permutacion nos indicara que filas se permutan
        1 -> columnas 0 y 1
        2 -> columnas 1 y 2
        3 -> columnas 2 y 3
        4 -> columnas 3 y 0
        """
        self.__matrix[:, [tipo_permutacion - 1, tipo_permutacion % 4]] = self.__matrix[:, [tipo_permutacion % 4, tipo_permutacion - 1]]        

        #actualizamos los colores
        self.__color_matrix = QuantumQube.get_color_matrix(self.__matrix)

    def cambio_de_colores(self, columna_o_fila: int, numero_columna_fila: int) -> NoReturn:
        """
        el valor de la variable columna_o_fila nos indicara si hacemos el cambio de color en una fila o columna
        0 -> fila
        1 -> columna
        
        el valor de la variable numero_columna_fila nos indicara en que fila o columna hay que hacer el cambio de color

        solo se podrá cambiar los morados a verdes y viceversa. Esto se hace multiplicando i por esa fila o columna
        cambiara la parte real e imaginaria de par a impar y de impar a par haciendo que se cambien estos colores.
        """        
        if columna_o_fila == 0:
            self.__matrix[numero_columna_fila, :] = self.__matrix[numero_columna_fila, :] * complex(0, 1)
        else:
            self.__matrix[:, numero_columna_fila] = self.__matrix[:, numero_columna_fila] * complex(0, 1)    

        #actualizamos los colores
        self.__color_matrix = QuantumQube.get_color_matrix(self.__matrix)



#tests
matrix_qube = np.array([[complex(1, 2), complex(3, 4), 4, 4], [1, 2, 4, 4]], dtype = complex)
qube = QuantumQube(matrix_qube)
qube.permutacion_columnas(2)   

print(qube.color_matrix)
qube.cambio_de_colores(1, 0)
print(qube.color_matrix)


