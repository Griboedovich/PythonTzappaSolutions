import math


def main(z, x, y):
	intermediate_calc = math.sin(13*z**2 + z**3/25 + y)**3 / 70
	intermediate_calc -= 65*(math.atan(x))**5
	intermediate_calc = math.sqrt(intermediate_calc)
	intermediate_calc += 63*(77*z**2 - x - x**3)**3
	intermediate_calc -= 93*y**4
	return intermediate_calc

