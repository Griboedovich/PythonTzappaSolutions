import math
import tkinter as tk

root = tk.Tk()

def draw(shader, width, height, seed):
	image = bytearray((0, 0, 0) * width * height)
	for y in range(height):
		for x in range(width):
			pos = (width * y + x) * 3
			color = shader(x / width, y / height, seed)
			normalized = [max(min(int(c * 255), 255), 0) for c in color]
			image[pos:pos + 3] = normalized
	header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
	return header + image


def main(*shaders):
	labels = []
	images = []
	i = 0
	seed = 1
	label = tk.Label(root)
	image = (tk.PhotoImage(data=draw(shaders[i], 256, 256, seed)).zoom(2, 2))
	label.pack(side=tk.LEFT)

	while True:
		image = (tk.PhotoImage(data=draw(shaders[i], 256, 256, seed)).zoom(2, 2))
		label.config(image=image)
		root.update_idletasks()
		seed += 1
		if seed > 1000:
			seed = 0

def two_color_shader(x, y, seed):

	calibrate_vector = {'x': 77777.777 * seed, 'y': 1313.131313 * seed} 
	calibrate_coefficient = 111111.11111 * seed


	raw_chaos = (
		math.sin(
		(x * calibrate_vector['x']
		+ y * calibrate_vector['y'])
		+ seed)
		* calibrate_coefficient
	)
 
	chaos = raw_chaos - math.floor(raw_chaos)

	return chaos, chaos, chaos

main(two_color_shader)
