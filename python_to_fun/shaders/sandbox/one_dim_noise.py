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

def one_dim_simple_noise_shader(x, y):

	chaos = random_generator(x, x, 1)

	return chaos, chaos, chaos

def one_dim_noise_shader(x, y):

	x, _ = coordinate_to_grid(x, y, 0.05)

	chaos = random_generator(x, x, 1)

	return chaos, chaos, chaos

'''
def one_dim_generate_values(size):

	# 0 < size < 1

	values_list = []

	for i in range(int(1 // size) + 2):

		x = i * size

		values_list.append(
			random_generator(x, x, 2)
		)

	return values_list

def one_dim_lerp (coord, values, size):

	coord_index = int(coord // size)

	c0 = coord_index * size
	c1 = (coord_index + 1) * size

	v0 = values[coord_index]
	v1 = values[coord_index + 1]

	k = (v1 - v0) / (c1 - c0)

	value = v0 + k * ( coord - c0)

	return value

chaos_values = []
# Неккоректный шейдер в виду того, что необходимо использовать
# Глобальные значения, а инициализация и передача в параметр
# Массива значений затруднительна в виду моей оргазниции
# Визуалиции нескольких окон
def one_dim_value_noise_shader(x, y):
	global chaos_values

	size = 0.13

	if len(chaos_values) == 0:
		chaos_values = one_dim_generate_values(size)

	chaos = one_dim_lerp(x, chaos_values, size)

	return chaos, chaos, chaos
'''
def one_dim_lerp (coord, size):

	c0 = coord // size * size
	c1 = (coord // size + 1) * size

	v0 = random_generator(c0, c0, 2)
	v1 = random_generator(c1, c1, 2)

	k = (v1 - v0) / (c1 - c0)

	value = v0 + k * ( coord - c0)

	return value

def one_dim_value_noise_shader(x, y):

	size = 0.05

	chaos = one_dim_lerp(x, size)

	return chaos, chaos, chaos

main(
	one_dim_simple_noise_shader,
 	one_dim_noise_shader,
	one_dim_value_noise_shader
)
