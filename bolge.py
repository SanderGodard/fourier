#!/usr/bin/env python3
from math import sin, cos, pi

# Bølgeberegninger. Er her man bytter ut eksempelbølgene.
# For å benytte seg av ulike initialverdier må man endre A og B "funksjonstallene" på linje 60.

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
	def A1(self, n):
		l = self.l
		return (2*(2*sin((pi*n)/2)-2*sin(pi*n)+pi*n*cos((pi*n)/2)))/(pi**2*n**2)-(2*(pi*n*(pi**2*n**2-24)*cos((pi*n)/2)-6*(pi**2*n**2-8)*sin((pi*n)/2)))/(pi**4*n**4)
	
	def B1(self, n):
		return 0

# Eksempel 2
	def A2(self, n):
		return 0
	
	def B2(self, n):
		l = self.l
		c = self.c
		return (4*l*(pi*n-sin(pi*n)))/(pi**3*c*n**3)

# Eksempel 3
	def A3(self, n):
		l = self.l
		return 2/l*(l*(4*pi*n*sin(l/2)*cos(pi*n)-2*l*cos(l/2)*sin(pi*n)))/(l**2-4*pi**2*n**2)

	def B3(self, n):
		l = self.l
		c = self.c
		return 2/(n*pi*c)*(l*(l*sin(l)*sin(pi*n)+pi*n*cos(l)*cos(pi*n)-pi*n))/(l**2-pi**2*n**2)



	def G(self, t, n):
		l = self.l
		c = self.c
		B = self.B(n) # Endre her basert på hvilket eksempel som er i bruk!
		A = self.A(n) # A2 betyr eksempel 2, se eksempler definert over.
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
