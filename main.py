import display
from data import *


def add_new_item():
    while True:
        display.show_message('name your item: ')
        name = input()
        if len(name) <= 15:
            break
        display.show_message('Name can be only 20 characters long!')
    while True:
        display.show_message('Type in item description: ')
        description = input()
        if len(description) <= 150:
            break
        display.show_message('Description can be max. 150 characters long!')
    new_item = Item(name, description)
    return new_item


def edit_item(item_list, edit_value, index_range):
    display.show_message('Type in index of item you want to edit: ')
    item_index = get_index_input(index_range)

    if edit_value == 'description':
        is_title = False
        max_value_length = 150

    else:
        is_title = True
        max_value_length = 20

    while True:
        display.show_message('Type in new ' + edit_value )
        new_value = input()

        if len(new_value) <= max_value_length:
            break
        else:
            display.show_message(edit_value + ' too long! Max length: ' + str(max_value_length))

    item_list[item_index].modify_item(new_value, is_title)


def get_index_input(index_range):
    MIN_INDEX = 0
    INDEX_TO_LEN_DIFFER = 1

    while True:
        try:
            index = int(input())
            if index > index_range - INDEX_TO_LEN_DIFFER or index < MIN_INDEX:
                display.show_message('Index out of range!')
                continue
            break

        except ValueError:
            display.show_message('Wrong index!')
            continue

    return index


def main():
    item_list = ItemList()
    menu_options = ['Exit', 'Add new item', 'Delete item', "Modify item's description", "Modify item's name",
                    'Mark item as done', 'Show items', 'Show specific item']
    while True:
        index_range = len(item_list)
        option = input()

        if option == '1':
            new_item = add_new_item()
            item_list.add_item(new_item)

        elif option == '2':
            pass

        elif option == '3':
            edit_item(item_list, 'description', index_range)

        elif option == '4':
            edit_item(item_list, 'title', index_range)

        elif option == '5':
            display.show_message('Type in index of item you want to mark as done: ')
            item_index = get_index_input(index_range)
            item_list[item_index].mark_as_done()

        elif option == '6':
            pass

        elif option == '7':
            pass

        elif option == '0':
            pass

        else:
            pass

if __name__ == '__main__':
    main()