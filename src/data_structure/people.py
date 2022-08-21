from operator import attrgetter
from entities.person import Person
from utils.print_helper import print_title_both, print_space, normal_error, print_bar_bottom, question, print_bar_top, print_title_bottom, separate_items, show_info

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
            print(f"- {node.person.full_name} (categorias: {separate_items(node.person.categories)})")
            self._list(node.right)

    def search(self):
        print_bar_bottom()
        print_title_both("# Buscar pessoa por nome")

        full_name = question("Digite o nome completo da pessoa que deseja buscar: ")
        value = { 'comparisons': 0, 'found_person': None }

        if self._root is not None: value = self._search(full_name, value['comparisons'], self._root)

        found_person = value['found_person']

        print_title_bottom("1) Sobre a pesquisa")
        show_info("Número de comparações", value['comparisons'])
        print_title_bottom("2) Sobre a pessoa")

        if found_person is None: show_info("Nenhuma pessoa foi encontrada com o nome de", name)
        else:
            show_info("Nome completo", found_person.full_name)
            show_info("Data de nascimento", found_person.birth_date)
            show_info("Telefone", found_person.phone)
            show_info("Email", found_person.email)
            show_info("Categorias", separate_items(found_person.categories))

            for key, value in found_person.data:
                value.show_info()

        print_title_both("Busca terminada e dados exibidos, iremos levar você para o menu novamente!")
        print_bar_top()

    def _search(self, full_name, comparisons, node):
        node_full_name = node.person.full_name
        ordered_full_names = sorted([full_name, node_full_name])
        first_full_name = ordered_full_names[0]

        comparisons += 1

        if full_name is node_full_name: return { 'comparisons': comparisons, 'found_person': node.person }

        comparisons += 1

        if first_full_name is full_name and node.left is not None: return self._search(full_name, comparisons, node.left)

        comparisons += 1

        if first_full_name is not full_name and node.right is not None: return self._search(full_name, comparisons, node.right)
