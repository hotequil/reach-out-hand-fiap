from .category import Category
from enums.category_type import CategoryType
from utils.print_helper import show_info

class Visitor(Category):
    def __init__(self, genre, has_allergies, is_married):
        super().__init__(CategoryType.VISITOR)

        self._genre = genre
        self._has_allergies = has_allergies
        self._is_married = is_married

    def show_info(self):
        show_info("Gênero", self._genre)
        show_info("Tem alergia", self._has_allergies)
        show_info("É casado", self._is_married)
