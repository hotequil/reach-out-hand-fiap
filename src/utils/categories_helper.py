from enums.category_number import CategoryNumber

category_numbers_list = [category_number.value for category_number in CategoryNumber]

def is_valid_category_number(category_number):
    return category_number in category_numbers_list
