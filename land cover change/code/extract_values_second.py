# extract pixel value
# 0.5 m is the interval in length and 0.4 m is the interval in width
import numpy as np

input_lpi = np.loadtxt("export_lpi_b3t2_arc.txt")
lpi = input_lpi[:, 3]
for j in range(lpi.size):
    if lpi[j] < 0:
        lpi[j] = 5

soil = np.zeros((200))
shrub = np.zeros((200))
grass = np.zeros((200))
number = np.zeros((200))


for i in range(200):
    unique_elements, counts_elements = np.unique(lpi[i*64:(i+1)*64],
                                                 return_counts=True)
    print(unique_elements)
    print(counts_elements)
    print("#######")
    if counts_elements.size == 2:
        soil[i] = counts_elements[1] / 64
        if unique_elements[0] == 2:
            shrub[i] = counts_elements[0] / 64
        elif unique_elements[0] == 3:
            shrub[i] = counts_elements[0] / 64
        elif unique_elements[0] == 4:
            grass[i] = counts_elements[0] / 64
    elif counts_elements.size == 3:
        soil[i] = counts_elements[2] / 64
        if unique_elements[0] == 2 and unique_elements[1] == 3:
            shrub[i] = (counts_elements[0] + counts_elements[1]) / 64
        elif unique_elements[0] == 2 and unique_elements[1] == 4:
            shrub[i] = counts_elements[0] / 64
            grass[i] = counts_elements[1] / 64
        elif unique_elements[0] == 3 and unique_elements[1] == 4:
            shrub[i] = counts_elements[0] / 64
            grass[i] = counts_elements[1] / 64
    elif counts_elements.size == 4:
        soil[i] = counts_elements[3] / 64
        shrub[i] = (counts_elements[0] + counts_elements[1]) / 64
        grass[i] = counts_elements[2] / 64
    elif counts_elements.size == 5:
        soil[i] = counts_elements[4] / 64
        shrub[i] = (counts_elements[1] + counts_elements[2]) / 64
        grass[i] = counts_elements[3] / 64
    number[i] = i-100

final = np.transpose(np.array([grass,shrub,soil,number]))
np.savetxt(r"lpi_b3t2_point.txt", final, delimiter='    ', fmt='%8.4f')
