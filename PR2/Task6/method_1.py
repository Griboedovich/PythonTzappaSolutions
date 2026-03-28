import math


def main(Omega):
	B = {
		math.ceil(w/4) for w in Omega
		if not(-53 <= w < 61)
	}
	P = {abs(w) for w in Omega if (w <= -13 or w >= 55)}
	E = {p**4 + p**3 for p in P if (p > min(B))}
	N = {abs(e) for e in E if (e <= -67 or e >= 29)}
	Y = {b**2 for b in B if (min(E) > b)}
	F = len(Y) + sum({3*u + abs(v) for u in Y for v in N})
	return F

