from category import Category
from src.enums.category_type import CategoryType

class Voluntary(Category):
    def __init__(self, district, city, state):
        super().__init__(CategoryType.VOLUNTARY)

        self._district = district
        self._city = city
        self._state = state
