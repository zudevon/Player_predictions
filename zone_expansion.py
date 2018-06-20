from shapely.geometry import LinearRing

def coord_extend(coords, feet_expand):
    """ 40 is the max amount of feet that a zone can be expanded """
    """ 0 is the minimum amount a zone can be minimized"""

    def latConvert(n):
        degrees = n / 305775
        return degrees

    def coordinate_get(x):
        return [(i[0], i[1]) for i in x]

    def coordinate_give(x):
        return [[i[0], i[1]] for i in x]

    # get = coordinate_get(coords)

    feet_expand = latConvert(feet_expand)

    obj = LinearRing(coords)

    offset_1 = obj.parallel_offset(feet_expand, 'left', join_style=2, mitre_limit=10.0)
    offset_2 = obj.parallel_offset(feet_expand, 'right', join_style=2, mitre_limit=10.0)

    #
    if offset_1.length > offset_2.length:
        orient = 'left'
    else:
        orient = 'right'

    offset = obj.parallel_offset(feet_expand, orient, join_style=2, mitre_limit=1000.0)

    offset = LinearRing(offset)

    new_coords = list(offset.coords)

    give = coordinate_give(new_coords)

    return (give)