# make 1000 combination from randomly pick up 3 out of 500

import numpy as np

input_lpi = np.loadtxt("lpi_more_b3t3.txt")

np.random.seed(8)
randnum1 = np.random.random_integers(0, 499, 50000)
np.random.seed(9)
randnum2 = np.random.random_integers(0, 499, 50000)
np.random.seed(10)
randnum3 = np.random.random_integers(0, 499, 50000)
final = np.zeros((50000, 2))

for i in range(50000):
    a = input_lpi[randnum1[i], :]
    b = input_lpi[randnum2[i], :]
    c = input_lpi[randnum3[i], :]
    output = (a + b + c) / 3
    final[i, :] = output

np.savetxt(r"lpi_50000_distribution_b3t3.txt", final, delimiter=',', fmt='%8.4f')
