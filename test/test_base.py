import unittest
import utils


class TestClass(unittest.TestCase):

    def test_zone_equalizer(self):

        """ Test to see if coordinates ran more than twice equal the same amount both times"""

        basic_square = [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0], [0.0, 0.0]]
        basic_triangle = [[1.0, 1.0], [1.0, 0.0], [0.0, 0.0], [1.0, 1.0]]

        square = utils.coord_extend(coords=basic_square, feet_expand=0)
        square_expected = basic_square

        square_small = utils.coord_extend(coords=basic_square, feet_expand=10)
        square_small_expected = [[-3.270378546316736e-05, 0.0], [-3.270378546316736e-05, 1.0000327037854633], [1.0000327037854633, 1.0000327037854633], [1.0000327037854633, -3.270378546316736e-05], [0.0, -3.270378546316736e-05], [-3.270378546316736e-05, 0.0]]

        square_large = utils.coord_extend(coords=basic_square, feet_expand=100)
        square_large_expected = [[-0.0003270378546316736, 0.0], [-0.0003270378546316736, 1.0003270378546316], [1.0003270378546316, 1.0003270378546316], [1.0003270378546316, -0.0003270378546316736], [0.0, -0.0003270378546316736], [-0.0003270378546316736, 0.0]]

        triangle = utils.coord_extend(coords=basic_triangle, feet_expand=0)
        triangle_expected = basic_triangle

        triangle_small = utils.coord_extend(coords=basic_triangle, feet_expand=10)
        triangle_small_expected = [[1.0000327037854633, 1.0], [1.0000327037854633, -3.2703785463272794e-05], [-7.89539224061997e-05, -3.2703785463272794e-05], [0.9999768749315285, 1.0000231250684715], [1.0000327037854633, 1.0]]

        triangle_large = utils.coord_extend(coords=basic_triangle, feet_expand=100)
        triangle_large_expected = [[1.0003270378546316, 1.0], [1.0003270378546316, -0.0003270378546316177], [-0.0007895392240611088, -0.0003270378546316177], [0.9997687493152853, 1.0002312506847149], [1.0003270378546316, 1.0]]

        self.assertEqual(square, square_expected)
        self.assertEqual(square_small, square_small_expected)
        self.assertEqual(square_large, square_large_expected)

        self.assertEqual(triangle, triangle_expected)
        self.assertEqual(triangle_small, triangle_small_expected)
        self.assertEqual(triangle_large, triangle_large_expected)
