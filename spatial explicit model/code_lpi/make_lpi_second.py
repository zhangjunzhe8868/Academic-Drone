# calculate the veg and bare soil in each line, 1 m is the interval in length and
# 0.04 m is the interval in width
# 500*102
import numpy as np

input_lpi = np.loadtxt("extract_more_points_b3t2.txt", delimiter=',')
lpi = input_lpi
for j in range(lpi.size):
    if lpi[j] < 0:
        lpi[j] = 5
bare = np.zeros((500))
veg = np.zeros((500))

# 102 points in one col, because the mid-points are duplicate
for i in range(500):
    unique_elements, counts_elements = np.unique(lpi[i*101:(i+1)*101],
                                                 return_counts=True)
    print(unique_elements)
    print(counts_elements)
    if counts_elements.size == 2:
        bare[i] = counts_elements[1] / 101
        if unique_elements[0] == 2:
            veg[i] = counts_elements[0] / 101
        elif unique_elements[0] == 3:
            veg[i] = counts_elements[0] / 101
        elif unique_elements[0] == 4:
            veg[i] = counts_elements[0] / 101
    elif counts_elements.size == 3:
        bare[i] = counts_elements[2] / 101
        if unique_elements[0] == 2 and unique_elements[1] == 3:
            veg[i] = (counts_elements[0] + counts_elements[1]) / 101
        elif unique_elements[0] == 2 and unique_elements[1] == 4:
            veg[i] = (counts_elements[0] + counts_elements[1]) / 101
        elif unique_elements[0] == 3 and unique_elements[1] == 4:
            veg[i] = (counts_elements[0] + counts_elements[1]) / 101
    elif counts_elements.size == 4:
        bare[i] = counts_elements[3] / 101
        veg[i] = (counts_elements[0] + counts_elements[1] +
                  counts_elements[2]) / 101
    elif counts_elements.size == 5:
        bare[i] = counts_elements[4] / 101
        veg[i] = (counts_elements[1] + counts_elements[2] +
                  counts_elements[3]) / 101
        
final = np.transpose(np.array([veg, bare]))
np.savetxt(r"lpi_more_b3t2.txt", final, delimiter=',', fmt='%8.4f')
