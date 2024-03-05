import unittest
from seven_seg import SevenSegmentDisplay


class MyTestCase(unittest.TestCase):
    def test_thatExceptionIsThrowIfIEnterMoreThanEightSwitch(self):
        seven_seg = SevenSegmentDisplay("100001010111")
        with self.assertRaises(ValueError) as error:
            seven_seg.insert_in_a_list()

    def test_thatExceptionIsThrowIfIEnterLessThanEightSwitch(self):
        seven_seg = SevenSegmentDisplay("111")
        with self.assertRaises(ValueError) as error:
            seven_seg.insert_in_a_list()

    def test_thatIfICannotEnterAString(self):
        seven_seg = SevenSegmentDisplay("string")
        with self.assertRaises(ValueError) as error:
            seven_seg.insert_in_a_list()

    def test_mySwitchWillAcceptValidInput(self):
        seven_seg = SevenSegmentDisplay("11101111")
        self.assertTrue(seven_seg)
