import unittest

from string_calculator import StringCalculator
class StringCalculatorTests(unittest.TestCase):
    def test_empty_string(self):
        sc = StringCalculator()
        self.assertEqual(sc.add(""),0)

    def test_simple_string_with_two_numbers(self):
        sc = StringCalculator()
        self.assertEqual(sc.add("2,3"),5)
    
    def test_simple_string_with_more_than_two_numbers(self):
        sc = StringCalculator()
        self.assertEqual(sc.add("2,3,5"),10)

if __name__ == '__main__':
    unittest.main()