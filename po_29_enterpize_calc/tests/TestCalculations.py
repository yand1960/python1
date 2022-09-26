from unittest import TestCase
from po_29_enterpize_calc.buslog.calculations import Calculations

class TestCalculations(TestCase):

    def setUp(self) -> None:
        self.calculations = Calculations("../../data/calc.csv")

    def test_plus(self):
        result = self.calculations.plus(3, 4)
        self.assertEqual(7, result)
