#!/usr/bin/env python3
from bolge import bolge
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as line
from numpy import arange
from sys import argv

def main():
	if not len(argv) == 2:
		print(f"usage: {argv[0]} [k]")
		return
	k = int(argv[1])
	# Simulering av noe bølgelikning
	# Bruker funksjon av tid og posisjon

	t = 0
	#c = 3 # Satt i bølge script
	l = 10		# Fast l (lengde) for denne simulasjonen
#	k = 1
	#x er variabel bortover langs l
	#t er variabel for plotting


	#Kalibrering
	marker = -1	# Punkt langs x som skal utmerkes

	millis = min(4*k, 15)	# Målinger per enhet fra 0 til l. Øker smoothness i grafen
#	millis = 10	# Målinger per enhet fra 0 til l. Øker smoothness i grafen
# Presisjon i sub-enhet av x mot l.

	t_max = 10/k 	# Tror denne burde stå på 5 egt		# Variabel tid lengde for gif, gjør t_max * t_precision gif frames
	t_precision = 3*k # Variabel for tidspresisjon per tidsenhet

	n_start = 0	# Det under summasjonstegnet. Ofte n=1.
	n_end = 50	# Det over summasjonstegnet. Ofte inf, men her bruker vi lavere tall for sim
	# Gir presisjon i hver enkelt måling




	# Formatering av graf
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	if marker != -1 and marker < l and marker > 0:
		ax.legend(handles=[line([0], [0], markerfacecolor='k', marker='o', color='w', label=f"Punkt ( {marker}, u({marker}, {t}) ) er markert")], loc='upper right')
	ax.set_ylabel("uk(x, t)")
	ax.set_xlabel("x")
#	ax.set_ylim(-50, 50) # Kan justeres for hver enkelt egt.
	ax.set_xlim(0, l)
#	ax.tight_layout()
	ax.set_title(f"Plotting av uk(x, t) hvor k = {k}")
	x_tick_detail = 10 # amount of ticks from 0 to l
	x_ticks = []
	for val in arange(0, l, float(l)/float(x_tick_detail)):
		x_ticks.append(str(val))
	x_ticks.append('l')
	ax.set_xticks(range(len(x_ticks)), x_ticks)
	ax.grid()


	print(f"Gjør {int(t_precision*t_max*millis*(n_end-n_start+1))} målinger.")





	u_list = []
	x_list = []

	for x in arange(0, l+1, 1/float(millis)):
		x = round(x, 2)

		a = bolge(l, n_end, k)
		u_sum = a.uk(x, t)

		if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
			marker_u = u_sum
		u_list.append(u_sum)
		x_list.append(x)
		print(f"{int(x/float(l+1)*100)}%", end="\r")

	if marker != -1 and marker < l and marker > 0:
		point = ax.scatter(marker, marker_u, color='k')
	if t == 0:
		ax.plot(x_list, u_list, color='k')
	else:
		ax.plot(x_list, u_list, color='k', linestyle='--', linewidth=0.2)

	print("Ferdig, viser graf")
	try:
		plt.show()
	except KeyboardInterrupt as e:
		print("Quitting!\n")
	return

if __name__ == "__main__":
	main()
