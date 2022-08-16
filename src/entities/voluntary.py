from category import Category

class Voluntary(Category):
    def __init__(self, name, district, city, state):
        super().__init__(name)

        self._district = district
        self._city = city
        self._state = state
