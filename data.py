class Item:
    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done


class ItemList:
    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)