from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import show_info

class Voluntary(Category):
    def __init__(self, district, city, state):
        super().__init__(CategoryType.VOLUNTARY)

        self._district = district
        self._city = city
        self._state = state

    def show_info(self):
        show_info("Bairro", self._district)
        show_info("Cidade", self._city)
        show_info("Estado", self._state)
