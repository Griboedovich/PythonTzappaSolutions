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


def random_generator(x, y, seed):
	calibrate_vector = {'x': 77.77 * seed, 'y': 13.13 * seed} 
	calibrate_coefficient = 11111 + 13 / seed

	raw_random = (
		math.sin(
		(x * calibrate_vector['x']
		+ y * calibrate_vector['y']) + seed)
		* calibrate_coefficient
	)

	random_value = raw_random - math.floor(raw_random)

	return random_value

def simple_noise_shader(x, y):

	chaos = random_generator(x, y, 1)

	return chaos, chaos, chaos

def coordinate_to_grid(x, y, grid_size):

	new_x = x // grid_size

	new_y = y // grid_size

	return new_x, new_y

def grid_noise_shader(x, y):

	x, y = coordinate_to_grid(x, y, 0.05)

	chaos = random_generator(x, y, 1)

	return chaos, chaos, chaos

main(
	simple_noise_shader,
	grid_noise_shader
)
