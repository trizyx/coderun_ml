import numpy as np
import math


def main():
    y = []
    n = int(input())
    for _ in range(n):
        y.append(int(input()))
    const_mse = np.mean(y)
    const_mae = np.median(y)
    y.sort()
    y_cum = np.cumsum([1/x for x in y])
    mid_perc = y_cum[-1]/2
    for i in range(n):
        if y_cum[i]>= mid_perc:
            const_mape = y[i]
            break
    print(const_mse)
    print(const_mae)
    print(const_mape)


if __name__ == '__main__':
    main()
