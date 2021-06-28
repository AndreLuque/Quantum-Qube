import numpy as np
from copy import deepcopy


H_2 = 1/np.sqrt(2) * np.array([[1, 1],
                               [1, -1]])
V = np.array([[1, 0],
             [0, 1j]])


class QuantumQube:

    matrix: np.ndarray

    def __init__(self, matrix: np.ndarray):
        self.__matrix = matrix
        self.__color_matrix = QuantumQube.get_color_matrix(matrix)
        if not self.is_reducible():
            raise ValueError('The given QuantumQube is not reducible')

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

    def get_submatrices(self, inplace: bool = False) -> tuple[np.ndarray, np.ndarray,
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
        pass


