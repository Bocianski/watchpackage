import unittest
from datetime import datetime


class ClockTest(unittest.TestCase):
    def test_ok(self):
        time = datetime.now()

        string = time.strftime('%H')

        self.assertTrue(string, not None)
        self.assertLessEqual(len(string), 2)
