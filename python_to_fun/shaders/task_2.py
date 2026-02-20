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
	label2 = tk.Label()
	img2 = tk.PhotoImage(data=draw(shaders[1], 256, 256)).zoom(2, 2)
	label2.pack(side=tk.LEFT)
	label2.config(image=img2)
	tk.mainloop()

def two_color_shader(x, y):
	rc_x_center = 0.525
	rc_y_center = 0.525
	rc_radius = 0.4
	red_circle = (
		1
		-((x-rc_x_center)**2 + (y-rc_y_center)**2)	
		/ rc_radius**2			 
	)

	gc_x_center = 0.475
	gc_y_center = 0.475
	gc_radius = 0.4
	green_circle = (
		1
		- ((x-gc_x_center)**2 + (y-gc_y_center)**2)	
		/ gc_radius**2			 
	)

	return red_circle, green_circle, 0

def three_color_shader(x, y):
	# Координата x - вправо || y - вниз
	
	# КРАСНЫЙ КРУГ

	# Центр круга по оси x
	rc_x_center = 0.525
	# Центр круга по оси y
	rc_y_center = 0.525
	# Радиус круга
	rc_radius = 0.4
	# Формула описывает форму круга
	# Описание мат. действие см. синий круг.
	'''
	Когда мы делим (x-rc_x_center)**2 + (y-rc_y_center)**2)
	На rc_radius**2 то получаем распределение точек
	В котором точки лежащие внутри окружности заданного радиуса
	Будут иметь значение меньше 1, точке же снаружи будут иметь
	Значение больше одного и как следствие - более насыщенный
	Цвет. Получается что весь цвет остаёться снаружи круга,
	Нам нужен же противоположный результат. Поэтому инвертируем
	зоны распреджеления цвета через 1-(зона), таким образом 
	внутри круга значения точек будут положительны и больше нуля
	а снаружи меньше нуля, что означает наличие цвета внутри круга
	и пустоста снаружи. Градиент же получается в виду отличных от 1 
	значений. 1 - красный, 0.5 - тёмно красный, 0 - чёрный. 
	(т.е. значение отвечает за яркость конкретного цвета)
	'''
	red_circle = (
		1
		-((x-rc_x_center)**2 + (y-rc_y_center)**2)	
		/ rc_radius**2			 
	)

	# ЗЕЛЁНЫЙ КРУГ

	gc_x_center = 0.475
	gc_y_center = 0.475
	gc_radius = 0.4
	green_circle = (
		1
		- ((x-gc_x_center)**2 + (y-gc_y_center)**2)	
		/ gc_radius**2			 
	)

	# СИНИЙ КРУГ

	# Нужен для добавления белого цвета в центр окружности
	# Это придаёт эффект матовости

	bc_x_center = 0.5
	bc_y_center = 0.5
	bc_radius = 0.35
	blue_circle = (
		(1
		- ((x-bc_x_center)**2 + (y-bc_y_center)**2)	
		/ bc_radius**2)
		* 0.2
	)
	'''
		(
		(1					# инвертирование цвета в окружности
		- ((x-bc_x_center)**2 + (y-bc_y_center)**2)	
		/ bc_radius**2)		# Формула задаёт распределение цветов
							# В форме окружности
		* 0.2	 			# Задаёт яркость синего круга внутры зоны.
							# С точки зрения наложения цветов
							# Означает прозрачность
		)
	'''

	return  red_circle, green_circle, blue_circle

main(two_color_shader, three_color_shader)
