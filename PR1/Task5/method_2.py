import math


def main(x):
	amount = sum([((math.floor(60*x[i]**2 - x[i]**3/43))**3) for i in range(len(x))])
	return 89*amount

