import unittest
from task_1 import TaskOne
from task_1 import Correction


class MyTestCase(unittest.TestCase):
    def test_get_string(self):
        self.assertEqual("hi", TaskOne.get_string(self, "hi"))

    def test_print_string(self):
        console = TaskOne()
        word = console.get_string("hi")
        self.assertEqual("HI", console.printString())
        # self.assertEqual("HI", TaskOne.printString(self, "hi"))

    def test_correction(self):
        console = Correction()
        word = console.get_string("hi")
        self.assertEqual("HI", console.printString())

if __name__ == '__main__':
    unittest.main()