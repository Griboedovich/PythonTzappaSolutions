import math


def main(n):
	return (
		(-0.80) if (n == 0) else(
			(0.09) if (n == 1) else(
				math.log(main(n-1)**3 + 1 + main(n-2)**2)**2 + 70))
	)

