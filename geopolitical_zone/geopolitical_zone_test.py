import unittest
from geopolitical_zone import GeopoliticalZone


class MyTestCase(unittest.TestCase):
    def test_ThatOyoIsFromSouthWest(self):
        self.assertEqual(GeopoliticalZone.SOUTH_WEST, GeopoliticalZone.get_zone("Oyo"))

    def test_ThatKogiIsFromNorthCentral(self):
        self.assertEqual(GeopoliticalZone.NORTH_CENTRAL, GeopoliticalZone.get_zone("niger"))

    def test_ThatAdamawaIsFromNorthEast(self):
        self.assertEqual(GeopoliticalZone.NORTH_EAST, GeopoliticalZone.get_zone("Adamawa"))

    def test_ThatYobeIsFromNorthWest(self):
        self.assertEqual(GeopoliticalZone.NORTH_WEST, GeopoliticalZone.get_zone("Jigawa"))

    def test_ThatBayelsaIsFromSouthSouth(self):
        self.assertEqual(GeopoliticalZone.SOUTH_SOUTH, GeopoliticalZone.get_zone("Bayelsa"))

    def test_ThatEbonyiIsFromSouthEast(self):
        self.assertEqual(GeopoliticalZone.SOUTH_EAST, GeopoliticalZone.get_zone("Ebonyi"))

if __name__ == '__main__':
    unittest.main()
