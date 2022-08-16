from category import Category
from src.enums.category_type import CategoryType

class Employee(Category):
    def __init__(self, rg, cpf, role):
        super().__init__(CategoryType.EMPLOYEE)

        self._rg = rg
        self._cpf = cpf
        self._role = role
