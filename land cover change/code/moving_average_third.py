# compute moving average value

import numpy as np

input_lpi = np.loadtxt("lpi_b3t4_point.txt")
output1 = np.zeros(200-4)
output2 = np.zeros(200-4)
output3 = np.zeros(200-4)
output4 = np.zeros(200-4)

for i in range(200-4):
    output1[i] = np.sum(input_lpi[i:i+4, 0]) / 4
    output2[i] = np.sum(input_lpi[i:i+4, 1]) / 4
    output3[i] = np.sum(input_lpi[i:i+4, 2]) / 4
    output4[i] = input_lpi[i, 3]

final = np.transpose(np.array([output1, output2, output3, output4]))
np.savetxt(r"b3t4_ma.txt", final, delimiter='   ', fmt='%8.4f')
