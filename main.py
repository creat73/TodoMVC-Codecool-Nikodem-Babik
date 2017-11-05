import display
from data import *


def add_new_item():
    while True:
        display.show_message('name your item: ')
        name = input()
        if len(name) <= 20:
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


def edit_item(item_list, edit_value, id_range):
    display.show_message('Type in id of item you want to edit: ')
    item_id = get_id_input(id_range)

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

    item_list[item_id].modify_item(new_value, is_title)


def get_id_input(id_range):
    MIN_ID = 0
    ID_TO_LEN_DIFFER = 1
    ID_TO_LEN_DIFFER = 1

    while True:
        try:
            item_id = int(input())
            if item_id > id_range - ID_TO_LEN_DIFFER or item_id < MIN_ID:
                display.show_message('id out of range!')
                continue
            break

        except ValueError:
            display.show_message('Wrong id!')
            continue

    return item_id


def main():
    EMPTY_LIST_LENGTH = 0

    item_list = ItemList()
    menu_options = ['Exit', 'Add new item', 'Delete item', "Modify item's description", "Modify item's name",
                    'Mark item as done', 'Show items', 'Show specific item']
    edition_options_id = ['2', '3', '4', '5']

    while True:
        id_range = len(item_list)
        display.show_menu_options(menu_options)
        option = input()

        if id_range == EMPTY_LIST_LENGTH:
            if option in edition_options_id:
                display.show_message("No items to edit/delete!")
                continue

        if option == '1':
            new_item = add_new_item()
            item_list.add_item(new_item)

        elif option == '2':
            display.show_message('Type in id of item you want to delete: ')
            item_id = get_id_input(id_range)
            item_list.delete_item(item_id)

        elif option == '3':
            edit_item(item_list, 'description', id_range)

        elif option == '4':
            edit_item(item_list, 'title', id_range)

        elif option == '5':
            display.show_message('Type in id of item you want to mark as done: ')
            item_id = get_id_input(id_range)
            item_list[item_id].mark_as_done()

        elif option == '6':
            display.show_item_list(str(item_list))

        elif option == '7':
            if id_range == EMPTY_LIST_LENGTH:
                display.show_message('No items to show,')
                continue
            display.show_message('Type in id of item you want to show: ')
            item_id = get_id_input(id_range)
            display.show_specific_item(item_id, str(item_list[item_id]))

        elif option == '0':
            display.show_exit_message()
            exit()

        else:
            pass

if __name__ == '__main__':
    main()