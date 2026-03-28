import math
import tkinter as tk
from tkinter import ttk

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


def main(shader):
	root = tk.Tk()

	noise_preferense_frame = ttk.Frame()
	noise_frame = ttk.Frame()

	noise_preferense_frame.pack(fill=tk.X)
	noise_frame.pack()
	
	label = tk.Label(noise_frame)
	image = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)

	label.pack(side=tk.LEFT)
	label.config(image=image)

	root.mainloop()

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

def one_dim_lerp (coord, c0, c1, v0, v1):

	k = (v1 - v0) / (c1 - c0)

	value = v0 + k * ( coord - c0)

	return value

def get_point_neighbors(coord, points_count, point_step, seed = 1):

	index_num0 = coord // point_step

	index_num1 = index_num0 + 1

	coord0 = index_num0 * point_step
	coord1 = index_num1 * point_step
	#v0 = random_generator(c0, c0, 2)
	#v1 = random_generator(c1, c1, 2)

	point0 = index_num0 % points_count + 11
	point1 = index_num1 % points_count + 11

	value0 = random_generator(point0, point0, seed)
	value1 = random_generator(point1, point1, seed)

	return coord0, coord1, value0, value1

def one_dim_value_noise_shader(x, y):
	# Период функции
	points_count = 30
	# Растояние между якорными точками интерполяции (f < 1)
	point_step = 0.05 #frequency??? frequency*x
	# Амплитуда шума (сила) (0, ...)
	amplitude = 1
	# Смещение x (offset < 1)
	offset = 0.01

	x = x + offset - math.floor(x + offset) 

	c0, c1, v0, v1 = get_point_neighbors (x, points_count, point_step)

	chaos = one_dim_lerp(x, c0, c1, v0, v1)
	chaos *= amplitude

	return chaos, chaos, chaos

main(
	one_dim_value_noise_shader
)
