from math import sqrt
from spicy.integrate import quad

def fact(n):
	factorial=1
	if n>0:
		for i in range(1, n+1):
			factorial= factorial*i
	else:
		return "ValueError"
	return factorial
	pass

def roots(a, b, c):
	try:
		square=sqrt(b**2-4*a*c)
		if square==0:
			return [int('%.0f'%(-b/2*a))]
		else:
			answer=[]
			i=1
			while i!=2:
				answer.append(int('%.0f'%(-b+i*square)/2*a))
	except ValueError:
		return []
	pass

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	x2= lambda x: function
	answer=integrate.quad(x2, lower, upper)
	return [0]
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 2, 1))
	print(integrate('x ** 2 - 1', -1, 1))
