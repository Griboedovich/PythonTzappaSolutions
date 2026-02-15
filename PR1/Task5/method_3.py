import math


def main(x):

	amount = 0
	i = 0

	while i < len(x):
		amount += (math.floor(60*x[i]**2 - x[i]**3/43))**3
		i += 1

	return 89*amount

