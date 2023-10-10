#!/usr/bin/env python3
from bolge import bolge
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as line
from numpy import arange
from math import pi


# Script som viser alle småbølgene under resultatbølgen,
# altså den viser i tillegg alle de stående bølgene som summeres til resultatet


def main():
	#x er variabel av rom bortover langs l
	t = 0 #t er variabel av tid som stiger
	l = 10		# Fast l (lengde) for denne simulasjonen
	c = 1		# Bølgens hastighet for denne simulasjonen
	n_start = 0	# Det under summasjonstegnet. Ofte n=0 eller n=1.
	n_end = 5	# Det over summasjonstegnet. Ofte inf; bruker lavere tall enn inf for simulering

	marker = -1	# Punkt langs x som skal utmerkes


	#Kalibrering
	millis = 10 # Målinger per enhet fra 0 til l. Øker smoothness i grafen
			# Presisjon i sub-enhet av x mot l.


	# Formatering av graf
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	if marker != -1 and marker < l and marker > 0:
		ax.legend(handles=[line([0], [0], markerfacecolor='k', marker='o', color='w', label=f"Punkt ( {marker}, u({marker}, {t}) ) er markert")], loc='upper right')
	ax.set_title(f"Plotting av u(x, t), med visning av stående bølger bak")
	ax.set_ylabel("u(x, t)")
	ax.set_xlabel("x")
#	ax.set_ylim(-2, 2) # Kan justeres for hver enkelt egt.
	ax.set_xlim(0, l)
#	ax.tight_layout()
	x_tick_detail = 10 # amount of ticks from 0 to l
	x_ticks = []
	for val in arange(0, l, float(l)/float(x_tick_detail)):
		x_ticks.append(str(val))
	x_ticks.append('l')
	ax.set_xticks(range(len(x_ticks)), x_ticks)
	ax.grid()


	print(f"Gjør {int(millis*l*(n_end-n_start+1))} målinger.")
	a = bolge(l, c)

	big_u_list = []
	for run in range(n_start, n_end+1):
		u_list = []
		x_list = []
		big_u_list.append([])
		for x in arange(0, l+1, 1/float(millis)):
			x = round(x, 2)

			u_sum = a.un(x, t, run)
			big_u_list[run-n_start].append(u_sum)

			if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
				marker_u = u_sum

			u_list.append(u_sum)
			x_list.append(x)

			print(f"{int(x/((l+1)*millis)*100)}%", end="\r")

		if marker != -1 and marker < l and marker > 0:
			point = ax.scatter(marker, marker_u, color='k')

		lin = ax.plot(x_list, u_list, linestyle='--', linewidth=0.7)

	# Så ta into account den sammenlagte bølgen.
	sum_u_list = [0 for n in range((l+1)*millis)]
	for run in big_u_list:
		for i, val in enumerate(run):
			sum_u_list[i] += val
	ax.plot(x_list, sum_u_list, color='k')


	if marker != -1 and marker < l and marker > 0:
		point = ax.scatter(marker, marker_u, color='k')

	print("Ferdig, viser graf")
	try:
		plt.show()
	except KeyboardInterrupt as e:
		print("Quitting!\n")
	return

if __name__ == "__main__":
	main()
