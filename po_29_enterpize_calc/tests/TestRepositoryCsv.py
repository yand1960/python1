from unittest import TestCase
from po_29_enterpize_calc.dal.repository_csv import RepositoryCsv


class TestRepositoryCsv(TestCase):

    def test_add(self):
        path = "../../data/calc.csv"

        with open(path, encoding="utf-8") as f:
            lines_start = len(f.read().split("\n"))

        repository = RepositoryCsv(path)
        repository.add(1, 2, 3)

        with open(path, encoding="utf-8") as f:
            lines = f.read().split("\n")
            lines_final = len(lines)
            last_line = lines[-2]

        self.assertEqual(lines_start + 1, lines_final)
        self.assertTrue(last_line.startswith("1;2;3"))