from category import Category
from src.enums.category_type import CategoryType

class Served(Category):
    def __init__(self, salary, children_quantity, is_employed):
        super().__init__(CategoryType.SERVED)

        self._salary = salary
        self._children_quantity = children_quantity
        self._is_employed = is_employed
