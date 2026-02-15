import math


def main(n):
	if (n == 0):
		return -0.80
	if (n == 1):
		return 0.09	
	if (n >= 2):
		return math.log(main(n-1)**3 + 1 + main(n-2)**2)**2 + 70

