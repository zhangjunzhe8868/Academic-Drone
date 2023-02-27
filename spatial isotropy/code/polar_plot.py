# plot for polar plot

import numpy as np
import matplotlib.pyplot as plt

direction = 0
max_axis = 50
min_axis = 50
max_step = 5
min_step = 5

data_input_veg = np.loadtxt('polar_veg.txt')
data_input_soil = np.loadtxt('polar_soil.txt')

dataLenth = 180
data_veg = data_input_veg[:, 1]
data_soil = data_input_soil[:, 1]

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
angles1 = np.concatenate((angles, [angles[0]]))
data_veg1 = np.concatenate((data_veg, [data_veg[0]]))
data_soil1 = np.concatenate((data_soil, [data_soil[0]]))

data_max1 = np.arange(0, max_axis, max_step)
angles_max1 = np.ones((int(max_axis/max_step))) * direction / 180 * np.pi
data_max2 = np.arange(0, max_axis, max_step)
angles_max2 = np.ones((int(max_axis/max_step))) * (direction / 180 * np.pi + np.pi)
data_min1 = np.arange(0, min_axis, min_step)
angles_min1 = np.ones((int(max_axis/max_step))) * (direction / 180 * np.pi + np.pi / 2)
data_min2 = np.arange(0, min_axis, min_step)
angles_min2 = np.ones((int(max_axis/max_step))) * (direction / 180 * np.pi + np.pi * 1.5)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles1, data_veg1, 'k.-', linewidth=1, markersize=2)
ax.plot(angles1, data_soil1, 'k.-', linewidth=1, markersize=2)
ax.plot(angles_max2, data_max2, 'k-.', linewidth=1, markersize=0.1)
ax.plot(angles_max1, data_max1, 'k-.', linewidth=1, markersize=0.1)
ax.plot(angles_min2, data_min2, 'k-.', linewidth=1, markersize=0.1)
ax.plot(angles_min1, data_min1, 'k-.', linewidth=1, markersize=0.1)

name = ['0', '45', '90', '135', '180', '225', '270', '315']
theta = np.linspace(0, 2*np.pi, len(name), endpoint=False)
ax.set_thetagrids(theta*180/np.pi, name)
ax.set_theta_zero_location('E')
ax.set_rticks([100, 200, 300])  # Less radial ticks
# ax.set_rlabel_position(22.5)  # Move radial labels away from plotted line
# ax.set_title("Polar", va='bottom', fontproperties="SimHei")
ax.grid(True)
# plt.show()
plt.savefig('combo_polar1.png', dpi=300)
plt.clf()
