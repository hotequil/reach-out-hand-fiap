from category import Category
from src.enums.category_type import CategoryType

class Donor(Category):
    def __init__(self, blood_type, gift_to_donate, height):
        super().__init__(CategoryType.DONOR)

        self._blood_type = blood_type
        self._gift_to_donate = gift_to_donate
        self._height = height
