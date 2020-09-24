from test_task.even_numbers import even_numbers as ev
import unittest


class TestSimple(unittest.TestCase):
    def test_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7]
        self.assertIsInstance(ev(test_list), list)

    def test_int(self):
        test_list = [1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(ev(test_list), int)

    def test_even(self):
        test_list = [1, 2, 3, 4, 5, 6, 7]
        for number in ev(test_list):
            self.assertTrue(number % 2 == 0)

    def test_257_number(self):
        test_list = [1, 2, 3, 4, 5, 6, 257, 12, 25, 14]
        self.assertTrue(ev(test_list), None)