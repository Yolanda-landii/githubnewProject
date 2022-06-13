import unittest
import FizzBuzz


class test_FizzBuzz(unittest.TestCase):
    def test_FizzBuzz(self):
        expected_output="Buzz"
        assert FizzBuzz.Process(20)==expected_output

if __name__ == " __main__ ":
    unittest.main()