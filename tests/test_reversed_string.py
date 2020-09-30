from test_task.reverse_string import reverse_string as rs
import unittest


class TestReverseString(unittest.TestCase):
    def test_reverse(self):
        input_string = 'Beautiful is better than ugly'
        self.assertEqual(rs(input_string), ['ugly', 'than', 'better', 'is', 'Beautiful'])
