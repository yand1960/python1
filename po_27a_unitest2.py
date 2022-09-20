from unittest import TestCase
from po_23_repository_xml import Product, ProductXMLRepository


class TestProductXMLRepository(TestCase):

    def setUp(self):
        self.repository = ProductXMLRepository("data/ProductsTest.xml")

    def test_products(self):
        products = self.repository.products
        self.assertEqual(471, len(products))




