import math


def main(n):
	f_res = [-0.8, 0.09]
	for i in range(n - 1):
		f_res.append(math.log(f_res[i+1]**3 + 1 + f_res[i]**2)**2 + 70)
	return f_res[-1]

