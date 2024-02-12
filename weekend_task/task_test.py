import unittest
import task

class MyTestCase(unittest.TestCase):
    def test_to_duplicate_items_the_list(self):
        my_list = range(1, 16)
        output = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
        self.assertEqual(output, my_list)  # add assertion here

if __name__ == '__main__':
    unittest.main()
