from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import show_info

class Employee(Category):
    def __init__(self, rg, cpf, role):
        super().__init__(CategoryType.EMPLOYEE)

        self._rg = rg
        self._cpf = cpf
        self._role = role

    def show_info(self):
        show_info("RG", self._rg)
        show_info("CPF", self._cpf)
        show_info("Cargo profissional", self._role)
