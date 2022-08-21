from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import list_item

class Visitor(Category):
    def __init__(self, genre, has_allergies, is_married):
        super().__init__(CategoryType.VISITOR)

        self._genre = genre
        self._has_allergies = has_allergies
        self._is_married = is_married

    def show_info(self):
        list_item("Gênero", self._genre)
        list_item("Tem alergia", self._has_allergies)
        list_item("É casado", self._is_married)
