# calculate the mean bare soil gap size and plant height from the extraction folder 
import numpy as np

veg_size = np.zeros(1000)
veg_height = np.zeros(1000)
bare = np.zeros(1000)
bare1 = np.zeros(1000)
a = []
b = []

for i in range(1000):
    data = np.loadtxt('extraction/output'+str(i)+'.txt', delimiter=',', skiprows=1)
    # print(data.size)
    if data.size != 3:
        unique, index, counts = np.unique(data[:, 0], return_inverse=True,
                                          return_counts=True)
        # 1=bare, 0=veg
        x = np.mean(data[(np.where(index == 0)), 1])
        y = np.mean(data[(np.where(index == 0)), 2])
        z = np.mean(data[(np.where(index == 1)), 1])
        # cal the mean of 1000*n
        a = np.append(a, data[(np.where(index == 0)), 1])
        b = np.append(b, data[(np.where(index == 0)), 2])
        # cal the precentage of bare soil gap / 5000
        z1 = np.sum(data[(np.where(index == 1)), 1])

        veg_size[i] = x
        veg_height[i] = y
        bare[i] = z
        bare1[i] = z1 / 5000
    else:
        veg_size[i] = 0
        veg_height[i] = 0
        bare[i] = 5000
        bare1[i] = 5000 / 5000
print(veg_size, veg_height, bare, bare1)
print('mean_can:', np.mean(a), "mean_plt:", np.mean(b))
final = np.transpose(np.array([veg_size, veg_height, bare, bare1]))
np.savetxt('more_variables_b3t2.txt', final, delimiter=',', fmt='%8.4f')
