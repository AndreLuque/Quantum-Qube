import numpy as np


def restriccion_fila_columna(color_matrix: np.ndarray, cumple=True) -> bool:
    # para cada fila y columna, la suma del numero de nodos verdes y nodos morados debe ser par
    # primero creamos una nueva matriz para almacenar los valores de esta suma
    matrix_restrictions = np.zeros((2, 4))

    # recorremos la matriz en busca de nodos morados y verdes sumando sus cantidades en cada columna y fila
    for row in range(color_matrix.shape[0]):
        for column in range(color_matrix.shape[1]):
            if color_matrix[row, column] == 3 or color_matrix[row, column] == 4:
                matrix_restrictions[0, row] += 1
                matrix_restrictions[1, column] += 1

    # ahora recorremos la matriz de restricciones y comprobamos que se han cumplido todas las restricciones
    # inicializamos valores de i y j.
    i: int = 0
    j: int = 0
    while cumple and i < matrix_restrictions.shape[0]:
        while cumple and j < matrix_restrictions.shape[1]:
            if matrix_restrictions[i, j] % 2 != 0:
                cumple = False
            j += 1
        i += 1

    # retornamos el booleano que dira si se han cumplido las restricciones
    return cumple


def restriccion_dos_fila_columna(color_matrix: np.ndarray, flag=True) -> bool:
    # primero evaluaremos las filas y luego las columnas (range(2)), iremos de una en una y las compararemos con todas
    # las demas analizando si cumple los requisitos de las restricciones
    t: int = 0
    while flag and t < 2:
        i: int = 0
        while flag and i < color_matrix.shape[t]:
            # tendremos que comparar cada fila con las demas por lo que construimos una nueva matriz que contiene a
            # todas menos esta fila
            matrix_colors_new: np.ndarray = np.delete(color_matrix, i, axis=t)
            j: int = 0
            while flag and j < matrix_colors_new.shape[t]:
                suma_restriccion1: int = 0
                suma_restriccion2: int = 0
                k: int = 0
                # si son filas compararemos de una forma y si son columnas de otra
                while flag and k < matrix_colors_new.shape[(t + 1) % 2]:
                    # FILAS
                    if t == 0:
                        if (color_matrix[i, k] == 2 and matrix_colors_new[j, k] == 3) or (
                                color_matrix[i, k] == 2 and matrix_colors_new[j, k] == 4) or (
                                color_matrix[i, k] == 3 and matrix_colors_new[j, k] == 4):
                            print('jaksj')
                            suma_restriccion1 += 1
                        if (color_matrix[i, k] == 2 and matrix_colors_new[j, k] == 3) or (
                                color_matrix[i, k] == 2 and matrix_colors_new[j, k] == 4) or (
                                color_matrix[i, k] == 3 and matrix_colors_new[j, k] == 3) or (
                                color_matrix[i, k] == 4 and matrix_colors_new[j, k] == 4):
                            print('asjd')
                            suma_restriccion2 += 1
                    # COLUMNAS
                    elif t == 1:
                        if (color_matrix[k, i] == 2 and matrix_colors_new[k, j] == 3) or (
                                color_matrix[k, i] == 2 and matrix_colors_new[k, j] == 4) or (
                                color_matrix[k, i] == 3 and matrix_colors_new[k, j] == 4):
                            suma_restriccion1 += 1
                        if (color_matrix[k, i] == 2 and matrix_colors_new[k, j] == 3) or (
                                color_matrix[k, i] == 2 and matrix_colors_new[k, j] == 4) or (
                                color_matrix[k, i] == 3 and matrix_colors_new[k, j] == 3) or (
                                color_matrix[k, i] == 4 and matrix_colors_new[k, j] == 4):
                            suma_restriccion2 += 1
                    k += 1

                # comprobamos que la suma final ha dado un numero par
                if suma_restriccion1 % 2 != 0 or suma_restriccion2 % 2 != 0:
                    flag = False
                j += 1
            i += 1
        t += 1

    # retornamos el booleano que dira si se han cumplido las restricciones
    print(flag)
    return flag


def coloracion(matrix_qube: np.ndarray, color_matrix: np.ndarray) -> np.ndarray:
    # 0 = sin color
    # 1 = rojo
    # 2 = azul
    # 3 = morado
    # 4 = verde

    # accedemos a las diferentes posicones de la matriz utilizando un doble bucle
    for row in range(matrix_qube.shape[0]):
        for column in range(matrix_qube.shape[1]):
            # analizamos la parte real y la parte imaginaria viendo si es par o impar. En funcion de estp, asignamos el
            # color correspondiente
            if matrix_qube[row, column].real % 2 == 0 and matrix_qube[row, column].imag % 2 == 0:
                color_matrix[row, column] = 1
            elif matrix_qube[row, column].real % 2 != 0 and matrix_qube[row, column].imag % 2 != 0:
                color_matrix[row, column] = 2
            elif matrix_qube[row, column].real % 2 == 0 and matrix_qube[row, column].imag % 2 != 0:
                color_matrix[row, column] = 3
            else:
                color_matrix[row, column] = 4

    # debemos comprobar que estos nuevos colores cumplen las restricciones impuestas
    cumple_restriccion_fila_columna: bool = restriccion_fila_columna(color_matrix)
    cumple_restriccion_dos_fila_columna: bool = restriccion_dos_fila_columna(color_matrix)

    if cumple_restriccion_fila_columna:
        return color_matrix
    else:
        return np.zeros((4, 4))


# creamos la matriz que almacenara los colores
matrix_colors = np.zeros((4, 4))

# creamos una matriz de las posiciones de nuestro quantum qube (usamos el ejemplo que esta en las dispositivas)
matrix_qube = np.array([[complex(1, 2), complex(3, 4), 4], [1, 2, 4]], dtype=complex)

# actualizamos los valores de los colores
matrix_colors = coloracion(matrix_qube, matrix_colors)

test_matrix = np.array([[3, 1, 3], [4, 1, 4], [1, 1, 1]])
print(test_matrix)
restriccion_dos_fila_columna(test_matrix)
# deberia dar true
