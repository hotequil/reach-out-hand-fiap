from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import show_info

class Donor(Category):
    def __init__(self, blood_type, gift_to_donate, height):
        super().__init__(CategoryType.DONOR)

        self._blood_type = blood_type
        self._gift_to_donate = gift_to_donate
        self._height = height

    def show_info(self):
        show_info("Tipo sanguíneo", self._blood_type)
        show_info("Presente para doação", self._gift_to_donate)
        show_info("Altura", self._height)
