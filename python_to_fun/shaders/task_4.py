import math
import tkinter as tk


def draw(shader, width, height):
	image = bytearray((0, 0, 0) * width * height)
	for y in range(height):
		for x in range(width):
			pos = (width * y + x) * 3
			color = shader(x / width, y / height)
			normalized = [max(min(int(c * 255), 255), 0) for c in color]
			image[pos:pos + 3] = normalized
	header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
	return header + image


def main(*shaders):
	labels = []
	images = []
	for i in range(len(shaders)):
		labels.append(tk.Label())
		images.append(tk.PhotoImage(data=draw(shaders[i], 256, 256)).zoom(2, 2))
		labels[i].pack(side=tk.LEFT)
		labels[i].config(image=images[i])
	tk.mainloop()

def two_color_shader(x, y):

	calibrate_vector = {'x': 77777.777, 'y': 1313.131313} 
	calibrate_coefficient = 111111.11111


	raw_chaos = (
		math.sin(
		(x * calibrate_vector['x']
		+ y * calibrate_vector['y']))
		* calibrate_coefficient
	)
 
	chaos = raw_chaos - math.floor(raw_chaos)

	return chaos, chaos, chaos

main(two_color_shader)
