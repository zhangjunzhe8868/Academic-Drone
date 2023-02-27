# make samples
# make point sample in the transect lines
import numpy as np
lpi_lat = np.zeros((64))
lpi_lon = np.zeros((64))
lpi_lat1 = np.zeros((200, 64))
lpi_lon1 = np.zeros((200, 64))
final = np.zeros((64*200, 2))

down_N1_lat = 32.550999
down_N5_lat = 32.5507558278999
down_N1_lon = -106.763755
down_N5_lon = -106.763671157
up_N3_lat = 32.5507288710999
side_N3_lat = 32.5510129637999
up_N3_lon = -106.764225358
side_N3_lon = -106.763218300999

col_lat_step = (down_N1_lat - down_N5_lat) / 63
col_lon_step = (down_N1_lon - down_N5_lon) / 63
row_lat_step = (up_N3_lat - side_N3_lat) / 200  #tc is 170
row_lon_step = (up_N3_lon - side_N3_lon) / 200  #tc is 170
lat_start = down_N5_lat + 100 * row_lat_step
lon_start = down_N5_lon + 100 * row_lon_step
for i in range(64):
    lpi_lat[i] = lat_start + i * col_lat_step
    lpi_lon[i] = lon_start + i * col_lon_step

for i in range(64):
    for j in range(200):
        lpi_lat1[j, i] = lpi_lat[i] - j * row_lat_step
        lpi_lon1[j, i] = lpi_lon[i] - j * row_lon_step

x = lpi_lat1.reshape(64*200)
y = lpi_lon1.reshape(64*200)
final[:, 0] = x
final[:, 1] = y
np.savetxt("input_b3_t1.txt", final, delimiter=',', fmt='%20.16f')
