import numpy as np


class Gate:

    matrix: np.ndarray

    def __init__(self, matrix: np.ndarray):
        if not self.is_gate(matrix):
            raise ValueError("matrix not valid")
        self.__matrix = matrix

    @staticmethod
    def is_gate(matrix: np.ndarray) -> bool:
        pass

    def is_standard(self) -> bool:
        pass

    @property
    def matrix(self):
        return self.__matrix

    def __matmul__(self, other: 'Gate'):
        return self.__matrix @ other.matrix

    def __getitem__(self, item):
        return self.__matrix[item]

    def level(self) -> int:
        pass


class G(Gate):

    def __init__(self):
        super().__init__(np.array([[1, 0],
                                  [0, 1j]]))

    def __matmul__(self, other):
        pass

