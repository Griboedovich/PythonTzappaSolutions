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
	label = tk.Label()
	img = tk.PhotoImage(data=draw(shaders[0], 256, 256)).zoom(2, 2)
	label.pack(side=tk.LEFT)
	label.config(image=img)
	tk.mainloop()

def shader(x, y):
	pacman = 0	

	body_center = (0.5, 0.5)
	body_radius = 0.35
	body = (
		((x-body_center[0])**2 + (y-body_center[1])**2)	
		< body_radius**2			 
	)

	eye_center = (0.6, 0.28)
	eye_radius = 0.06
	eye = (
		((x-eye_center[0])**2 + (y-eye_center[1])**2)	
		< eye_radius**2			 
	)

	mouth_position = (0.5, 0.5)

	# y = kx + b
	# (y - y0) = k(x - x0) + b
	# y = kx + (b + y0 - kx0)
	# Мне было лень выводить из общей формулы, поэтому
	# Коэффициентов b будет 2: для нижний и верхней зоны

	# Не забываем, что ордината смотрит в другую сторону

	k_30_deg = (math.sqrt(3)/3)
	b_up = mouth_position[1] - (-1 *  k_30_deg) * mouth_position[0]
	b_down = mouth_position[1] - k_30_deg * mouth_position[0]

	# У зон рта отличаются знаки в неравенстве области под прямой!
	mouth_up = ((-k_30_deg * x + b_up < y) and x >= mouth_position[0])
	mouth_down= ((k_30_deg * x + b_down > y) and x >= mouth_position[0])
	
	mouth = mouth_up and mouth_down

	# Через логическую функцию вырезаем рот и глаз
	# Из туловища

	pacman = body and not(eye) and not(mouth)
	return pacman, pacman, 0

main(shader)
