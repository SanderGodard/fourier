#!/usr/bin/env python3
from math import sin, cos, pi
from fakultet import fac
def main():
	print("Test av __str__:", bolge(1, 0, 10))
	return

class bolge:
	def __init__(self, l, c):
		if l != 0:		# Idiotsikring
			self.l = float(l)
		else:
			print("l (lengde) kan ikke være lik 0.")
			exit()
		self.c = float(c)	# Bølgens hastighet


# Generelle betingelser
	def A(self, n):
		return float(1) # La være konst for generell form

	def B(self, n):
		return float(0) # La være konst for generell form

# Eksempel 1
	# def f(self, x):
	# 	l = self.l
	# 	if x < l/2:
	# 		return x**3
	# 	else:
	# 		return x/4 + 1/4
		
	def A1(self, n):
		l = self.l
		ledd1 = -(l**3*(cos(n*pi/2)*n*pi**3 - 6*sin(n*pi/2)*n*pi**2 - 24*n*pi*cos(n*pi/2) + 48*sin(n*pi/2)))/(4*n*pi**4)
		ledd2 = (n*pi*cos(n*pi/2)*l - 2*n*pi*cos(n*pi)*l - 2*sin(n*pi/2)*l + 2*sin(n*pi)*l + 2*n*pi*cos(n*pi/2) - 2*n*pi*cos(n*pi))/(4*n*pi**2)
		return ledd1 + ledd2
	
	# def g(self, t):
	# 	return 0

	def B1(self, n):
		return 0

# Eksempel 2
	# def f(self, x):
	# 	return 0

	def A2(self, n):
		return 0
	
	# def g(self, t):
	# 	l = self.l
	# 	if t < l/4:
	# 		return 2*t
	# 	else:
	# 		return 2*t/3 + t/3

	def B2(self, n):
		l = self.l
		c = self.c
		ledd1 = -((n*pi*cos(n*pi/4) - 4*sin(n*pi/4))*l**2)/(c*n**2*pi**3)
		ledd2 = (l*(n*pi*cos(n*pi/4)*l - 4*n*pi*cos(n*pi)*l - 4*sin(n*pi/4)*l + 4*sin(n*pi)*l + 4*sin(n*pi)*l + 4*n*pi*cos(n*pi/4) - 4*n*pi*cos(n*pi)))/(3*c*n**2*pi**3)
		return ledd1 + ledd2



	def G(self, t, n):
		l = self.l
		c = self.c
		B = self.B1(n) # Endre her basert på hvilket eksempel som er i bruk!
		A = self.A1(n)
		return A*cos(n*pi*c*t/l) + B*sin(n*pi*c*t/l)

	def F(self, x, n):
		l = self.l
		return sin(n*pi*x/l)


	def un(self, x, t, n):
		l = self.l
		return self.F(x, n)*self.G(t, n)

	def u(self, x, t, n_max, n_start=0):
		l = self.l
		tot = 0
		for n in range(n_start, n_max+1):
			tot += self.F(x, n)*self.G(t, n)/(n_max)
		return tot

	def __str__(self):
		return f"t={self.t}, x={self.x}, l={self.l}, u={self.u(self.x, self.t)}"


if __name__ == "__main__":
	main()
