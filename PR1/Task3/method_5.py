import math


def n_recursion_summation(n, k):
	if k < n:
		return k + n_recursion_summation(n, k+1)
	else:
		return k


def m_recursion_summation(z, m, j):
	if j < m:
		return ((
			0.02 - (z**3 + z + z**2)**5 - math.log(j)**6)
			+ m_recursion_summation(z, m, j+1))
	else:
		return (0.02 - (z**3 + z + z**2)**5 - math.log(j)**6)


def main(m, z, n):
	return m_recursion_summation(z, m, 1) - n_recursion_summation(n, 1)
	
