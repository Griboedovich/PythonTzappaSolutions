import math


def main(m, z, n):
	m_amount = (
		(0.02 - (z**3 + z + z**2)**5 - math.log(j)**6)
		for j in range(1, m+1)
	)
	n_amount = (k for k in range(1, n+1))
	return sum(m_amount) - sum(n_amount)

