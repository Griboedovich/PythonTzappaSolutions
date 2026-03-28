import math
import tkinter as tk
from tkinter import ttk

def draw(shader, width, height, seed, point_count, point_step, amplitude, offset, interpolation_mode):
	image = bytearray((0, 0, 0) * width * height)
	for y in range(height):
		for x in range(width):
			pos = (width * y + x) * 3
			color = shader(x / width, y / height, seed, point_count, point_step, amplitude, offset, interpolation_mode)
			normalized = [max(min(int(c * 255), 255), 0) for c in color]
			image[pos:pos + 3] = normalized
	header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
	return header + image


def main(*shaders):
	shader = shaders[1]

	root = tk.Tk()

	noise_preferense_frame = ttk.Frame()
	noise_frame = ttk.Frame()

	noise_preferense_frame.pack(fill=tk.X)
	noise_frame.pack()
	
	label = tk.Label(noise_frame)
	label.pack(side=tk.LEFT)

	seed_var = tk.IntVar(value = 30)

	point_count_var = tk.IntVar( value = 30 )

	point_step_var = tk.DoubleVar(value = 0.05)

	offset_var = tk.DoubleVar(value = 0)

	amplitude_var = tk.DoubleVar(value = 1)

	checkbutton_var = tk.IntVar(value = 1)

	interpolite_checkbutton = ttk.Checkbutton(
		variable=checkbutton_var,
		command=lambda : update_shader(
			root,
			label,
			shader,
			seed_var,
			point_count_var,
			point_step_var,
			amplitude_var,
			offset_var,
			checkbutton_var
		)
	)

	point_step_scale = ttk.Scale(
		noise_preferense_frame,
		orient=tk.HORIZONTAL,
		from_ = 1/256,
		to = 1,
		command=lambda _: update_shader(
			root,
			label,
			shader,
			seed_var,
			point_count_var,
			point_step_var,
			amplitude_var,
			offset_var,
			checkbutton_var
		),
		variable = point_step_var
	)

	point_count_scale = ttk.Scale(
		noise_preferense_frame,
		orient=tk.HORIZONTAL,
		from_ = 1,
		to = 256,
		command=lambda _: update_shader(
			root,
			label,
			shader,
			seed_var,
			point_count_var,
			point_step_var,
			amplitude_var,
			offset_var,
			checkbutton_var
		),
		variable = point_count_var
	)

	seed_scale = ttk.Scale(
		noise_preferense_frame,
		orient=tk.HORIZONTAL,
		from_ = 1,
		to = 256,
		command=lambda _: update_shader(
			root,
			label,
			shader,
			seed_var,
			point_count_var,
			point_step_var,
			amplitude_var,
			offset_var,
			checkbutton_var
		),
		variable = seed_var
	)

	amplitude_scale = ttk.Scale(
		noise_preferense_frame,
		orient=tk.HORIZONTAL,
		from_ = 0,
		to = 10,
		command=lambda _: update_shader(
			root,
			label,
			shader,
			seed_var,
			point_count_var,
			point_step_var,
			amplitude_var,
			offset_var,
			checkbutton_var
		),
		variable = amplitude_var
	)

	offset_scale = ttk.Scale(
		noise_preferense_frame,
		orient=tk.HORIZONTAL,
		from_ = 0,
		to = 1,
		command=lambda _: update_shader(
			root,
			label,
			shader,
			seed_var,
			point_count_var,
			point_step_var,
			amplitude_var,
			offset_var,
			checkbutton_var
		),
		variable = offset_var
	)

	interpolite_checkbutton.pack(fill=tk.X)

	seed_scale.pack(fill=tk.X)

	point_count_scale.pack(fill=tk.X)

	point_step_scale.pack(fill=tk.X)

	amplitude_scale.pack(fill=tk.X)

	offset_scale.pack(fill=tk.X)

	image = tk.PhotoImage(data=draw(shader, 256, 256, seed_var.get(), point_count_var.get(), point_step_var.get(), amplitude_var.get(), offset_var.get(), checkbutton_var.get())).zoom(2, 2)
	label.config(image=image)


	root.mainloop()

def update_shader(
	root,
	label,
	shader,
	seed_var,
	point_count_var,
	point_step_var,
	amplitude_var,
	offset_var,
	checkbutton_var
):
	seed = seed_var.get()
	point_count = point_count_var.get()
	point_step = point_step_var.get()
	amplitude = amplitude_var.get()
	offset = offset_var.get()
	interpolation_mode = checkbutton_var.get()
	image = tk.PhotoImage(data=draw(shader, 256, 256, seed, point_count, point_step, amplitude, offset, interpolation_mode)).zoom(2, 2)
	label.config(image=image)
	label.image = image

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

def one_dim_simple_noise_shader(x, y):

	chaos = random_generator(x, x, 1)

	return chaos, chaos, chaos
'''
def one_dim_lerp_trivial (coord, c0, c1, v0, v1):

	k = (v1 - v0) / (c1 - c0)

	value = v0 + k * ( coord - c0)

	return value
'''


def one_dim_lerp (coord, c0, c1, v0, v1, interpolation_mode):

	if interpolation_mode == 0:
		t = (coord - c0)/(c1 - c0)
	elif interpolation_mode == 1:
		t = (1 - math.cos(((coord - c0)/(c1 - c0)) * math.pi)) * 0.5
	value = v0 * (1 - t) + v1 * t

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

def one_dim_value_noise_shader(x, y, seed, points_count = 30, point_step = 0.05, amplitude = 1, offset = 0, interpolation_mode = 1):
	# Период функции
	#points_count = 30
	# Растояние между якорными точками интерполяции (f < 1)
	#point_step = 0.05 #frequency??? frequency*x
	# Амплитуда шума (сила) (0, ...)
	#amplitude = 1
	# Смещение x (offset < 1)
	#offset = 0.01

	x = x - math.floor(x)
	x += offset
	x = x - math.floor(x) 

	c0, c1, v0, v1 = get_point_neighbors (x, points_count, point_step, seed)

	chaos = one_dim_lerp(x, c0, c1, v0, v1, interpolation_mode)
	chaos *= amplitude

	return chaos, chaos, chaos

main(
	one_dim_simple_noise_shader,
	one_dim_value_noise_shader
)
