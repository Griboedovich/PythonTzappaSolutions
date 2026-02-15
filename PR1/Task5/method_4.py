import math


def recursion_calc(x, x_length, i):
	if (i < x_length):
		return (
			(math.floor(60*x[i]**2 - x[i]**3/43))**3
			+ recursion_calc(x, x_length, i+1)
		)
	else:
		return 0


def main(x):
	result = 89 * recursion_calc(x, len(x), 0)
	return result

