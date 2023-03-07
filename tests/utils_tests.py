import unittest
import data_retriever

class UtilsTests(unittest.TestCase):

    def test_time_to_millis(self):
        input = "1:38.101"
        result = data_retriever.time_to_float(input)
        expected = 101 + 38*1000 + 1*60*1000
        self.assertEqual(expected, result)

    def test_time_to_millis_no_minutes(self):
        input = "38.101"
        result = data_retriever.time_to_float(input)
        expected = 101 + 38*1000
        self.assertEqual(expected, result)

    def test_time_to_millis_no_millis(self):
        input = "1:38"
        result = data_retriever.time_to_float(input)
        expected = 1*60*1000 + 38*1000
        self.assertEqual(expected, result)

    def test_millis_to_time_str(self):
        input = 1*60*1000 + 38*1000 + 25
        expected = "1:38.025"
        result = data_retriever.float_to_time(input)
        self.assertEqual(expected, result)

    def test_millis_to_time_str_round_value(self):
        input = 95000
        expected = "1:35"
        result = data_retriever.float_to_time(input)
        self.assertEqual(expected, result)