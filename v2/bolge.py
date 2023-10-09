#!/usr/bin/env python3
from math import sin, cos, pi

def main():
	print("Test av __str__:", bolge(1, 0, 10))
	return

class bolge:
	def __init__(self, l, n_max, k=1):
		#self.t = float(t) # Settes hos u(x, t)
		#self.x = float(x)
		if l != 0: # Dette er en av initialbetingelsene, kan ikke beregnes her :)
			self.l = float(l)
		else:
			print("l (lengde) kan ikke være lik 0.")
			exit()
		self.k = k
		self.n_max = n_max
		self.c = float(5) # Konstant for testmiljøet.
#		self.c = 3e8


	def A(self, n): # Må finne verdier for disse!
		if n == 0:
			return float(1)
		return float(0)

	def B(self, n): # Må finne verdier for disse!
		return float(1)

	def G_n(self, t, n):
		B = self.B(n)
		A = self.A(n)
		return self.A(n)*cos(n*pi*self.c*t/self.l)+self.B(n)*sin(n*pi*self.c*t/self.l)

	def F_n(self, x, n):
		return self.B(n)*sin(n*pi*x/self.l)


	def u_n(self, x, t, n):
		return self.F_n(x, n)*self.G_n(t, n)

	def uk(self, x, t):
		#k er harmoniske svingning
		return cos((self.k)*pi*self.c*t/self.l)*sin((self.k)*pi*x/self.l)

	def u(self, x, t):
		tot = 0
		for n in range(self.n_max+1):
			tot += self.u_n(x, t, round(float(n), 2))
		return tot

	def __str__(self):
		return f"Bølge: l={self.l}"


if __name__ == "__main__":
	main()
