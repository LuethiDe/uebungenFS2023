import matplotlib.pyplot as plt
import shapely
import shapely.wkt

g0 = shapely.wkt.loads("POINT(2 2)")
g1 = shapely.wkt.loads("LINESTRING(0 0,1 1,1 2)")
g2 = shapely.wkt.loads("POLYGON((0 0, 4 0, 4 4, 0 4, 0 0),(1 1, 2 1, 2 2, 1 2, 1 1))")
g3 = shapely.wkt.loads("MULTIPOINT(0 0, 1 2)")
g4 = shapely.wkt.loads("MULTILINESTRING((0 0, 1 1, 1 2),(2 3, 3 2, 5 4))")
g5 = shapely.wkt.loads("MULTIPOLYGON(((0 0, 4 0, 4 4, 0 4, 0 0),(1 1, 2 1, 2 2, 1 2, 1 1)),((-1 -1, -1 -2, -2 -2, -2 -1, -1 -1)))")
g6 = shapely.wkt.loads("GEOMETRYCOLLECTION(POINT(2 3), LINESTRING(2 3, 3 4))")

x,y = g0.xy #Point
plt.plot(x,y,'bx')

x,y = g1.xy #Linestring
plt.plot(x,y,'ro-')
print("Länge Linestring g1:", g1.length)

x,y = g2.exterior.xy #Polygon
plt.plot(x,y,'ko-')
print("Länge Polygon g2:", g2.length)

x,y = g2.interiors[0].xy #Polygon
plt.plot(x,y,'go-')
print("Länge Polygon g2:", g2.length)
print("Fläche Polygon g2:", g2.area)

for point in g3.geoms:  # MultiPoint
    x, y = point.xy
    plt.plot(x, y, 'y*', markersize=10)

for line in g4.geoms:  # MultiLineString
    x, y = line.xy
    plt.plot(x, y, 'm--')
    print("Länge MultiLineString g4:", g3.length)

for polygon in g5.geoms:  # MultiPolygon
    x, y = polygon.exterior.xy
    plt.plot(x, y, 'c-')
    print("Länge MultiPolygon g5:", g5.length)
    for interior in polygon.interiors:
        x, y = interior.xy
        plt.plot(x, y, 'g--')
        print("Länge Polygon g5:", g5.length)
        print("Fläche Polygon g5:", g5.area)

for geometry in g6.geoms:  # GeometryCollection
    if geometry.type == "Point":
        x, y = geometry.xy
        plt.plot(x, y, 'bs')
        print("Punkt:", geometry)
    elif geometry.type == "LineString":
        x, y = geometry.xy
        plt.plot(x, y, 'r-.')
        print("Linestring:", geometry)
        print("Länge Linestring g6:", g6.length)
    

plt.axis("equal")
plt.show()