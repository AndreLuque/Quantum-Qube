import numpy as np 
import random


class Generation:
	def __restriccion_fila_columna(matrix_colors: np.ndarray, cumple = True) -> bool:
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

	def __restriccion_dos_fila_columna(matrix_colors: np.ndarray, cumple = True) -> bool:
		#primero evaluaremos las filas y luego las columnas (range(2)), iremos de una en una y las compararemos con todas 
		#las demas analizando si cumple los requisitos de las restricciones
		t:int = 0
		while cumple and t < 2:
			i: int = 0
			while cumple and i < matrix_colors.shape[t]:
				#tendremos que comparar cada fila con las demas por lo que construimos una nueva matriz que contiene a todas menos esta fila
				matrix_colors_new: np.ndarray = np.delete(matrix_colors, i, axis = t)
				j: int = 0
				while cumple and j < matrix_colors_new.shape[t]:
					suma_restriccion1: int = 0
					suma_restriccion2: int = 0
					k: int = 0
					#si son filas compararemos de una forma y si son columnas de otra
					while cumple and k < matrix_colors_new.shape[(t + 1) % 2]:
						#FILAS
						if t == 0:
							if (matrix_colors[i, k] == 2 and matrix_colors_new[j, k] == 3) or (matrix_colors[i, k] == 2 and matrix_colors_new[j, k] == 4) or (matrix_colors[i, k] == 3 and matrix_colors_new[j, k] == 4):	
								print('jaksj')
								suma_restriccion1 += 1
							if (matrix_colors[i, k] == 2 and matrix_colors_new[j, k] == 3) or (matrix_colors[i, k] == 2 and matrix_colors_new[j, k] == 4) or (matrix_colors[i, k] == 3 and matrix_colors_new[j, k] == 3) or (matrix_colors[i, k] == 4 and matrix_colors_new[j, k] == 4):
								print('asjd')
								suma_restriccion2 += 1	
						#COLUMNAS
						elif t == 1:
							if (matrix_colors[k, i] == 2 and matrix_colors_new[k, j] == 3) or (matrix_colors[k, i] == 2 and matrix_colors_new[k, j] == 4) or (matrix_colors[k, i] == 3 and matrix_colors_new[k, j] == 4):	
								suma_restriccion1 += 1
							if (matrix_colors[k, i] == 2 and matrix_colors_new[k, j] == 3) or (matrix_colors[k, i] == 2 and matrix_colors_new[k, j] == 4) or (matrix_colors[k, i] == 3 and matrix_colors_new[k, j] == 3) or (matrix_colors[k, i] == 4 and matrix_colors_new[k, j] == 4):
								suma_restriccion2 += 1
						k += 1		
						
					#comprobamos que la suma final ha dado un numero par
					if suma_restriccion1 % 2 != 0 or suma_restriccion2 % 2 != 0:
						cumple = False
					j += 1
				i += 1		
			t += 1	


		#retornamos el booleano que dira si se han cumplido las restricciones		
		print(cumple)	
		return cumple	


	def __get_complex(self):
		a = random.randint(-10, 10)
		b = random.randint(-10, 10)
		return complex(a, b)


	def __Gram_Schmidt(self, m):
		v1 = m[0]
		v2 = m[1]
		v3 = m[2]
		v4 = m[3]

		u1 = v1

		u2 = v2 - (np.vdot(u1,v2)/np.vdot(u1,u1))*u1 
		u2 *= np.vdot(u1,u1)

		u3 = v3 - (np.vdot(u1,v3)/np.vdot(u1,u1))*u1 - (np.vdot(u2,v3)/np.vdot(u2,u2))*u2
		u3 *= np.vdot(u1,u1) * np.vdot(u2,u2)

		u4 = v4 - (np.vdot(u1,v4)/np.vdot(u1,u1))*u1 - (np.vdot(u2,v4)/np.vdot(u2,u2))*u2 - (np.vdot(u3,v4)/np.vdot(u3,u3))*u3
		u4 *= np.vdot(u1,u1) * np.vdot(u2,u2) * np.vdot(u3,u3)

		return np.array([u1, u2, u3, u4])


	def generate(self, attempts=10000):
		'''
		-Sea Λ nuestra matriz buscada. Λ se genera con una probabilidad de entre 19.622% y 20% de probabilidades. 
		-De media, Λ se genera cada 4,1168 matrices. 
		-Para generar una matriz con ≈95% de probabilidades hace falta generar 15 matrices.
		-Es recomendado poner un numero de generación >20
		'''
		res = []
		for i in range(attempts):
			temp = np.array([[self.__get_complex() for _ in range(4)] for _ in range(4)]) # Generate 4x4 matrix
			if np.linalg.matrix_rank(temp) == 4: # Check if it is R4 base
				m = self.__Gram_Schmidt(temp) # Orthogonalize the matrix
				if self.__restriccion_fila_columna and self.__restriccion_dos_fila_columna: # Check parity condition
					res.append(m)

		return res


