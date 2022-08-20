from utils.print_helper import print_title_top, double_break_line, break_line, print_bar_top, print_title_bottom, print_bar_bottom, print_title_both
from enums.setup_option import SetupOption
from factories.person import create_person

def init():
    print_title_top("Bem-vindo ao menu do sistema de cadastro da ONG Estenda à Mão!")
    print_bar_top()

    stop = False

    while not stop:
        option = int(input(f"Escolha uma das seguintes opções abaixo: {double_break_line}0) Sair do sistema; {break_line}1) Cadastrar pessoa; {double_break_line}Resposta: "))

        if option == SetupOption.STOP_SYSTEM.value: stop = True
        elif option == SetupOption.ADD_PERSON.value: create_person()
        else:
            print_title_both("Você digitou uma opção inválida, tente novamente")
            print_bar_top()

    print_bar_bottom()
    print_title_bottom("Muito obrigado e volte sempre!")
