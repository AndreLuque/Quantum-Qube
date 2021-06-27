import numpy as np 
import random


def get_complex():
	a = random.randint(-100, 100)
	b = random.randint(-100, 100)
	return complex(a, b)




col1 = np.array([complex(7, 2), complex(3, 0), complex(-1, -1), complex(0, 0)])
col2 = np.array([complex(-2, -2), complex(6, 4), complex(-1, 1), complex(1, -1)])
col3 = np.array([complex(1, -1), complex(1, 1), complex(7, 1), complex(-1, 3)])
col4 = np.array([complex(0, 1), complex(0, -1), complex(-1, 3), complex(6, 4)])

k = [col1, col2, col3, col4]



def mv(num):
	if num.real % 2 == 1 and num.imag % 2 == 0:
		return True
	elif num.real % 2 == 0 and num.imag % 2 == 1:
		return True
	else:
		return False

def check1(m):
	for i in range(4):
		counter = 0
		for j in range(4):
			if mv(m[j][i]):
				counter += 1
			if mv(m[i][j]):
				counter += 1
		if counter%2 != 0:
			return False
	return True	

def check2(m):
	l = []
	l.append(np.vdot(m[0],m[1]))
	l.append(np.vdot(m[0],m[2]))
	l.append(np.vdot(m[0],m[3]))
	l.append(np.vdot(m[1],m[2]))
	l.append(np.vdot(m[1],m[3]))
	l.append(np.vdot(m[2],m[3]))

	for i in l:
		if i != 0:
			return False

	return True


def check(m):

	if check1(m) == True and check2(m) == True:
		return	True
	return check1(m), check2(m)




def generate():
	return [[get_complex() for _ in range(4)] for _ in range(4)]



def main():
	attempts = 5000000

	par  = 0
	orto = 0
	print('Working...')
	for i in range(attempts):
		
		m = generate()
		
		score = check(m)
		
		if score == True:
			print('MATRIX FOUND!')
			print(m)
			return None
		else:
			par += int(score[0])
			orto += int(score[1])

	print(f'Parity hits: {par}\nOrthogonal hits: {orto}\nAttempts: {attempts}')


main()














'''
for i in range(4):
	counter = 0
	for j in range(4):
		if mv(k[j][i]):
			counter += 1

	if counter%2 != 0:
		print('ERROR')

	


for i in range(4):
	counter = 0
	for j in range(4):
		if mv(k[i][j]):
			counter += 1

	if counter%2 != 0:
		print('ERROR')

'''













