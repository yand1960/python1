# Импорт по относительному пути
# Но он работает только в том случае, если файла запуще не как скрипт,
# а в составе пакета
# from .module1.module11.po_28a_foo import foo # error

# Работопспособный относительный импорт - см. module1\module13\__init__.py
from module1.module13 import foo

print(foo)