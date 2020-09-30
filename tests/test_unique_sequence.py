import unittest
from test_task.unique_sequence import unique_sequence as us


class TestUniqueSequence(unittest.TestCase):
    def test_incorrect_input(self):
        list_of_numbers = [1, 2, 3, 4]
        self.assertEqual(us(list_of_numbers), f'последовательность {set(list_of_numbers)} уникальна')

    def test_not_unique_sequence(self):
        list_of_numbers = [1, 1, 1, 1, 1, 1]
        self.assertEqual(us(list_of_numbers), 'последовательность не уникальна')
