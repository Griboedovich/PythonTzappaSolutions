import math


def main(x):
	amount = 0
	for i in range(len(x)):
		amount += (math.floor(60*x[i]**2 - x[i]**3/43))**3
	return 89*amount

