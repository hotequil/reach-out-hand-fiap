from utils.print_helper import print_title_top, double_break_line, break_line, print_bar_top, print_title_bottom, print_bar_bottom, print_title_both, print_space, normal_error
from enums.setup_option import SetupOption
from factories.person import create_person
from data_structure.people import PeopleAvlTree

def init():
    print_title_top("Bem-vindo ao menu do sistema de cadastro da ONG Estenda à Mão!")
    print_bar_top()

    people = PeopleAvlTree()
    stop = False

    while not stop:
        print_title_top("# Menu")

        option = input(f"Escolha uma das seguintes opções abaixo: {double_break_line}{SetupOption.STOP_SYSTEM.value}) Sair do sistema; {break_line}{SetupOption.ADD_PERSON.value}) Cadastrar pessoa; {break_line}{SetupOption.LIST_PEOPLE.value}) Listar pessoas ordenadas por nome e categorias; {double_break_line}Resposta: ")

        if option.isnumeric(): option = int(option)

        if option == SetupOption.STOP_SYSTEM.value: stop = True
        elif option == SetupOption.ADD_PERSON.value: people.add(create_person())
        elif option == SetupOption.LIST_PEOPLE.value: people.list()
        else:
            print_space()
            normal_error("Você digitou uma opção inválida, tente novamente!")
            print_space()
            print_bar_top()

    print_bar_bottom()
    print_title_bottom("Muito obrigado e volte sempre!")
