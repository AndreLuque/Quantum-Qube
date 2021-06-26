import numpy as np
from gates import Gate


H_2 = Gate((1/np.sqrt(2)) * np.array([[1, 1],
                                   [1, -1]]))
V = Gate(np.array([[1, 0],
                  [0, 1j]]))


class QuantumQube:

    matrix: np.ndarray

    def __init__(self, matrix: np.ndarray):
        self.__matrix = Gate(matrix)

    @staticmethod
    def get_color(z: complex) -> int:
        """
        colors:
        (even, even) -> red -> 0
        (odd, odd) -> blue -> 1
        (even, odd) -> purple -> 2
        (odd, even) -> green -> 3
        :param z: a complex number
        :return: the color (int)
        """

    def get_submatrices(self) -> tuple[np.ndarray, np.ndarray,
                                       np.ndarray, np.ndarray]:
        pass
