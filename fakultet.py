#!/usr/bin/env python3

def fac(n):
	return fakultet(n)

def fakultet(n):
	if (n < 2):
		return 1
	return n*fakultet(n-1)

def main():
	n = int(input("n: "))
	res = fakultet(n)

	print("Resultat:", res)
	return

if __name__ == "__main__":
	main()
