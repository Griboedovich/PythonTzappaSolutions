import math


def main(m, z, n):
	m_amount = sum([
		(0.02 - (z**3 + z + z**2)**5 - math.log(j)**6)
		for j in range(1, m+1)
	])
	n_amount = sum([k for k in range(1, n+1)])
	return m_amount - n_amount

