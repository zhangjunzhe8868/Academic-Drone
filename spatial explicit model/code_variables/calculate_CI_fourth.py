# randomly pick up 6 out of 1000 to make
# a distribution for 1000 times
# average of mean, std, confidence interval of mean and
# confidence interval of std

import numpy as np
from scipy import stats

input_lpi = np.loadtxt("more_variables_b3t4.txt", delimiter=',')

plt_mean = np.zeros((1000))
can_mean = np.zeros((1000))
bare_mean = np.zeros((1000))
bare1_mean = np.zeros((1000))
plt_std = np.zeros((1000))
can_std = np.zeros((1000))
bare_std = np.zeros((1000))
bare1_std = np.zeros((1000))
plt_t = np.zeros((1000, 2))
can_t = np.zeros((1000, 2))
bare_t = np.zeros((1000, 2))
bare1_t = np.zeros((1000, 2))
plt_chi2 = np.zeros((1000, 2))
can_chi2 = np.zeros((1000, 2))
bare_chi2 = np.zeros((1000, 2))
bare1_chi2 = np.zeros((1000, 2))

for i in range(1000):
    randnum = np.random.random_integers(0, 999, size=6)
    can_mean[i] = np.mean(input_lpi[randnum, 0])
    plt_mean[i] = np.mean(input_lpi[randnum, 1])
    bare_mean[i] = np.mean(input_lpi[randnum, 2])
    bare1_mean[i] = np.mean(input_lpi[randnum, 3])
    can_std[i] = np.std(input_lpi[randnum, 0])
    plt_std[i] = np.std(input_lpi[randnum, 1])
    bare_std[i] = np.std(input_lpi[randnum, 2])
    bare1_std[i] = np.std(input_lpi[randnum, 3])
    can_t[i, :] = stats.t.interval(0.95, 6, can_mean[i], can_std[i])
    plt_t[i, :] = stats.t.interval(0.95, 6, plt_mean[i], plt_std[i])
    bare_t[i, :] = stats.t.interval(0.95, 6, bare_mean[i], bare_std[i])
    bare1_t[i, :] = stats.t.interval(0.95, 6, bare1_mean[i], bare1_std[i])
    where_are_nan = np.isnan(can_t)
    can_t[where_are_nan] = 0
    where_are_nan = np.isnan(plt_t)
    plt_t[where_are_nan] = 0
    where_are_nan = np.isnan(bare_t)
    bare_t[where_are_nan] = 0
    where_are_nan = np.isnan(bare1_t)
    bare1_t[where_are_nan] = 0
    can_chi2[i, 0] = np.sqrt((6) * (can_std[i] ** 2.0) /
                             stats.chi2.ppf(0.975, 6))
    can_chi2[i, 1] = np.sqrt((6) * (can_std[i] ** 2.0) /
                             stats.chi2.ppf(0.025, 6))
    plt_chi2[i, 0] = np.sqrt((6) * (plt_std[i] ** 2.0) /
                             stats.chi2.ppf(0.975, 6))
    plt_chi2[i, 1] = np.sqrt((6) * (plt_std[i] ** 2.0) /
                             stats.chi2.ppf(0.025, 6))
    bare_chi2[i, 0] = np.sqrt((6) * (bare_std[i] ** 2.0) /
                              stats.chi2.ppf(0.975, 6))
    bare_chi2[i, 1] = np.sqrt((6) * (bare_std[i] ** 2.0) /
                              stats.chi2.ppf(0.025, 6))
    bare1_chi2[i, 0] = np.sqrt((6) * (bare1_std[i] ** 2.0) /
                               stats.chi2.ppf(0.975, 6))
    bare1_chi2[i, 1] = np.sqrt((6) * (bare1_std[i] ** 2.0) /
                               stats.chi2.ppf(0.025, 6))
print('mean:', np.mean(bare_mean))
print('std:', np.mean(bare_std))
print('t:', np.mean(bare_t[:, 0]), np.mean(bare_t[:, 1]), np.mean(bare_t))
print('chi2:', np.mean(bare_chi2[:, 0]), np.mean(bare_chi2[:, 1]),
      np.mean(bare_chi2))

##np.savetxt(r"D:\sample_can_mean.txt", can_mean, delimiter=',', fmt='%8.4f')
##np.savetxt(r"D:\sample_plt_mean.txt", plt_mean, delimiter=',', fmt='%8.4f')
##np.savetxt(r"D:\sample_bare_mean.txt", bare_mean, delimiter=',', fmt='%8.4f')
##np.savetxt(r"D:\sample_bare1_mean.txt", bare1_mean, delimiter=',', fmt='%8.4f')
##np.savetxt(r"D:\sample_can_std.txt", can_std, delimiter=',', fmt='%8.4f')
##np.savetxt(r"D:\sample_plt_std.txt", plt_std, delimiter=',', fmt='%8.4f')
##np.savetxt(r"D:\sample_bare_std.txt", bare_std, delimiter=',', fmt='%8.4f')
##np.savetxt(r"D:\sample_bare1_std.txt", bare1_std, delimiter=',', fmt='%8.4f')
