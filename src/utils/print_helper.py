small_break_line = "\n"
break_line = f"{small_break_line}{small_break_line}"

def print_space():
    print("")

def print_bar():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def print_bar_top():
    print_bar()
    print_space()

def print_bar_bottom():
    print_space()
    print_bar()

def print_title_top(title):
    print(title)
    print_space()

def print_title_bottom(title):
    print_space()
    print(title)

def print_title_both(title):
    print_space()
    print(title)
    print_space()
