from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import list_item

class Employee(Category):
    def __init__(self, rg, cpf, role):
        super().__init__(CategoryType.EMPLOYEE)

        self._rg = rg
        self._cpf = cpf
        self._role = role

    def show_info(self):
        list_item("RG", self._rg)
        list_item("CPF", self._cpf)
        list_item("Cargo profissional", self._role)
