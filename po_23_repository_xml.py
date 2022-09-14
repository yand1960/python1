# Репозиторий, работающий с хранилищем списка товаров в xml-файлы

import xml.etree.ElementTree as ET
from typing import List

# Класс-сущность, описывающий единицу товара
class Product:

    def __init__(self, id: int, name: str, code: str, price: float):
        self.id = id
        self.name = name
        self.code = code
        self.price = price

    def __str__(self):
        return self.__dict__.__str__()

# собственно репозиторий
class ProductXMLRepository:

    # конструктор обращащается в xml-хранилищу
    # и представляет данные о товарах
    # в виде списка объектов-сущностей (self.products)
    def __init__(self, store_path):

        with open(store_path, encoding="utf-8") as f:
            text = f.read()
        products_xml = ET.fromstring(text)
        self.products = []
        for p in products_xml.findall("Product"):
            id = int(p.find("ProductID").text)
            name = p.find("Name").text
            code = p.find("ProductNumber").text
            price = float(p.find("ListPrice").text)
            self.products.append(Product(id, name, code, price))

    # получение сущности по ID - обычная вещь репозитории
    def getbyid(self, id: int) -> Product:
        #   реализуйте в одну строку кода (10:40)
        return list(filter(lambda p: p.id == id, self.products))[0]

    # не обязательные, но полезные дополнительные методы в репозитории
    def findbyfirstletters(self, letters) -> List[Product]:
        #  реализуйте в одну строку кода (10:50)
        return list(filter(lambda p: p.name.lower().startswith(letters.lower()), self.products))


if __name__ == "__main__":
    repository = ProductXMLRepository("data/Products.xml")
    for p in repository.products:
        print(f"{p.name} - ${p.price}")
    print(repository.getbyid(321))

    filtered = repository.findbyfirstletters("aw")
    for p in filtered:
        print(p)

