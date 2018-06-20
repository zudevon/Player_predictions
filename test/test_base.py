import unittest
import utils
import simplejson as json
from shapely.geometry import Polygon


class TestClass(unittest.TestCase):

    def test_zone_expand(self):
        json_data = open('../json_files/100zones.json').read()

        zones = json.loads(json_data)
        test1 = [[-75.3735146964451, 40.048726137420715], [-75.37362829302396, 40.04878158188856], [-75.37374124460855, 40.0486622295677], [-75.37356429522984, 40.04841118596099], [-75.37324657386823, 40.04829787293306], [-75.37301969222925, 40.04831048474756], [-75.37271306436878, 40.04844614603036], [-75.37277730512214, 40.04853569209274], [-75.37304177319365, 40.04842993578626], [-75.37324108978545, 40.048419550182956], [-75.3732379251943, 40.048394461396185], [-75.3734837557163, 40.048506505136004], [-75.37350412188319, 40.04852964429341], [-75.37345983972509, 40.048552788337105], [-75.37354869260399, 40.048672089770804], [-75.3735146964451, 40.048726137420715]]
        for x in (range(0, len(zones['data']))):

            coords = zones['data'][x]['geojson']['geometry']['coordinates'][0]

            for i in range(5, 45,5):
                "i is for 1-40 feet expansion for every zone"
                #if i == 18 or i == 9 or i == 16 or i == 41:
                 #   i = i + 1

                "Test if function sends back same coordinates"
                self.assertEqual(utils.coord_extend(coords=coords, feet_expand=i),
                                 utils.coord_extend(coords=coords, feet_expand=i))

                "Test if function actually sends"
                self.assertNotEqual(utils.coord_extend(coords=coords, feet_expand=i), list)

                "Test if function returns list"
                self.assertIsInstance(utils.coord_extend(coords=coords, feet_expand=i), list)

                "Test if last point equals first point"
                self.assertEqual(utils.coord_extend(coords=coords, feet_expand=i)[0],
                                 utils.coord_extend(coords=coords, feet_expand=i)[-1])
                "Test if expanded zone is larger than original"
                coords_area = Polygon(coords).area
                new_coords_area = Polygon(utils.coord_extend(coords=coords, feet_expand=i)).area

                self.assertGreater(new_coords_area, coords_area)

                print(x, i)