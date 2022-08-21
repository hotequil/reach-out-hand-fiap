from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import list_item

class Donor(Category):
    def __init__(self, blood_type, gift_to_donate, height):
        super().__init__(CategoryType.DONOR)

        self._blood_type = blood_type
        self._gift_to_donate = gift_to_donate
        self._height = height

    def show_info(self):
        list_item("Tipo sanguíneo", self._blood_type)
        list_item("Presente para doação", self._gift_to_donate)
        list_item("Altura", self._height)
