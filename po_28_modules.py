# Импорт "вниз" от текущей директории
from module1.module11.po_28a_foo import foo, foo1
from module1.module12.po_28b_arith import Arith
from module1.module13 import foo123

print(foo, foo1())
a = Arith()
print(a.plus(1, 2), a.minus(3, 4), foo123)