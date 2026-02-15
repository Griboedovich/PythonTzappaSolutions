def main(x):
	result_dict = {
		(x < -41): (94*x**3),
		(-41 <= x and x < 10): ((x**2 / 71)**7),
		(x >= 10): (x**2 + x**4 + 16*(4*x + 23*x**3 + 77)**6)
	}

	return result_dict[True]

