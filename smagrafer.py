#!/usr/bin/env python3
from bolge import bolge
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as line
from numpy import arange
from math import pi, sin

# Simuulere enkeltbølge, kan vise markert punkt.
# Brukt for å lage småbilder av odde og like grafer, og liknende småting.

def main():
	marker = -1	# Punkt langs x som skal utmerkes

	#Kalibrering
	millis = 10 # Målinger per enhet fra 0 til l. Øker smoothness i grafen
			# Presisjon i sub-enhet av x mot l.

	# Formatering av graf
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	if marker != -1 and marker < l and marker > 0:
		ax.legend(handles=[line([0], [0], markerfacecolor='k', marker='o', color='w', label=f"Punkt ( {marker}, u({marker})) er markert")], loc='upper right')
	ax.set_title(f"Generisk graf:")
	ax.set_ylabel("f(x)")#, rotation=0)
	ax.set_xlabel("x")
	# if not n_set == -1:
	# 	ax.set_ylim(-1.2, 1.2) # Kan justeres for hver enkelt egt.
	ax.set_xlim(0, l)
	ax.set_ylim(0, 1.2)
# #	ax.tight_layout()
# 	x_tick_detail = 10 # amount of ticks from 0 to l
# 	x_ticks = []
# 	for val in arange(0, l, float(l)/float(x_tick_detail)):
# 		x_ticks.append(str(val))
# 	x_ticks.append('l')
# 	ax.set_xticks(range(len(x_ticks)), x_ticks)
	ax.grid()

	print(f"Gjør {int(millis*l)} målinger.")

	u_list = []
	x_list = []
	for x in arange(0, l+1, 1/float(millis)):
		x = round(x, 2)
		a = bolge(l, c)

		if x < l/2:
			u_sum = x**3/((l/2)**3) # ENDRING AV FUNKSJONSUTTRYKK SKJER HER
		else:
			u_sum = -x/(l/2)+2

		if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
			marker_u = u_sum

		u_list.append(u_sum)
		x_list.append(x)

		if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
			point = ax.scatter(marker, marker_u, color='k')

	ax.plot(x_list, u_list, color='k')
	

	print("Ferdig, viser graf")
	try:
		plt.show()
	except KeyboardInterrupt as e:
		print("Quitting!\n")
	return

if __name__ == "__main__":
	main()
