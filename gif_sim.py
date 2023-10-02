#!/usr/bin/env python3
from bolge import bolge
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as line
from numpy import arange
from glob import glob
from PIL import Image
from sys import argv
from tempfile import TemporaryDirectory

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
	if not len(argv) == 2:
		print(f"usage: {argv[0]} [k]")
		return
	k = int(argv[1])

	# Simulering av noe bølgelikning
	# Bruker funksjon av tid og posisjon
	# D'Alemberts likninger tror jeg?

	l = 10		# Fast l (lengde) for denne simulasjonen
	# t = 0		# Fast t (tid) for denne simulasjonen
	#x er variabel

	#Kalibrering
	marker = l/2	# Punkt langs x som skal utmerkes

	millis = 10	# Målinger per enhet fra 0 til l. Øker smoothness i grafen
# Presisjon i sub-enhet av x mot l.

	t_max = 10/k # Variabel tid lengde for gif, gjør t_max * t_precision gif frames
	t_precision = 3*k # Variabel for tidspresisjon per tidsenhet

	n_start = 1	# Det under summasjonstegnet. Ofte n=1.
	n_end = 50	# Det over summasjonstegnet. Ofte inf, men her bruker vi lavere tall for sim
	# Gir presisjon i hver enkelt måling




	# Formatering av graf
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	if marker != -1 and marker < l and marker > 0:
		ax.legend(handles=[line([0], [0], markerfacecolor='k', marker='o', color='w', label=f"Punkt ( {marker}, u({marker}, t) ) er markert")], loc='upper right')
	ax.set_ylabel("u_k(x, t)")
	ax.set_xlabel("x")
	ax.set_ylim(-50, 50) # Kan justeres for hver enkelt egt.
	ax.set_xlim(0, l)
#	ax.tight_layout()
	ax.set_title(f"Simulasjon av u_k(x, t) hvor k = {k}")
	x_tick_detail = 10 # amount of ticks from 0 to l
	x_ticks = []
	for val in arange(0, l, float(l)/float(x_tick_detail)):
		x_ticks.append(str(val))
	x_ticks.append('l')
	ax.set_xticks(range(len(x_ticks)), x_ticks)
	ax.grid()


	print(f"Gjør {t_precision*t_max*millis*(n_end-n_start+1)} målinger.")

	temp_dir = TemporaryDirectory()

	for t in arange(0, t_max, round(1/float(t_precision+1), 2)):
		u_list = []
		u2_list = []
		x_list = []
		freq = []
	#	print(float(millis)/float(l))
		for x in arange(0, l+1, 1/float(millis)):
	#		print(x)
			x = round(x, 2)
			u_sum = 0
			u2_sum = 0
			for n in range(n_end-n_start+1):
				a = bolge(t, x, l, n+n_start)
				#print(a)
				u_sum += a.uk(x, t, k)
				u2_sum += a.uk(x, t_max-t, k)
	#		print(float(marker), x)
			if float(marker) == float(x) and marker != -1 and marker <= l and marker >= 0:
				marker_u = u_sum
			u_list.append(u_sum)
			u2_list.append(u2_sum)
			x_list.append(x)
			print(f"{int(t/t_max*100)}%", end="\r")

		if marker != -1 and marker < l and marker > 0:
			point = ax.scatter(marker, marker_u, color='k')
		lines = ax.plot(x_list, u_list, color='k')
		lines2 = ax.plot(x_list, u2_list, color='k', linestyle='--', linewidth=0.5)

		plt.savefig(f"{temp_dir.name}/frame_{t}.png")

		if marker != -1 and marker < l and marker > 0:
			point.remove()
		lines.pop(0).remove() # Fjerner graf igjen
		lines2.pop(0).remove() # Fjerner graf igjen

	print("Lager gif")
	make_gif(temp_dir.name, f"waves_k{k}.gif")
	print("Ferdig")
	temp_dir.cleanup()

if __name__ == "__main__":
	main()
