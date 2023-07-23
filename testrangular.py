import unittest
from io import StringIO
import sys
import string
from rangular import print_rangoli
from contextlib import redirect_stdout

class TestPrintRangoli(unittest.TestCase):
    def test_print_rangoli(self):
        # Test case 1
        expected_output = """--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
        with StringIO() as buffer, redirect_stdout(buffer):
            print_rangoli(5)
            self.assertEqual(buffer.getvalue(), expected_output)

        # Test case 2
        expected_output = """----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""
        with StringIO() as buffer, redirect_stdout(buffer):
            print_rangoli(3)
            self.assertEqual(buffer.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()