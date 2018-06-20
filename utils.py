from shapely.geometry import LinearRing


def test_me():
    return True


def coord_extend(coords, feet_expand):

    if feet_expand > 40:
        raise ValueError("You can only expand zone up to 40 ft")
    if feet_expand <= 0:
        raise ValueError("Negative value input")
    if feet_expand % 5 != 0:
        raise ValueError("Expansion values must be multiples of 5")
    def lat_convert(n):
        degrees = n / 305775
        return degrees

    # def coordinate_get(x):
    # return [(i[0], i[1]) for i in x]

    # get = coordinate_get(coords)

    feet_expand = lat_convert(feet_expand)

    obj = LinearRing(coords)

    #try catch
    offset_1 = obj.parallel_offset(feet_expand, 'left', join_style=2, mitre_limit=1000.0)
    offset_2 = obj.parallel_offset(feet_expand, 'right', join_style=2, mitre_limit=1000.0)

    offset = offset_1 if offset_1.length > offset_2.length else offset_2

    #if offset_1.length > offset_2.length:
     #   orient = 'left'
    #else:
     #   orient = 'right'

        #offset = obj.parallel_offset(feet_expand, orient, join_style=2, mitre_limit=1000.0)
    new_offset = LinearRing(offset)
    #try:
      # offset = LinearRing(offset)
    #except NotImplementedError as e:
       #try:
           #offset = obj.parallel_offset(feet_expand+1, orient, join_style=2, mitre_limit=1000.0)
       #except NotImplementedError as e:
           #pass

    new_coords = list(new_offset.coords)

    def coordinate_give(x):
        return [[i[0], i[1]] for i in x]

    give = coordinate_give(new_coords)

    return give
