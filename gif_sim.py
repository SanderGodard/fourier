#!/usr/bin/env python3
from bolge import bolge
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as line
from numpy import arange
from glob import glob
from PIL import Image
from sys import argv
from tempfile import TemporaryDirectory

# Simuler enkeltbølger over T tid. Med/uten skygge
# Husk at for å endre hvilke initialbetingelser man simulerer for, så må man endre dette i bolge.py filen!

def make_gif(tmp, gifname): # https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/
	l = [image for image in glob(f"{tmp}/frame_*.png")]
	l2 = [image for image in glob(f"{tmp}/frame_*.png")]
	# Sort
	s = l[0].index("frame_")
	f = sorted(l, key=lambda e: float(e[s+6:-4]))
	f2 = sorted(l2, key=lambda e: float(e[s+6:-4]), reverse=True)
	# Make image elements
	frames = [Image.open(fr) for fr in f]
	frames2 = [Image.open(fr) for fr in f2]
	# Remove duplicates for loop
	frames2.pop(0)
	frames2.pop(-1)
	frames = frames + frames2
	# Append rest to first frame
	frame_one = frames[0]
	frame_one.save(f"{gifname}", format="GIF", append_images=frames, save_all=True, duration=100, loop=0)
	return


def main():
#	lage args for n styring??

	#x er variabel av rom bortover langs l
	#t er variabel av tid som stiger
	l = 10		# Fast l (lengde) for denne simulasjonen
	c = 1		# Bølgens hastighet for denne simulasjonen
	n_set = -1	# Når ikke -1, så overskriver denne summasjonen av bølgene fra n_start til n_end
	n_start = 1	# Det under summasjonstegnet. Ofte n=1.
	n_end = 20	# Det over summasjonstegnet. Ofte inf; bruker lavere tall enn inf for simulering

	marker = -1	# Punkt langs x som skal utmerkes

	show_evil_twin = 0
	filnavn = "eks.gif"


	#Kalibrering
	if not n_set == -1:
		t_delta = float(10*max(1, n_set))	# Antall målinger per periode
		t_period = 1/2 * (10*2)/(c*max(1, n_set))	# Periode i tid
		print(f"{t_delta=}, {t_period=}")
	else:
		t_delta = float(10*n_end)
		t_period = 1/2 * (10*2)/(c)

	millis = 10 # Målinger per enhet fra 0 til l. Øker smoothness i grafen
			# Presisjon i sub-enhet av x mot l.


	# Formatering av graf
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	if marker != -1 and marker < l and marker > 0:
		ax.legend(handles=[line([0], [0], markerfacecolor='k', marker='o', color='w', label=f"Punkt ( {marker}, u({marker}, t) ) er markert")], loc='upper right')
	ax.set_ylabel("u(x, t)")
	ax.set_xlabel("x")
	ax.set_xlim(0, l)
	# ax.set_ylim(-1.2, 1.2)
#	ax.tight_layout()
	x_tick_detail = 10 # amount of ticks from 0 to l
	x_ticks = []
	for val in arange(0, l, float(l)/float(x_tick_detail)):
		x_ticks.append(str(val))
	x_ticks.append('l')
	ax.set_xticks(range(len(x_ticks)), x_ticks)
	ax.grid()



	print(f"Gjør {int(t_delta*millis*l*(n_end-n_start+1))} målinger.")

	temp_dir = TemporaryDirectory()

	for t in arange(0, t_period+t_period/(t_delta), t_period/(t_delta)):
		if n_set != -1:
			ax.set_title(f"Plotting av u_n(x, t), n = {n_set}, t = {round(t, 2)}s")
		else:
			ax.set_title(f"Plotting av u(x, t), t = {round(t, 2)}s")
		u_list = []
		u2_list = []
		x_list = []
		for x in arange(0, l+1, 1/float(millis)):
			x = round(x, 2)

			a = bolge(l, c)
			u_sum = a.u(x, t, n_end, n_start)*n_end # Sum fra n_start til n_end
			if show_evil_twin:
				u2_sum = a.u(x, t_period-t, n_end, n_start)*n_end # Sum fra n_start til n_end

			if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
				marker_u = u_sum
			u_list.append(u_sum)
			if show_evil_twin:
				u2_list.append(u2_sum)
			x_list.append(x)

		# print("LISTE:", u2_list[1])
		if marker != -1 and marker < l and marker > 0:
			point = ax.scatter(marker, marker_u, color='k')
		lines = ax.plot(x_list, u_list, color='k')
		if show_evil_twin:
			lines2 = ax.plot(x_list, u2_list, color='k',  linestyle='--', linewidth=0.7)

		plt.savefig(f"{temp_dir.name}/frame_{t}.png")

		if marker != -1 and marker < l and marker > 0:
			point.remove()
		lines.pop(0).remove() # Fjerner graf igjen
		if show_evil_twin:
			lines2.pop(0).remove()

	print("Lager gif")
	if filnavn == "":
		if n_set != -1:
			make_gif(temp_dir.name, f"waves_n_{n_set}.gif")
		else:
			make_gif(temp_dir.name, f"waves_sum_all_{n_end}.gif")
	else:
		make_gif(temp_dir.name, filnavn)

	print("Ferdig")
	temp_dir.cleanup()

if __name__ == "__main__":
	main()
