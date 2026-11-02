import numpy as np
import math
import matplotlib.pyplot as plt
from  matplotlib.colors import ListedColormap

class Sprite:


	def __init__(self, value=np.zeros((5, 5)), cmap=['k', 'w']):

		self.value = value
		self.cmap = cmap
		self.ccount = len(cmap)
		self.h = value.shape[0]
		self.w = value.shape[1]
		self.const_val = tuple(tuple(row) for row in self.value)


	def show(self):
		plt.matshow(self.value, cmap=ListedColormap(self.cmap))
		plt.show()


	def get_with_border(self):
		value = np.pad(
			np.copy(self.value),
			pad_width=2,
			mode='constant',
			constant_values=0
		)
		new_sprite = Sprite(value, self.cmap)
		return new_sprite


class SpriteTable:


	def __init__(self, sprite_generator):
		self.sprites = []
		self.cmap = sprite_generator.cmap
		self.spborder = 2
		self.border = 2
		self.sg = sprite_generator

	def add(self, sprite):
		self.sprites.append(sprite)

	def generate_sprites(self):
		pass

	
	def find_sides(self, spcount):
		optimal_h = 0
		optimal_w = 0
		min_diff = spcount + 1
		for i in range(1, int(spcount**0.5) + 1):
			if spcount % i == 0 and (abs(spcount // i - i) < min_diff) :
				min_diff = abs(spcount // i - i)
				optimal_h = i
				optimal_w = spcount // i

			if optimal_h / optimal_w < 0.40:
				optimal_h = math.ceil(spcount**0.5)
				optimal_w = spcount // optimal_h + spcount % optimal_h
		return optimal_h, optimal_w


	def show(self):
		sp_count = len(self.sprites)
		rows, colums = self.find_sides(sp_count)
		sh = self.sg.h
		sw = self.sg.w

		table = np.zeros(((rows*sh + (rows - 1) * self.spborder), (colums*sw + (colums - 1) * self.spborder)))

		for i in range(len(self.sprites)):
			row = i // colums
			colum = i % colums
			bhpad = row * sh + row * self.spborder
			ahpad = (rows - (row + 1)) * sh + (rows - (row + 1)) * self.spborder
			bwpad = colum * sw + colum * self.spborder
			awpad = (colums - (colum + 1)) * sw + ((colums - (colum + 1)) * self.spborder)
			sprite = self.sprites[i]
			value = sprite.value
			value = np.pad(
				value,
				pad_width=((bhpad, ahpad), (bwpad, awpad)),
				mode='constant',
				constant_values=0
			)

			table = table + value


		table = np.pad(
			table,
			pad_width=self.border,
			mode='constant',
			constant_values=0
		)
		plt.matshow(table, cmap=ListedColormap(self.cmap))
		plt.show()

	

class SpriteGenerator:


	def __init__(self, w=5, h=5, cmap=['k', 'w']):
		self.w = w
		self.h = h
		self.cmap = cmap
		self.ccount = len(cmap)
		self.generated_sprite_set = set()

	def get_color_sprite(self):
		return self.paint_sprite(self.get_sprite())

	# переписать этот кал
	def choise_correct_complex_sprites(self):
		variants = []
		ver_neibors = (self.generate_sprite_cen, self.generate_sprite_cyr, self.generate_sprite_ver)
		gor_neibors = (self.generate_sprite_cen, self.generate_sprite_cyr, self.generate_sprite_gor)
		cyr_cen_neibors = (self.generate_sprite_cen, self.generate_sprite_cyr)
		for neibor in ver_neibors:
			variants.append((self.generate_sprite_ver, neibor))
		for neibor in gor_neibors:
			variants.append((self.generate_sprite_gor, neibor))
		for neibor in cyr_cen_neibors:
			variants.append((self.generate_sprite_cen, neibor))
		variants.append((self.generate_sprite_cyr, self.generate_sprite_cyr))
		mode = np.random.randint(0, len(variants) - 1)
		sp1_gen, sp2_gen = variants[mode]
		return (sp1_gen(), sp2_gen())

	def get_complex_color_sprite(self):
		sprite_1, sprite_2 = self.choise_correct_complex_sprites()
		val_sp_1 = sprite_1.value
		val_sp_2 = sprite_2.value
		inv_val_sp_2 = (np.invert(val_sp_2)) + (2 * np.ones((sprite_2.h, sprite_2.w)))
		val_sp_1 = inv_val_sp_2 * val_sp_1

		sprite_1 = self.paint_sprite(Sprite(val_sp_1, self.cmap))
		sprite_2 = self.paint_sprite(Sprite(val_sp_2, self.cmap))
		
		sprite = Sprite(sprite_1.value + sprite_2.value, self.cmap)
		return sprite

	def get_sprite(self):
		mode = np.random.randint(0,3)
		match mode:
			case 0:
				return self.generate_sprite_ver()
			case 1:
				return self.generate_sprite_gor()
			case 2:
				return self.generate_sprite_cen()


	def get_uniq_sprite(self, mode=0):
		if mode == 1 : gen_func = self.get_color_sprite
		elif mode == 2 : gen_func = self.get_complex_color_sprite
		else: self.get_sprite

		attempt = 0
		while attempt < 10:
			sprite = gen_func()
			if (not (sprite.const_val in self.generated_sprite_set)):
				self.generated_sprite_set.add(sprite.const_val)
				return sprite
			attempt += 1
		return Sprite(np.zeros((self.h, self.w)), self.cmap)


	def generate_sprite(self):
		value = np.random.randint(0, self.ccount, (self.h, self.w))
		sprite = Sprite(value, self.cmap)
		return sprite


	def generate_sprite_ver(self):
		w_left_random = self.w // 2 + self.w % 2
		w_pad = self.w - w_left_random

		value_left_random = np.pad(
			np.random.randint(0, 2, (self.h, w_left_random)),
			pad_width=((0, 0), (0, w_pad)),
			mode='constant',
			constant_values=0
		)
		value_right_random = np.flip(np.copy(value_left_random), 1)
		value = value_left_random + value_right_random
		value -= value_left_random * value_right_random	
		
		sprite = Sprite(value, self.cmap)
		return sprite


	def generate_sprite_gor(self):
		h_top_random = self.h // 2 + self.h % 2
		h_pad = self.h - h_top_random

		value_top_random = np.pad(
			np.random.randint(0, 2, (h_top_random, self.w)),
			pad_width=((0, h_pad), (0, 0)),
			mode='constant',
			constant_values=0
		)
		value_bottom_random = np.flip(np.copy(value_top_random), 0)
		value = value_top_random + value_bottom_random
		value -= value_top_random * value_bottom_random	

		sprite = Sprite(value, self.cmap)
		return sprite

	def paint_sprite(self, sprite):
		color_value = sprite.value * np.random.randint(1, self.ccount)
		return Sprite(color_value)


	def generate_sprite_cen(self):
		w_left_random = self.w // 2 + self.w % 2
		h_top_random = self.h // 2 + self.h % 2
		w_pad = self.w - w_left_random
		h_pad = self.h - h_top_random

		value_left_top_random = np.pad(
			np.random.randint(0, 2, (h_top_random, w_left_random)),
			pad_width=((0, h_pad), (0, w_pad)),
			mode='constant',
			constant_values=0
		)

		value_right_top_random = np.flip(np.copy(value_left_top_random), 1)
		value_top_random = value_left_top_random + value_right_top_random
		value_top_random -= value_left_top_random * value_right_top_random	
		value_bottom_random = np.flip(np.copy(value_top_random), 0)
		value = value_top_random + value_bottom_random
		value -= value_top_random * value_bottom_random	

		sprite = Sprite(value, self.cmap)
		return sprite


	def generate_sprite_cyr(self):
		w_left_random = self.w // 2 + self.w % 2
		h_top_random = self.h // 2 + self.h % 2
		w_pad = self.w - w_left_random
		h_pad = self.h - h_top_random

		value_left_top = np.zeros((h_top_random, w_left_random), dtype=int)

		r = np.random.randint(0, min(h_top_random, w_left_random))

		for x in range(w_left_random):
			for y in range(h_top_random):
				if abs(r**2 - ((x - (w_left_random - 1))**2 + (y - (h_top_random - 1))**2)) <= r:
					value_left_top[y][x] = 1

		value_left_top_random = np.pad(
			value_left_top,
			pad_width=((0, h_pad), (0, w_pad)),
			mode='constant',
			constant_values=0
		)
		value_right_top_random = np.flip(np.copy(value_left_top_random), 1)
		value_top_random = value_left_top_random + value_right_top_random
		value_top_random -= value_left_top_random * value_right_top_random	
		value_bottom_random = np.flip(np.copy(value_top_random), 0)
		value = value_top_random + value_bottom_random
		value -= value_top_random * value_bottom_random	

		sprite = Sprite(value, self.cmap)
		return sprite


def main():
	cmap = [
		"#000000",
		"#1D2B53",
		"#7E2553",
		"#008751",
		"#AB5236",
		"#5F574F",
		"#C2C3C7",
		"#FFF1E8",
		"#FF004D",
		"#FFA300",
		"#FFEC27",
		"#00E436",
		"#29ADFF",
		"#83769C",
		"#FF77A8",
		"#FFCCAA",
	]
	sg = SpriteGenerator(5, 5, cmap)
	st = SpriteTable(sg)
	for i in range(120):
		#sprite = sg.get_uniq_sprite(2)
		sprite = sg.get_complex_color_sprite()
		st.add(sprite)
	st.show()

main()
