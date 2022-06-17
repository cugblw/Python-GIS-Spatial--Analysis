import geojson
import shapely.wkt


def points_to_geojson(points):
    """
    Convert a list of points to a geojson object.
    """
    return None


def polyline_to_geojson(polyline):
    """
    Convert a list of lines to a geojson object.
    """
    return None


def polygon_to_geojson(polygon):
    """
    Convert a list of polygons to a geojson object.
    """
    polygon_geometry = shapely.wkt.loads(polygon)

    polygon_geojson = geojson.Feature(geometry=polygon_geometry, properties={})

    # polygon_geojson.geometry
    return polygon_geojson


if __name__ == '__main__':
    Polygon = "POLYGON ((121.14744186401366 23.047985767509395, 121.26142501831056 23.047985767509395, 121.26142501831056 23.148252272743257, 121.14744186401366 23.148252272743257, 121.14744186401366 23.047985767509395))"
    print(polygon_to_geojson(Polygon).geometry)
    pass
