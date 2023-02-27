# randomly pick up 3 out of 500 to make 
# a distribution for 1000 or 50000 times
# average of mean, std, confidence interval of mean and 
# confidence interval of std

import numpy as np
from scipy import stats

input_lpi = np.loadtxt("lpi_more_b3tc.txt",delimiter=',')

np.random.seed(8)
randnum1 = np.random.random_integers(0, 499, 500)
np.random.seed(9)
randnum2 = np.random.random_integers(0, 499, 500)
np.random.seed(10)
randnum3 = np.random.random_integers(0, 499, 500)
final_output = np.zeros((500, 6))
soil_mean = np.zeros((500))
veg_mean = np.zeros((500))
soil_std = np.zeros((500))
veg_std = np.zeros((500))
soil_t = np.zeros((500, 2))
veg_t = np.zeros((500, 2))
soil_chi2 = np.zeros((500, 2))
veg_chi2 = np.zeros((500, 2))

for i in range(500):
    a = input_lpi[randnum1[i], :]
    b = input_lpi[randnum2[i], :]
    c = input_lpi[randnum3[i], :]
    final_output[i, :] = np.append(a, [b, c])
    soil_mean[i] = np.mean(np.array([final_output[i, 0], final_output[i, 2], # soil in first
                                    final_output[i, 4]]))
    veg_mean[i] = np.mean(np.array([final_output[i, 1], final_output[i, 3],
                                   final_output[i, 5]]))
    soil_std[i] = np.std(np.array([final_output[i, 0], final_output[i, 2],
                                  final_output[i, 4]]))
    veg_std[i] = np.std(np.array([final_output[i, 1], final_output[i, 3],
                                 final_output[i, 5]]))

    soil_t[i, :] = stats.t.interval(0.95, 6, soil_mean[i], soil_std[i])
    veg_t[i, :] = stats.t.interval(0.95, 6, veg_mean[i], veg_std[i])
    where_are_nan = np.isnan(soil_t)
    soil_t[where_are_nan] = 0
    where_are_nan = np.isnan(veg_t)
    veg_t[where_are_nan] = 0
    soil_chi2[i, 0] = np.sqrt((6)*(soil_std[i]**2.0)/stats.chi2.ppf(0.975, 6))
    soil_chi2[i, 1] = np.sqrt((6)*(soil_std[i]**2.0)/stats.chi2.ppf(0.025, 6))
    veg_chi2[i, 0] = np.sqrt((6)*(veg_std[i]**2.0)/stats.chi2.ppf(0.975, 6))
    veg_chi2[i, 1] = np.sqrt((6)*(veg_std[i]**2.0)/stats.chi2.ppf(0.025, 6))
print('mean:', np.mean(veg_mean))
print('std:', np.mean(veg_std))
print('veg_t:', np.mean(veg_t[:, 0]), np.mean(veg_t[:, 1]), np.mean(veg_t))
print('veg_chi2:', np.mean(veg_chi2[:, 0]), np.mean(veg_chi2[:, 1]),
      np.mean(veg_chi2))

# np.savetxt(r"D:\sample_soil_mean.txt", soil_mean, delimiter=',', fmt='%8.4f')
# np.savetxt(r"D:\sample_veg_mean.txt", veg_mean, delimiter=',', fmt='%8.4f')
# np.savetxt(r"D:\sample_soil_std.txt", soil_std, delimiter=',', fmt='%8.4f')
# np.savetxt(r"D:\sample_veg_std.txt", veg_std, delimiter=',', fmt='%8.4f')
# np.savetxt(r"D:\sample_soil_t.txt", soil_t, delimiter=',', fmt='%8.4f')
# np.savetxt(r"D:\sample_veg_t.txt", veg_t, delimiter=',', fmt='%8.4f')
# np.savetxt(r"D:\sample_soil_chi2.txt", soil_chi2, delimiter=',', fmt='%8.4f')
# np.savetxt(r"D:\sample_veg_chi2.txt", veg_chi2, delimiter=',', fmt='%8.4f')
