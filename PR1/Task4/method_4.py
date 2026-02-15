import math


def main(n):
	match n:
		case 0:
			return -0.80
		case 1:
			return 0.09
		case x if x >= 2:
			return math.log(main(n-1)**3 + 1 + main(n-2)**2)**2 + 70

