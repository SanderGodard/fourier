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

	def f(self, x):
		return x**2

	def g(self, x):
		return 0

	def integr_f(self, x):
		x = self.l
		return 1/3*x**3

	def integr_g(self, x):
		return 0

	def A(self, n):
		l = self.l
		return float(1) # La være konst for nå, regnes ut senere.
		return 2/l * integr_f(l) * cos(n*pi*l/l) * l/(n*pi) # Dette er feil, tar ikke hensyn til at det er integrasjon av et produkt hvor begge faktoerene har x.

	def B(self, n):
		return float(0) # La være konst
		return 2/(self.c*n*pi) * integr_f(l) * cos(n*pi*l/l) * l/(n*pi) # er feil btw

	def G(self, t, n):
		l = self.l
		c = self.c
		B = self.B(n)
		A = self.A(n)
		return A*cos(n*pi*c*t/l) + B*sin(n*pi*c*t/l)

	def F(self, x, n):
		l = self.l
		return sin(n*pi*x/l)

#	def uk(self, x, t, k):
#		l = self.l
#		return cos(pi/l * k * t)*sin(pi/l * k * x)

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
