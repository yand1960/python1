import unittest
import po_08_functions


class TestModulePO08(unittest.TestCase):

    def test_plus(self):
        x = [1, 2, 3, 4, 5, 6]
        y = [2, 3, 4, 5, 8, 7]
        tax = [0.1, 0, 0, 0.1, 0.1, 0]
        expected = [2.7, 5, 7, 8.1, 11.7, 13]
        for i in range(0, len(x)):
            result = po_08_functions.plus(x[i], y[i], tax[i])
            # self.assertEqual(expected[i], result)
            self.assertAlmostEqual(expected[i], result, 6)
            # if abs(result - expected[i]) < 0.000001:
            #     self.assertTrue(True)
            # else:
            #     self.assertFalse(True)

    def test_minus(self):
        x = 1
        y = 2
        result = po_08_functions.minus(x, y)
        expected = -1
        self.assertEqual(expected, result)

