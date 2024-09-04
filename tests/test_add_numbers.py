import unittest
from src.add_numbers import add_numbers_in_string, NegativeNumberException


class TestAddNumbersInString(unittest.TestCase):

    def test_single_integer(self):
        self.assertEqual(add_numbers_in_string("123"), 123)

    def test_multiple_integers(self):
        self.assertEqual(add_numbers_in_string("12 and 34"), 46)

    def test_negative_numbers_raise_exception(self):
        with self.assertRaises(NegativeNumberException) as context:
            add_numbers_in_string("-1 and 99")
        self.assertIn('-1', str(context.exception))

    def test_float_numbers_excluded(self):
        self.assertEqual(add_numbers_in_string("1.5 and 2.3 and 100"), 100)

    def test_exponential_numbers(self):
        self.assertEqual(add_numbers_in_string("2e3 and 3e2"), 2300)  # 2e3 = 2000, 3e2 = 300

    def test_mixed_numbers_raise_exception(self):
        with self.assertRaises(NegativeNumberException) as context:
            add_numbers_in_string("5, -7; 3.14 and 8, 1e2")
        self.assertIn('-7', str(context.exception))

    def test_various_delimiters(self):
        self.assertEqual(add_numbers_in_string("1;2|3,4/5"), 15)

    def test_no_numbers(self):
        self.assertEqual(add_numbers_in_string("No numbers here!"), 0)

    def test_empty_string(self):
        self.assertEqual(add_numbers_in_string(""), 0)

    def test_numbers_with_text(self):
        self.assertEqual(add_numbers_in_string("There are 4 apples and 5 oranges"), 9)

    def test_large_numbers(self):
        self.assertEqual(add_numbers_in_string("1000000 and 2000000"), 3000000)



class TestAddNumbersInStringErrors(unittest.TestCase):

    def test_non_string_input(self):
        with self.assertRaises(ValueError):
            add_numbers_in_string(12345)

    def test_null_input(self):
        with self.assertRaises(ValueError):
            add_numbers_in_string(None)

    def test_list_input(self):
        with self.assertRaises(ValueError):
            add_numbers_in_string([1, 2, 3])

    def test_dict_input(self):
        with self.assertRaises(ValueError):
            add_numbers_in_string({'key': 'value'})


if __name__ == '__main__':
    unittest.main()
