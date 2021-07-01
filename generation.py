import numpy as np 
import random




def mv(num):
	if num.real % 2 == 1 and num.imag % 2 == 0:
		return True
	elif num.real % 2 == 0 and num.imag % 2 == 1:
		return True
	else:
		return False


def check(m): # PENDIENTE DE REVISION
	for i in range(4):
		columnas = 0
		filas = 0
		for j in range(4):
			if mv(m[j][i]):
				columnas += 1
			if mv(m[i][j]):
				filas += 1

		if columnas%2 != 0 or filas%2 != 0:
			return False
	return True	



'''
def check1(m): # PENDIENTE DE REVISION
	filas = []
	columnas = []

	for i in range(4):
		filas.append([m[i][j] for j in range(4)])
		columnas.append([m[j][i] for j in range(4)])

	#print('\nFILAS')
	for k in filas:
		count = 0
		for h in k:
			if mv(h):
				count += 1
		#print(f'fila: {k}, hits: {count}')
		if count %2 != 0:
			return False

	#print('\nCOLUMNAS')
	for k in columnas:
		count = 0
		for h in k:
			if mv(h):
				count += 1
		#print(f'columna: {k}, hits: {count}')
		if count %2 != 0:
			return False
	

	return True	

l = np.array([[complex( 7,  2), complex(-2, -2), complex( 1, -1), complex( 0,  1)],
			  [complex( 3,  0), complex( 6,  4), complex( 1,  1), complex( 0, -1)],
			  [complex(-1, -1), complex(-1,  1), complex( 7,  1), complex(-1,  3)],
			  [complex( 0,  0), complex( 1, -1), complex(-1,  3), complex( 6,  4)]])

check(l)
'''

def get_complex():
	a = random.randint(-10, 10)
	b = random.randint(-10, 10)
	return complex(a, b)



def Gram_Schmidt(m):
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



'''

print('Waiting user to start.')
attempts = int(input('Number of attempts: '))

print('Start processing...')

hit1 = 0
hit2 = 0
for i in range(attempts):
	h = np.array([[get_complex() for _ in range(4)] for _ in range(4)])
	if np.linalg.matrix_rank(h) == 4:
		hit1 += 1
		m = Gram_Schmidt(h)
		if check(m):
			hit2 += 1
			#print(f'\nMatrix found!\nMatrix found after {i} tries. ')
			#print('Matrix:\n', m)
			#print()

print('\nSummary:')
print(f'Total attempts: {attempts}   Matrix base hits: {hit1}   Total Matrix accurated hits: {hit2}  Missing: {attempts - hit2}  Hit rate: {round(100*hit2/attempts, 3)}%')		
input()

'''

print('Waiting user to start.')
attempts = int(input('Number of attempts: '))

def main():
	print('Start processing...')

	hit1 = 0
	hit2 = 0
	for i in range(attempts):
		h = np.array([[get_complex() for _ in range(4)] for _ in range(4)])
		if np.linalg.matrix_rank(h) == 4:
			hit1 += 1
			m = Gram_Schmidt(h)
			if check(m):
				return i
	return attempts


print('\nSummary:')
print(f'Total attempts: {attempts}   Total attempts needed: {main()}')		
input()
