# made by Junzhe Zhang
# in order to extract plant height, bare soil gap size, and canopy size
# input: two text files extracted by using ArcGIS ("merge" to combine line shapefile,
# "extract by mask" and "raster to point")
# from the same resolution classification and DEM
# output: one text file with three col (land cover, length, height)

import numpy as np
# set print option to float not exponential
np.set_printoptions(suppress=True)

# input your data (one classification result and one dem),
# suggest to input each transect sepatately
data_class1 = np.loadtxt('extract_more_lines_ortho_b3t2.txt', delimiter=',', skiprows=1,
                         dtype='i4')
data_dem1 = np.loadtxt('extract_more_lines_dem_b3t2.txt', delimiter=',', skiprows=1,
                       dtype='f4')

# convert the classification result to vegetation/bare ground map
for i in range(data_class1.shape[0]):
    if data_class1[i, -1] == 5:
        data_class1[i, -1] = 0
    else:
        data_class1[i, -1] = 1

# np.savetxt('D:\\class.txt',data_class,delimiter=',',fmt='%i')
integer = int(data_dem1.shape[0] / 1000)

for j in range(1000):
    data_class = data_class1[integer * j:integer * (j+1)]
    data_dem = data_dem1[integer * j:integer * (j+1)]
    print(data_class.shape, data_dem.shape)
    print(j)
    # find the land cover change point
    temp = np.zeros(0)
    for i in range(data_class.shape[0]-1):
        if data_class[i, -1] != data_class[i+1, -1]:
            temp = np.append(temp, (data_class[i, 1] - j * integer))

    # find the size greater than 25 cm
    temp1 = np.zeros(0)
    for i in range(temp.shape[0]-1):
        if (temp[i+1] - temp[i]) * (50 * 100 / data_class.shape[0]) > 25:
            temp1 = np.append(temp1, temp[i])

    # clean the discontinous data
    temp2 = np.zeros((temp1.shape[0], 2))
    for i in range(temp1.shape[0]):
        temp2[i, 0] = data_class[int(temp1[i]), -1]
        temp2[i, 1] = temp1[i]

    temp3 = np.zeros(0)
    for i in range(temp2.shape[0] - 1):
        if temp2[i, 0] != temp2[i+1, 0]:
            temp3 = np.append(temp3, temp2[i+1, 1])

    # add the start and end points
    temp4 = np.zeros((temp3.shape[0]+2, 2))
    for i in range(1, temp3.shape[0]+1):
        temp4[i, 0] = data_class[int(temp3[i-1]), -1]
        temp4[i, 1] = temp3[i-1]
    temp4[0, 0] = int(1-temp4[1, 0])
    temp4[0, 1] = 0
    temp4[-1, 0] = int(1-temp4[-2, 0])
    temp4[-1, 1] = data_class.shape[0]

    # if=whole bare soil, else=normal
    if temp4.shape[0] < 3:
        final2 = np.array([[1, 5000, 0]])
        final1 = final2
        final = final2
    else:
        # get the height from DEM
        c = np.zeros(temp4.shape[0])
        for i in range(1, temp4.shape[0]):
            if temp4[i, 0] == 0:
                a = np.max(data_dem[int(temp4[i-1, 1]):int(temp4[i, 1]), -1])
                b = np.min(data_dem[int(temp4[i-1, 1]):int(temp4[i, 1]), -1])
                c[i] = a - b

        # compute the size (pixel to m)
        temp5 = np.zeros(1)
        for i in range(1, temp4.shape[0]):
            temp5 = np.append(temp5, temp4[i, 1]-temp4[i-1, 1])

        # put all data together (reverse it)
        final = np.zeros((temp4.shape[0], 3), dtype=float)
        final[:, 0] = temp4[:, 0]
        final[:, 1] = temp5 * (50 * 100 / data_class.shape[0])
        final[:, 2] = c * 100

        # important: it the height (7 for here, may change) is too short,
        # considering it is wrong
        for i in range(1, final.shape[0]-1):
            if final[i, 2] <= 7:
                final[i, 0] = 1
                final[i, 2] = 0
        # filter the duplicated data
        for i in range(1, final.shape[0]):
            if final[i, 0] == final[i-1, 0]:
                final[i, 1] = final[i, 1] + final[i-1, 1]
                final[i, 2] = max(final[i, 2], final[i-1, 2])
                final[i-1, 1] = 0
                final[i-1, 2] = 0
        final1 = np.copy(final)
        total = np.zeros(0)
        for i in range(final.shape[0]):
            if final[i, 1]+final[i, 2] == 0:
                total = np.append(total, i)
        final2 = np.delete(final1, total, 0)

    np.savetxt("extraction\\output" + str(j) + ".txt", final2, delimiter=',',
               header='landcover(0=plant, 1=soil), length(cm), height(cm)',
               fmt='%8.4f', comments='')
