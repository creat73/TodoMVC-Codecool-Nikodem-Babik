def show_message(string):
    print(string)


def show_menu_options(menu_options):
    print('Options: ')
    for option in menu_options:
        print(menu_options.index(option), option)


def show_item_list(items):
    print('Current item list: ')
    print(items)


def show_specific_item(item_id, item_string):
    print(str(item_id) + '\n' + item_string)


def show_exit_message():
    print('Thanks for using the program!')
