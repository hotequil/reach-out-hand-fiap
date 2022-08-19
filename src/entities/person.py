# TODO: set categories and data customized

import re
from enums.category_number import CategoryNumber
from enums.category_type import CategoryType
from utils.print_helper import double_break_line, break_line, question, print_space, normal_error
from utils.categories_helper import is_valid_category_number
from utils.list_helper import has_len

class Person:
    def __init__(self, full_name, birth_date, phone, email):
        self._full_name = full_name
        self._birth_date = birth_date
        self._phone = phone
        self._email = email
        self._categories = []
        self._data = {}

    def add_categories(self):
        print_space()

        separator = ', '
        categories = question(
            f"Por fim, digite separando por vírgulas as categorias de seu desejo para essa nova pessoa (exemplo: {CategoryNumber.EMPLOYEE.value}{separator}{CategoryNumber.VOLUNTARY.value}{separator}{CategoryNumber.VISITOR.value}):"
            f"{double_break_line}{CategoryNumber.EMPLOYEE.value} - {CategoryType.EMPLOYEE.value};"
            f"{break_line}{CategoryNumber.VOLUNTARY.value} - {CategoryType.VOLUNTARY.value};"
            f"{break_line}{CategoryNumber.DONOR.value} - {CategoryType.DONOR.value};"
            f"{break_line}{CategoryNumber.SERVED.value} - {CategoryType.SERVED.value};"
            f"{break_line}{CategoryNumber.VISITOR.value} - {CategoryType.VISITOR.value};"
            f"{double_break_line}Resposta: "
        )

        categories = re.findall('[0-9]+', categories.strip())
        has_value = bool(categories)

        if not has_value:
            print_space()
            normal_error()
            return self.add_categories()

        categories = [category_number for category_number in categories if category_number.isnumeric()]
        categories = list(map(int, categories))
        categories = list(dict.fromkeys(categories))

        if not has_len(categories):
            print_space()
            normal_error()
            return self.add_categories()

        invalid_categories = list(map(str, [category_number for category_number in categories if not is_valid_category_number(category_number)]))

        if has_len(invalid_categories):
            print_space()
            normal_error(f"Tente novamente, você digitou as seguintes categorias inválidas: {separator.join(invalid_categories)}")
            return self.add_categories()

        if (CategoryNumber.SERVED.value in categories) and ((CategoryNumber.EMPLOYEE.value in categories) or (CategoryNumber.DONOR.value in categories)):
            print_space()
            normal_error(f"{CategoryType.EMPLOYEE.value} ou {CategoryType.DONOR.value.lower()} não podem estar em uma pessoa que tem a categoria {CategoryType.SERVED.value.lower()}")
            return self.add_categories()

        # self._categories.append(value)
