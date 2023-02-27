# plot line plot with scatter points

import numpy as np
import matplotlib.pyplot as plt

name = 'grass/litter', 'shrub', 'soil'
name1 = 'Mov.Avg.(grass/litter)', 'Mov.Avg.(shrub)', 'Mov.Avg.(soil)'
opacity = 1

# scatter
data_scatter = np.loadtxt('lpi_b3t4_point.txt')
print(data_scatter.shape)
x_scatter = data_scatter[:, 3] / 2
y1_scatter = data_scatter[:, 0]
y2_scatter = data_scatter[:, 1]
y3_scatter = data_scatter[:, 2]
volume = 5 ** 2
scatts1 = plt.scatter(x_scatter, y1_scatter, s=volume, c='white',
                      alpha=opacity, edgecolor='black',
                      label=name[0])
scatts2 = plt.scatter(x_scatter, y2_scatter, s=volume, c='white',
                      alpha=opacity, edgecolor='black',
                      label=name[1], marker='v')
scatts3 = plt.scatter(x_scatter, y3_scatter, s=volume, c='white',
                      alpha=opacity, edgecolor='black',
                      label=name[2], marker='^')

# line
data_ma = np.loadtxt('b3t4_ma.txt')
print(data_ma.shape)
x_ma = data_ma[:, 3] / 2
y1_ma = data_ma[:, 0]
y2_ma = data_ma[:, 1]
y3_ma = data_ma[:, 2]

plt.plot(x_ma, y1_ma, c='black', alpha=opacity, label=name1[0],
         linewidth=2, linestyle='-')
plt.plot(x_ma, y2_ma, c='black', alpha=opacity, label=name1[1],
         linewidth=2, linestyle='--')
plt.plot(x_ma, y3_ma, c='black', alpha=opacity, label=name1[2],
         linewidth=2, linestyle='-.')

# plt.xticks(np.arange(-60, 60, 10))
# plt.yticks(np.arange(0, 1.1, 0.2))
plt.tick_params(axis='both', which='major', labelsize=14)
plt.ylim(ymax=1, ymin=0)
plt.xlim(xmax=50, xmin=-50)
plt.legend(loc=5, ncol=1, fontsize=14)
plt.axvline(x=0, color='black')
# plt.title('Land cover')
plt.ylabel('Cover(%)', fontsize=16)
plt.xlabel('Distance from the middle boundary of upwind and downwind area',
           fontsize=16)
fig = plt.gcf()
fig.set_size_inches(15, 6.5)
# plt.show()
plt.savefig('soil_short_b3t4.png', dpi=300)
plt.clf()
