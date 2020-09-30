from test_task.even_numbers import even_numbers as ev
import unittest


class TestSimple(unittest.TestCase):
    def test_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7]
        self.assertIsInstance(ev(test_list), list)

    def test_even_list(self):
        test_list = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(ev(test_list), [2, 4, 6])

    def test_even(self):
        test_list = [1, 2, 3, 4, 5, 6, 7]
        for number in ev(test_list):
            self.assertTrue(number % 2 == 0)

    def test_257_number(self):
        test_list = [1, 2, 3, 4, 5, 6, 257, 12, 25, 14]
        self.assertEqual(ev(test_list), [2, 4, 6])