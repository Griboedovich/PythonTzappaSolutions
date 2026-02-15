def main(x):
	return ((94*x**3) if (x < -41)
			else (
			((x**2 / 71)**7) if (-41 <= x and x < 10)
			else (x**2 + x**4 + 16*(4*x + 23*x**3 + 77)**6)
			))

