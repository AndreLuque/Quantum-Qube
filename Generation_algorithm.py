import numpy as np 
import random


class Generation:
	def __mv(self, num):
		if num.real % 2 == 1 and num.imag % 2 == 0:
			return True
		elif num.real % 2 == 0 and num.imag % 2 == 1:
			return True
		else:
			return False

	def __check(self, m):
		for i in range(4):
			counter = 0
			for j in range(4):
				if self.__mv(m[j][i]):
					counter += 1
				if self.__mv(m[i][j]):
					counter += 1
			if counter%2 != 0:
				return False
		return True	


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


	def generate(self, attempts=25):
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
				if self.__check(m) == True: # Check parity condition
					res.append(m)

		return res





