# Собираем вместе то, что изучили до этого

from typing import Iterable, Callable


class ControlledList(list):

    def __init__(self, data: Iterable = [], criteria: Callable[[int], bool] = lambda x: True):
        self._criteria = criteria
        for value in data:
            if not self.criteria(value):
                raise ValueError("передача недопустимых данных")
        super().__init__(data)

    @property
    def criteria(self) -> Callable[[int], bool]:
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        for x in self:
            if not criteria(x):
                raise ValueError("существующие данные не соответствуют критерию")
        self._criteria = criteria

    def append(self, value):
        if self.criteria(value):
            super().append( value)
        else:
            raise ValueError("передача недопустимых данных")

    def __setitem__(self, key, value):
        if self.criteria(value):
            super().__setitem__(key, value)
        else:
            raise ValueError("передача недопустимых данных")

    def __add__(self, other):
        raise NotImplementedError("передача недопустимых данных")


list1 = ControlledList([1,3,5], criteria=lambda x: x < 10)
# list1 = ControlledList()
list1.append(1)
# list2 = [2,4]
# list1 = list1 + list2
# print(list1, type(list1))
print(list1)
list1.criteria = lambda x: x > -10

