import numpy as np
import cmath
from typing import List, NoReturn, TypeVar, Optional

def restriccion_fila_columna(matrix_colors: np.ndarray, cumple = True) -> bool:
	#para cada fila y columna, la suma del numero de nodos verdes y nodos morados debe ser par
	#primero creamos una nueva matriz para almacenar los valores de esta suma
	matrix_restrictions = np.zeros((2,4))

	#recorremos la matriz en busca de nodos morados y verdes sumando sus cantidades en cada columna y fila
	for row in range(matrix_colors.shape[0]):
		for column in range(matrix_colors.shape[1]):
			if matrix_colors[row, column] == 3 or matrix_colors[row, column] == 4:
				matrix_restrictions[0, row] += 1
				matrix_restrictions[1, column] += 1

	#ahora recorremos la matriz de restricciones y comprobamos que se han cumplido todas las restricciones
	#inicializamos valores de i y j.
	i: int = 0			
	j: int = 0
	while cumple and i < matrix_restrictions.shape[0]:
		while cumple and j < matrix_restrictions.shape[1]:
			if matrix_restrictions[i, j] % 2 != 0:
				cumple = False
			j += 1
		i += 1			

	#retornamos el booleano que dira si se han cumplido las restricciones			
	return cumple			

def coloracion(matrix_qube: np.ndarray, matrix_colors: np.ndarray) -> np.array:
	# 0 = sin color
	# 1 = rojo
	# 2 = azul
	# 3 = morado
	# 4 = verde

	#accedemos a las diferentes posicones de la matriz utlizando un doble bucle
	for row in range(matrix_qube.shape[0]):
		for column in range(matrix_qube.shape[1]):
			#analizamos la parte real y la parte imaginaria viendo si es par o impar. En funcion de estp, asignamos el color correspondiente
			if matrix_qube[row, column].real % 2 == 0 and matrix_qube[row, column].imag % 2 == 0:
				matrix_colors[row, column] = 1
			elif matrix_qube[row, column].real % 2 != 0 and matrix_qube[row, column].imag % 2 != 0:
				matrix_colors[row, column] = 2
			elif matrix_qube[row, column].real % 2 == 0 and matrix_qube[row, column].imag % 2 != 0:
				matrix_colors[row, column] = 3
			else:
				matrix_colors[row, column] = 4
	
	#debemos comprobar que estos nuevos colores cumplen las restricciones impuestas
	cumple_restriccion_fila_columna: bool = restriccion_fila_columna(matrix_colors)

	if cumple_restriccion_fila_columna:
		return matrix_colors
	else:
		return np.zeros((4, 4))	


#creamos la matriz que almacenara los colores
matrix_colors = np.zeros((4,4))

#creamos una matriz de las posiciones de nuestro quantum qube (usamos el ejemplo que esta en las dispositivas)
matrix_qube = np.array([[complex(1, 2), complex(3, 4), 4], [1, 2, 4]], dtype = complex)

#actualizamos los valores de los colores
matrix_colors = coloracion(matrix_qube, matrix_colors)