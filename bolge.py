#!/usr/bin/env python3
from math import sin, cos, pi
from fakultet import fac
def main():
	print("Test av __str__:", bolge(1, 0, 10))
	return

class bolge:
	def __init__(self, t, x, l, n):
		self.t = float(t)
		self.x = float(x)
		if l != 0:
			self.l = float(l)
		else:
			print("l (lengde) kan ikke være lik 0.")
			exit()
		self.n = float(n)

#		self.c = float(-x**2) # TODO Skal c faktisk være lysfarten??
		self.c = float(3*10**8) # lysets hastighet

	def convolution(self, a, b):
		# https://stackoverflow.com/questions/1222147/convolution-of-two-functions-in-python
		# TODO skrive en funksjon her. Bare mulig med CA verdi, ellers må bytte til octave
		return a*b

	def lamda(self, n):
		l = self.l
		c = self.c
		return float(2)*pi*n*c/l

	def B(self, n):
		# TODO hvis avansert må bytte til octave
		return float(1)

	def G(self, t):
		l = self.l
		n = self.n
		lamda = self.lamda(n)
		B = self.B(n)
		return B*cos(lamda)*t+self.convolution(B, sin(lamda)*t)

	def F(self, x):
		l = self.l
		n = self.n
		return sin(n*pi/l)*x

	def uk(self, x, t, k):
		l = self.l
		return (cos(pi/l * k * t)) * (sin(pi/l * k * x))

	def u(self, x, t):
		l = self.l
		return self.F(x)*self.G(t)

	# TODO transform???
#	def transform(self):
#		t = self.t
#		return t/fac(t)

#	def getfreq(self):
#		return self.transform(self.t)

#	def calculate(self):
#		self.x = getx()
#		self.freq = getfreq()

	def __str__(self):
		return f"t={self.t}, x={self.x}, l={self.l}, u={self.u(self.x, self.t)}"


if __name__ == "__main__":
	main()
