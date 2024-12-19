#!/usr/bin/env python3
from bolge import bolge
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as line
from numpy import arange
from math import pi, log, sin, cos

# Lag bilder av flere n bølger ved siden av hverandre.
# Denne filen er nesten duplikat av massesim.py, ble modifisert for å legge g(t) og f(x) ved siden av hverandre raskere. Altså brukt for å fremstille initialbetingelser

def main():
	#x er variabel av rom bortover langs l
	#t er variabel av tid som stiger
	l = 10		# Fast l (lengde) for denne simulasjonen
	c = 1		# Bølgens hastighet for denne simulasjonen
	n_start = 1	# Det under summasjonstegnet. Ofte n=0 eller n=1.
	n_end = 2	# Det over summasjonstegnet. Ofte inf; bruker lavere tall enn inf for simulering

	marker = -1	# Punkt langs x som skal utmerkes

	millis = 10 # Målinger per enhet fra 0 til l. Øker smoothness i grafen
			# Presisjon i sub-enhet av x mot l.

	cols = int((n_end)/2)
	fig, axis = plt.subplots(cols, 2)

	for hnum in range(n_start, n_end+1):

		n_set = hnum

		#Kalibrering
		t_delta = 15	# Antall målinger per periode
		t_period = (2*l)/c

	# Formatering av graf
		if cols > 1:
			ax = axis[int(hnum/cols), hnum%cols]
		else:
			ax = axis[int(hnum%2)]

		if marker != -1 and marker < l and marker > 0:
			ax.legend(handles=[line([0], [0], markerfacecolor='k', marker='o', color='w', label=f"Punkt ( {marker}, u({marker}, {t}) ) er markert")], loc='upper right')
		if hnum%2:
#			ax.set_title(f"Plotting av u_n(x, t) hvor n = {hnum}")
			ax.set_title(f"g(t)")
			ax.set_ylabel("hastighet")
			ax.set_xlabel("t")
			ax.set_ylim(-1.2, 1.2) # Kan justeres for hver enkelt egt.
			ax.set_xlim(0, t_period)
		#	ax.tight_layout()
			x_tick_detail = t_period # amount of ticks from 0 to l
			x_ticks = []
			for val in arange(0, float(t_period), float(t_period)/float(x_tick_detail)):
				x_ticks.append(str(round(val, 2)))
			x_ticks.append('T')
			ax.set_xticks(range(len(x_ticks)), x_ticks)

		else:
			ax.set_title(f"f(x)")
			ax.set_ylabel("u(x, t)")
			ax.set_xlabel("x")
			ax.set_ylim(-1.2, 1.2) # Kan justeres for hver enkelt egt.
			ax.set_xlim(0, l)
		#	ax.tight_layout()
			x_tick_detail = 10 # amount of ticks from 0 to l
			x_ticks = []
			for val in arange(0, l, float(l)/float(x_tick_detail)):
				x_ticks.append(str(round(val, 2)))
			x_ticks.append('l')
			ax.set_xticks(range(len(x_ticks)), x_ticks)
		ax.grid()


		print(f"Gjør {int(t_delta*millis*l*(n_end-n_start+1))} målinger.")

		u_list = []
		x_list = []
		if hnum%2:
			lengde = t_period
		else:
			lengde = l
		lengde += 1/float(millis)
		for x in arange(0, lengde, 1/float(millis)):
			x = round(x, 2)

			if hnum%2:
				u_sum = cos(x)
				# if x < l/2:
				# 	u_sum = x**3/((l/2)**3) # graf rester fra tidligere eksempel
				# else:
				# 	u_sum = -x/(l/2)+2
			else:
				u_sum = sin(x/2)
				# u_sum = 0 # rester her også.

			if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
				marker_u = u_sum

			u_list.append(u_sum)
			x_list.append(x)

			#print(f"{int(x/((l+1)*millis)*100)}%", end="\r")

		if marker != -1 and marker < l and marker > 0:
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
