import unittest
import utils
import simplejson as json
from shapely.geometry import Polygon

# Run utils.coor_extend()
# test_zone_expansion.py holds the correct function so does utils.py


class TestClass(unittest.TestCase):

    def test_zone_equalizer(self):

        """ Test to see if coordinates ran more than twice equal the same amount both times"""

        basicSquare = [(0, 0), (0, 1), (1, 1), (1, 0)]
        basicTriangle = [(1,1), (1,0), (0,0)]

        new_square = utils.coord_extend(coords=basicSquare, feet_expand=10)
        new_triangle = utils.coord_extend(coords=basicTriangle, feet_expand=10)

        for i in range(0, 20):
            self.assertEqual(utils.coord_extend(coords=basicSquare, feet_expand=10),
                             new_square)
            self.assertEqual(utils.coord_extend(coords=basicTriangle, feet_expand=10),
                             new_triangle)


    def test_zone_expand(self):
        json_data = open('../json_files/100zones.json').read()

        zones = json.loads(json_data)


        for x in (range(0, len(zones['data']))):

            coords = zones['data'][x]['geojson']['geometry']['coordinates'][0]

            for i in range(5, 200, 5):

                """"Test if function sends back same coordinates"""
                self.assertEqual(utils.coord_extend(coords=coords, feet_expand=i),
                                 utils.coord_extend(coords=coords, feet_expand=i))

                """"Test if function actually sends a list with elements"""
                self.assertNotEqual(utils.coord_extend(coords=coords, feet_expand=i), list)

                """"Test if function returns list"""
                self.assertIsInstance(utils.coord_extend(coords=coords, feet_expand=i), list)

                """Test if last point equals first point"""
                self.assertEqual(utils.coord_extend(coords=coords, feet_expand=i)[0],
                                 utils.coord_extend(coords=coords, feet_expand=i)[-1])

                """Test if expanded zone is larger than original"""
                coords_area = Polygon(coords).area
                new_coords_area = Polygon(utils.coord_extend(coords=coords, feet_expand=i)).area
                self.assertGreater(new_coords_area, coords_area)