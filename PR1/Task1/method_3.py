import math


def main(z, x, y):
	return (math.sqrt(
			math.sin(13*z**2 + z**3/25 + y)**3 / 70
			- 65*(math.atan(x))**5)
			+ 63*(77*z**2 - x - x**3)**3
			- 93*y**4)
	

