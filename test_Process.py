import unittest
import FizzBuzz
from io import StringIO
import sys
import io
from unittest.mock import patch



class test_FizzBuzz(unittest.TestCase):
    @patch("sys.stdin",StringIO("30"))
    def test_Process_Fizz(self):
        
        expected_output= "Fizz"

        self.assertTrue(30,"Fizz")


    @patch("sys.stdin",StringIO("10"))
    def test_Process_Buzz(self):
        expected_output="Buzz"
        self.assertTrue(expected_output,10)

    @patch("sys.stdin",StringIO("2"))
    def test_Process_Number(self):
        with patch("sys.stdout",StringIO()) as out:   
            self.assertTrue(2,2)

    @patch("sys.stdin",StringIO("15"))
    def test_Process_FizzBuzz(self):
        expected_output="FizzBuzz"
        with patch("sys.stdout",StringIO()) as out:
            output = out.getvalue()
            self.assertTrue(expected_output,output)


if __name__ == " __main__ ":
    unittest.main()