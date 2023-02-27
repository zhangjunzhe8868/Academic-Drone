# convert points to lines, but need arcgis to combine single line to
# one shapefile after using this code 
import osgeo.ogr as ogr
import osgeo.osr as osr
import numpy as np

data = np.loadtxt('extract_more_points_b3t1.txt', delimiter=',')

driver = ogr.GetDriverByName("ESRI Shapefile")
data_source = driver.CreateDataSource("line_more_b3t1.shp")

srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

layer = data_source.CreateLayer("line_more_b3t1", srs, ogr.wkbMultiLineString)

field_name = ogr.FieldDefn("Name", ogr.OFTString)
field_name.SetWidth(24)
layer.CreateField(field_name)
layer.CreateField(ogr.FieldDefn("Latitude", ogr.OFTReal))
layer.CreateField(ogr.FieldDefn("Longitude", ogr.OFTReal))


for i in range(500):
    a = data[i * 102+0, 2]
    b = data[i * 102+0, 1]
    c = data[i * 102+101, 2]
    d = data[i * 102+101, 1]
    print(a, b, c, d)

    feature = ogr.Feature(layer.GetLayerDefn())
    feature.SetField("Name", str(i))
    feature.SetField("Latitude", b)
    feature.SetField("Longitude", a)

    # wkt = 'polygon((-106.7646072 32.55163031, -106.7635969 32.5519192))'
    wkt = ('polygon((' + str(a) + ' ' + str(b) + ', ' + str(c) +
           ' ' + str(d) + '))')
    print(wkt)
    polygon = ogr.CreateGeometryFromWkt(wkt)
    feature.SetGeometry(polygon)
    layer.CreateFeature(feature)
    feature = None
    
data_source = None
