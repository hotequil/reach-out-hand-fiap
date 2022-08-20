from operator import attrgetter
from entities.person import Person
from utils.print_helper import print_title_both, separator, print_space, normal_error, print_bar_bottom

class _PersonNode:
    def __init__(self, person):
        self.person = person
        self.left = None
        self.right = None

class PeopleAvlTree:
    def __init__(self):
        self._root = None

    def add(self, person):
        if self._root is None: self._root = _PersonNode(person)
        else: self._add(person, self._root)

    def _add(self, person, node):
        people = [person, node.person]
        ordered_people = sorted(people, key=attrgetter('full_name', 'categories'))
        first_ordered_person = ordered_people[0]

        if first_ordered_person is person:
            if node.left is None: node.left = _PersonNode(person)
            else: self._add(person, node.left)
        else:
            if node.right is None: node.right = _PersonNode(person)
            else: self._add(person, node.right)

    def list(self):
        print_bar_bottom()
        print_title_both("# Lista de pessoas ordenadas por nome e categorias")

        if self._root is not None: self._list(self._root)
        else: normal_error("Não existem pessoas cadastradas ainda, cadastre uma e ela aparecerá aqui!")

        print_bar_bottom()
        print_space()

    def _list(self, node):
        if node is not None:
            self._list(node.left)
            print(f"- {node.person.full_name} (categorias: {separator.join(node.person.categories)})")
            self._list(node.right)
