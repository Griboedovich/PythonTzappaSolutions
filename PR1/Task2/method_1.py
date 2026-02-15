def main(x):
	if (x < -41):
		return 94*x**3
	elif (-41 <= x and x < 10):
		return (x**2 / 71)**7
	else:
		return x**2 + x**4 + 16*(4*x + 23*x**3 + 77)**6

