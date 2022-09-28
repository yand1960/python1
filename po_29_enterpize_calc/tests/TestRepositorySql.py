from unittest import TestCase
from po_29_enterpize_calc.dal.repository_sql import RepositorySql

class TestRepositorySql(TestCase):

    def test_add(self):
        repository = RepositorySql("yand.dyndns.org;MyDb;northwind;northwind")
        repository.add(11,22,33)
