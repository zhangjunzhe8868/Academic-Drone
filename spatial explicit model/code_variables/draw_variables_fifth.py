# make 1000 combination from randomly pick up 6 out of 1000

import numpy as np
from scipy import stats

input_lpi = np.loadtxt("more_variables_b3t3.txt", delimiter=",")
final = np.zeros((50000, 4)) #50000 times for comparsion

for i in range(50000): #50000 times for comparsion
    randnum = np.random.random_integers(0, 999, size=6)
    a = input_lpi[randnum[0], :]
    b = input_lpi[randnum[1], :]
    c = input_lpi[randnum[2], :]
    d = input_lpi[randnum[3], :]
    e = input_lpi[randnum[4], :]
    f = input_lpi[randnum[5], :]
    output = (a + b + c + d + e + f) / 6
    final[i, :] = output

np.savetxt(r"variables_50000_distribution_b3t3.txt", final, delimiter=',', fmt='%8.4f')
