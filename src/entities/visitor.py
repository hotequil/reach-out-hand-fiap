from category import Category
from src.enums.category_type import CategoryType

class Visitor(Category):
    def __init__(self, genre, has_allergies, is_married):
        super().__init__(CategoryType.VISITOR)

        self._genre = genre
        self._has_allergies = has_allergies
        self._is_married = is_married
