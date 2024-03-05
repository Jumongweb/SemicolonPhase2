from unittest import TestCase
from letter_counter import *

class Test(TestCase):
    def test_count_letter(self):
        letter_and_digit = countLetter("hello world! 123")
        expected = 'LETTERS 10 DIGITS 3'
        self.assertEqual(expected, letter_and_digit)

    def test_count_upper_lower_case(self):
        sentence = {"UPPER CASE": 1, "LOWER CASE": 9}
        output = upper_and_lower_case("Hello world!")
        self.assertEqual(sentence, output)
