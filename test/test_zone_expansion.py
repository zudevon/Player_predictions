from shapely.geometry import LinearRing


def coord_extend(coords, feet_expand):

    def lat_convert(n):
        degrees = n / 305775
        return degrees

    #def coordinate_get(x):
        #return [(i[0], i[1]) for i in x]

    #get = coordinate_get(coords)

    feet_expand = lat_convert(int)

    obj = LinearRing(coords)

    offset_1 = obj.parallel_offset(feet_expand, 'left', join_style=2, mitre_limit=10.0)
    offset_2 = obj.parallel_offset(feet_expand, 'right', join_style=2, mitre_limit=10.0)

    if offset_1.length > offset_2.length:
        orient = 'left'
    else:
        orient = 'right'


    offset=obj.parallel_offset(feet_expand,orient,join_style=2,mitre_limit=(1000.0))

    offset = LinearRing(offset)

    new_coords = list(offset.coords)

    def coordinate_give(x):
        return [[i[0], i[1]] for i in x]

    give = coordinate_give(new_coords)

    return give