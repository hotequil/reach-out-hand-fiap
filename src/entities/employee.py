from category import Category

class Employee(Category):
    def __init__(self, name, rg, cpf, role):
        super().__init__(name)

        self._rg = rg
        self._cpf = cpf
        self._role = role
