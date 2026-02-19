import math


def main(n):
    first = -0.8  # n = 0
    second = 0.09  # n = 1
    for i in range(n - 1):
        second, first = (math.log(second**3 + 1 + first**2)**2 + 70), second
    return second

