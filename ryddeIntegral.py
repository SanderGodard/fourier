#!/usr/bin/env python3

# Miniscript for å tydde opp integraler hentet fra wolframalpha
# Ikke inkluder i zip til lars-Nils

def clean(a):
	a=a.replace("L", "l")
	a=a.replace("π", "pi")
	a=a.replace("^", "**")
	a=a.replace(" - ", "-")
	a=a.replace(" + ", "+")
	a=a.replace(" ", "*")
	return a

def main():
	print("Skriv inn tekst kopiert fra alt teksten til bildene på wolframalpha :))")
	inp = input("Tekst kopiert fra wolframalpha: ")
	print(clean(inp))
	return

if __name__ == "__main__":
	main()
