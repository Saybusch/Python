import unittest
from zad import Kosc

class TestKosc(unittest.TestCase):
    def test_rzutLimits(self):
        obj = Kosc()
        obj.throw()
        self.assertIn(obj.diceValue, range(1, 7))
    def test_notAvailableDataChange(self):
        obj = Kosc()
        before = obj.diceValue
        obj.block()
        self.assertEqual(obj.diceValue, before)