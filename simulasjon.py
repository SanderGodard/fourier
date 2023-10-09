#!/usr/bin/env python3
from bolge import bolge
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as line
from numpy import arange
from math import pi

def main():
#	lage args for n styring??

	#x er variabel av rom bortover langs l
	#t er variabel av tid som stiger
	l = 10		# Fast l (lengde) for denne simulasjonen
	c = 1		# Bølgens hastighet for denne simulasjonen
	n_set = -1	# Når ikke -1, så overskriver denne summasjonen av bølgene fra n_start til n_end
	n_start = 1	# Det under summasjonstegnet. Ofte n=0 eller n=1.
	n_end = 100000	# Det over summasjonstegnet. Ofte inf; bruker lavere tall enn inf for simulering

	marker = -1	# Punkt langs x som skal utmerkes

	stipla_toggle = 0 # Toggle stipla linjer av eller på.


	#Kalibrering
	if not n_set == -1:
		t_delta = 10*n_set	# Antall målinger per periode
		t_period = 1/2 * (10*2)/(c*n_set)	# Periode i tid
	else:
		t_delta = 10*n_end
		t_period = 1/2 * (10*2)/(c*n_end)

	millis = 10 # Målinger per enhet fra 0 til l. Øker smoothness i grafen
			# Presisjon i sub-enhet av x mot l.



	# Formatering av graf
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	if marker != -1 and marker < l and marker > 0:
		ax.legend(handles=[line([0], [0], markerfacecolor='k', marker='o', color='w', label=f"Punkt ( {marker}, u({marker}, {t}) ) er markert")], loc='upper right')
	if n_set != -1:
		ax.set_title(f"Plotting av u_n(x, t) hvor n = {n_set}")
	else:
		ax.set_title(f"Plotting av u(x, t)")
	ax.set_ylabel("u(x, t)")
	ax.set_xlabel("x")
	if not n_set == -1:
		ax.set_ylim(-1.2, 1.2) # Kan justeres for hver enkelt egt.
	ax.set_xlim(0, l)
#	ax.tight_layout()
	x_tick_detail = 10 # amount of ticks from 0 to l
	x_ticks = []
	for val in arange(0, l, float(l)/float(x_tick_detail)):
		x_ticks.append(str(val))
	x_ticks.append('l')
	ax.set_xticks(range(len(x_ticks)), x_ticks)
	ax.grid()

	print(f"Gjør {int(t_delta**(stipla_toggle)*millis*(n_end-n_start+1))} målinger.")

	for t in arange(0, t_period+t_period/(t_delta), t_period/(t_delta)):
		u_list = []
		x_list = []
		for x in arange(0, l+1, 1/float(millis)):
			x = round(x, 2)

			a = bolge(l, c)
			if n_set != -1:
				u_sum = a.un(x, t, n_set)
			else:
				u_sum = a.u(x, t, n_end, n_start) # Sum fra n_start til n_end

			if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
				marker_u = u_sum

			u_list.append(u_sum)
			x_list.append(x)

			#print(f"{int(x/((l+1)*millis)*100)}%", end="\r")

		if marker != -1 and marker < l and marker > 0:
			point = ax.scatter(marker, marker_u, color='k')

		if t == 0:
			ax.plot(x_list, u_list, color='k')
		else:
			ax.plot(x_list, u_list, color='k', linestyle='--', linewidth=0.2)
		
		if not stipla_toggle:
			break

	print("Ferdig, viser graf")
	try:
		plt.show()
	except KeyboardInterrupt as e:
		print("Quitting!\n")
	return

if __name__ == "__main__":
	main()
