class Item:
    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def modify_item(self, new_value, is_name=False):
        if is_name:
            self.name = new_value
        else:
            self.description = new_value

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        return self.name + "\n" + self.description + "\n"


class ItemList:
    def __init__(self):
        self.item_list = []

    def __getitem__(self, item_id):
        return self.item_list[item_id]

    def __len__(self):
        return len(self.item_list)

    def add_item(self, item):
        self.item_list.append(item)

    def delete_item(self, item_id):
        self.item_list.pop(item_id)

    def __str__(self):
        string = ""
        for item in self.item_list:
            string += str(self.item_list.index(item)) + "\n" + item.name + "\n\n"
        return string
