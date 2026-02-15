import math


def main(m, z, n):
	m_amount = 0
	n_amount = 0

	j = 1
	while j <= m:
		m_amount += (0.02 - (z**3 + z + z**2)**5 - math.log(j)**6)
		j += 1

	k = 1
	while k <= n:
		n_amount += k
		k += 1

	return m_amount - n_amount
	
