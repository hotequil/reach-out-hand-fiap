from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import list_item

class Voluntary(Category):
    def __init__(self, district, city, state):
        super().__init__(CategoryType.VOLUNTARY)

        self._district = district
        self._city = city
        self._state = state

    def show_info(self):
        list_item("Bairro", self._district)
        list_item("Cidade", self._city)
        list_item("Estado", self._state)
