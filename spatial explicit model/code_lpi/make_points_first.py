# make more lines

import osgeo.ogr as ogr
import osgeo.osr as osr
import numpy as np

input_lpi = np.loadtxt("GPS_b3t2.txt")  # this file is the left line and right line with 102 point
lat = np.zeros((102))
lon = np.zeros((102))
lpi_lat = np.zeros((500, 102))
lpi_lon = np.zeros((500, 102))
final = np.zeros(((102*500), 2))

for i in range(102):
    lat[i] = (input_lpi[i, 2] - input_lpi[i, 0]) / 316
    lon[i] = (input_lpi[i, 3] - input_lpi[i, 1]) / 316

for i in range(102):
    for j in range(500):
        lpi_lat[j, i] = input_lpi[i, 0] - (input_lpi[i, 2] - input_lpi[i, 0]) \
                        / 316 * 92 + j * lat[i]
        lpi_lon[j, i] = input_lpi[i, 1] - (input_lpi[i, 3] - input_lpi[i, 1]) \
                        / 316 * 92 + j * lon[i]

x = lpi_lat.reshape(102 * 500)
y = lpi_lon.reshape(102 * 500)
final[:, 0] = x
final[:, 1] = y
np.savetxt("more_points_b3t2.txt", final, delimiter=',', fmt='%20.16f')

# use a dictionary reader so we can access by field name
reader=final

# set up the shapefile driver
driver = ogr.GetDriverByName("ESRI Shapefile")

# create the data source
data_source = driver.CreateDataSource("more_points_b3t2.shp")

# create the spatial reference, WGS84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

# create the layer
layer = data_source.CreateLayer("more_points_b3t2", srs, ogr.wkbPoint)

# Add the fields we're interested in
# field_name = ogr.FieldDefn("Name", ogr.OFTString)
# field_name.SetWidth(24)
# layer.CreateField(field_name)
# field_region = ogr.FieldDefn("Region", ogr.OFTString)
# field_region.SetWidth(24)
# layer.CreateField(field_region)
layer.CreateField(ogr.FieldDefn("Latitude", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("Longitude", ogr.OFTReal))
# layer.CreateField(ogr.FieldDefn("Elevation", ogr.OFTInteger))

# Process the text file and add the attributes and features to the shapefile
for row in reader:
  # create the feature
    feature = ogr.Feature(layer.GetLayerDefn())
  # Set the attributes using the values from the delimited text file
#   feature.SetField("Name", row['Name'])
#   feature.SetField("Region", row['Region'])
    feature.SetField("Latitude", row[0])
    feature.SetField("Longitude", row[1])
#   feature.SetField("Elevation", row['Elev'])

  # create the WKT for the feature using Python string formatting
    wkt = "POINT(%f %f)" %  (float(row[1]) , float(row[0]))

  # Create the point from the Well Known Txt
    point = ogr.CreateGeometryFromWkt(wkt)

  # Set the feature geometry using the point
    feature.SetGeometry(point)
  # Create the feature in the layer (shapefile)
    layer.CreateFeature(feature)
  # Dereference the feature
    feature = None

# Save and close the data source
data_source = None
