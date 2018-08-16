from shapely.geometry import LinearRing

import math

# Distances are measured in miles.
# Longitudes and latitudes are measured in degrees.
# Earth is assumed to be perfectly spherical.

earth_radius = 3960.0
degrees_to_radians = math.pi/180.0
radians_to_degrees = 180.0/math.pi


def change_in_longitude(latitude, miles):
    "Given a latitude and a distance west, return the change in longitude."
    # Find the radius of a circle around the earth at given latitude.
    r = earth_radius*math.cos(latitude*degrees_to_radians)
    return (miles/r)*radians_to_degrees


def coord_extend(coords: list, feet_expand: int):

    def lat_convert(n):
        degrees = n / 305775
        return degrees

    degrees_expand = lat_convert(feet_expand)

    def to_linear_ring_tuples(x):
        return [(i[0], i[1]) for i in x]

    obj = LinearRing(to_linear_ring_tuples(coords))

    offset_1 = obj.parallel_offset(degrees_expand, 'left', join_style=2, mitre_limit=10.0)
    offset_2 = obj.parallel_offset(degrees_expand, 'right', join_style=2, mitre_limit=10.0)

    if offset_1.length > offset_2.length:
        orient = 'left'
    else:
        orient = 'right'

    offset = obj.parallel_offset(degrees_expand, orient, join_style=2, mitre_limit=1000.0)

    offset = LinearRing(offset)

    new_coords = list(offset.coords)

    def coordinate_give(x):
        return [[i[0], i[1]] for i in x]

    give = coordinate_give(new_coords)

    return give