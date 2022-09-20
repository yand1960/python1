from unittest import TestCase
from po_23_repository_xml import Product, ProductXMLRepository


class TestProductXMLRepository(TestCase):

    def setUp(self):
        self.repository = ProductXMLRepository("data/ProductsTest.xml")

    def test_products(self):
        products = self.repository.products

        self.assertEqual(471, len(products))

        for p in products:
            self.assertTrue(type(p) is Product)

        p = products[123]
        self.assertEqual(p.id, 478)
        self.assertEqual(p.name, "Metal Bar 2")
        self.assertEqual(p.code, "MB-6061")
        self.assertEqual(p.price, 0.0)

    def test_getbyid(self):
        p = self.repository.getbyid(812)
        self.assertEqual(p.id, 812)
        self.assertEqual(p.name, "ML Road Handlebars")
        self.assertEqual(p.code, "HB-R720")
        self.assertEqual(p.price, 73.75)

    def test_findbyfirstletters(self):
        products = self.repository.findbyfirstletters("f")
        self.assertEqual(len(products), 6)
        p = products[3]
        self.assertEqual(878, p.id)
        self.assertEqual("Fender Set - Mountain", p.name)
        self.assertEqual("FE-6654", p.code)
        self.assertEqual(26.18, p.price)
