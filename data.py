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


class ItemList:
    def __init__(self):
        self.item_list = []

    def __getitem__(self, index):
        return self.item_list[index]

    def __len__(self):
        return len(self.item_list)

    def add_item(self, item):
        self.item_list.append(item)