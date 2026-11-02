import numpy as np


def test():
	K1 = np.array([[1.0, 0.0], [0.0, 1.0]])
	N1 = np.array([[1.0, 0.0], [0.0, 1.0]])
	S1 = np.array([[1.0, 0.0], [0.0, 1.0]])
	W1 = np.array([[1.0, 0.0], [0.0, 1.0]])
	Y1 = np.array([[1.0, 0.0], [0.0, 1.0]])
	assert round(main(K1, N1, S1, W1, Y1), 2) == 1.41

	K2 = np.array([[0.89, 0.05], [0.36, 0.8]])
	N2 = np.array([[0.12, 0.64], [0.66, 0.63]])
	S2 = np.array([[0.02, 0.7], [0.34, 0.82]])
	W2 = np.array([[0.86, 0.37], [0.28, 0.89]])
	Y2 = np.array([[0.4, 0.23], [0.72, 0.08]])
	assert round(main(K2, N2, S2, W2, Y2), 2) == 0.64


def main(K, N, S, W, Y):
	result = np.linalg.norm(
    	Y + N + np.linalg.matrix_power((K * W), 8)
		- np.linalg.matrix_power(((S.T * N).T + Y), 2),
    	ord='fro'
	)
	return result

