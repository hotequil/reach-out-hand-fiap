from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import show_info

class Served(Category):
    def __init__(self, salary, children_quantity, is_employed):
        super().__init__(CategoryType.SERVED)

        self._salary = salary
        self._children_quantity = children_quantity
        self._is_employed = is_employed

    def show_info(self):
        show_info("Salário", self._salary)
        show_info("Quantidade de filhos", self._children_quantity)
        show_info("Está empregado", self._is_employed)
