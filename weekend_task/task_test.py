import unittest
import task


class MyTestCase(unittest.TestCase):
    def test_to_duplicate_items_the_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        output = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
        self.assertEqual(output, task.task2(my_list))  # add assertion here

    def test_to_remove_duplicate(self):
        sample = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]
        output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(output, task.task3(sample))

    def test_that_my_function_can_sum_every_third_element_on_the_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        output = 45
        self.assertEqual(output, task.task4(my_list))

    def test_that_my_list_can_add_the_first_middle_and_last_element(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        output = 24
        self.assertEqual(output, task.task5(my_list))

if __name__ == '__main__':
    unittest.main()
