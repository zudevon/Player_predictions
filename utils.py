from shapely.geometry import LinearRing


def test_me():
    return True


def coord_extend(coords, feet_expand):
    if feet_expand <= 0:
        raise ValueError("Negative value input")
    if feet_expand % 5 != 0:
        raise ValueError("Expansion values must be multiples of 5")

    def lat_convert(n):
        degrees = n / 305775
        return degrees

    if feet_expand <= 40:

        feet_expand = lat_convert(feet_expand)

        obj1 = LinearRing(coords)

        offset_1a = obj1.parallel_offset(feet_expand, 'left', join_style=2, mitre_limit=1000.0)
        offset_2a = obj1.parallel_offset(feet_expand, 'right', join_style=2, mitre_limit=1000.0)

        offset_a = offset_1a if offset_1a.length > offset_2a.length else offset_2a

        new_offset_a = LinearRing(offset_a)

        new_coords_a = list(new_offset_a.coords)

        def coordinate_give(x):
            return [[i[0], i[1]] for i in x]

        give_a = coordinate_give(new_coords_a)

        return give_a


    else:

        feet_expand = lat_convert(feet_expand/2)

        obj1 = LinearRing(coords)

        offset_1a = obj1.parallel_offset(feet_expand, 'left', join_style=2, mitre_limit=1000.0)
        offset_2a = obj1.parallel_offset(feet_expand, 'right', join_style=2, mitre_limit=1000.0)

        offset_a = offset_1a if offset_1a.length > offset_2a.length else offset_2a

        new_offset_a = LinearRing(offset_a)

        new_coords_a = list(new_offset_a.coords)

        def coordinate_give(x):
            return [[i[0], i[1]] for i in x]

        give_a = coordinate_give(new_coords_a)

        obj2 = LinearRing(give_a)

        offset_1b = obj2.parallel_offset(feet_expand, 'left', join_style=2, mitre_limit=1000.0)
        offset_2b = obj2.parallel_offset(feet_expand, 'right', join_style=2, mitre_limit=1000.0)

        offset_b = offset_1b if offset_1b.length > offset_2b.length else offset_2b

        new_offset_b = LinearRing(offset_b)

        new_coords_b = list(new_offset_b.coords)

        def coordinate_give(x):
            return [[i[0], i[1]] for i in x]

        give_b = coordinate_give(new_coords_b)

        return give_b
