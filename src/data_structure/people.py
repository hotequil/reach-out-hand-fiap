from operator import attrgetter
from utils.print_helper import print_title_both, print_space, normal_error, print_bar_bottom, question, print_bar_top, print_title_bottom, separate_items, list_item

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

    def list(self):
        print_bar_bottom()
        print_title_both("# Lista de pessoas ordenadas por nome e categorias")

        if self._root is not None: self._list(self._root)
        else: normal_error("Não existem pessoas cadastradas ainda, cadastre uma e ela aparecerá aqui!")

        print_bar_bottom()
        print_space()

    def search(self):
        print_bar_bottom()
        print_title_both("# Buscar pessoa por nome")

        full_name = question("Digite o nome completo da pessoa que você deseja buscar: ")
        value = { 'comparisons': 0, 'found_person': None }

        if self._root is not None: value = self._search(full_name, value['comparisons'], self._root)

        found_person = value['found_person']

        print_title_bottom("1) Sobre a busca")
        list_item("Número de comparações feitas", value['comparisons'])
        print_title_bottom("2) Sobre a pessoa")

        if found_person is None: list_item("Nenhuma pessoa foi encontrada com o nome de", full_name)
        else:
            list_item("Nome completo", found_person.full_name)
            list_item("Data de nascimento", found_person.birth_date)
            list_item("Telefone", found_person.phone)
            list_item("Email", found_person.email)
            list_item("Categorias", separate_items(found_person.categories))

            for value in found_person.data:
                value[1].show_info()

        print_title_both("Busca terminada e dados exibidos, iremos levar você para o menu.")
        print_bar_top()

    def _add(self, person, node):
        people = [person, node.person]
        ordered_people = sorted(people, key=attrgetter('full_name', 'categories'))
        ordered_people = sorted(ordered_people, key=lambda current_person: current_person.full_name.lower())
        first_ordered_person = ordered_people[0]

        if first_ordered_person is person:
            if node.left is None: node.left = _PersonNode(person)
            else: self._add(person, node.left)
        else:
            if node.right is None: node.right = _PersonNode(person)
            else: self._add(person, node.right)

    def _list(self, node):
        if node is not None:
            person = node.person

            self._list(node.left)
            print(f"- {person.full_name} (categorias: {separate_items(person.categories)})")
            self._list(node.right)

    def _search(self, full_name, comparisons, node):
        person = node.person
        node_full_name = person.full_name
        ordered_full_names = sorted([full_name, node_full_name])
        first_full_name = ordered_full_names[0]
        has_node_left = node.left is not None
        has_node_right = node.right is not None
        first_full_name_is_full_name = first_full_name == full_name

        comparisons += 1

        if full_name == node_full_name: return { 'comparisons': comparisons, 'found_person': person }

        comparisons += 1

        if first_full_name_is_full_name and has_node_left: return self._search(full_name, comparisons, node.left)

        # TODO: test with these lines
        # comparisons += 1
        #
        # if first_full_name_is_full_name and has_node_right: return self._search(full_name, comparisons, node.right)
        #
        # comparisons += 1
        #
        # if not first_full_name_is_full_name and has_node_left: return self._search(full_name, comparisons, node.left)

        comparisons += 1

        if not first_full_name_is_full_name and has_node_right: return self._search(full_name, comparisons, node.right)

        return { 'comparisons': comparisons, 'found_person': None }
