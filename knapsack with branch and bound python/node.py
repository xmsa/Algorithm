# class to represent a node in the tree
class node:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value
        self.ub = 0
        self.selected_items = []
    
    @property
    def selected_items(self):
        return self.__selected_items
    @selected_items.setter
    def selected_items(self, selected_items):
        self.__selected_items = selected_items.copy()

    def print(self, items):
        # s = "*"*50 + "\n"
        for i in range(len(self.selected_items)):
            _str =  f'item "{self.selected_items[i]}":' 
            _str += f'weight = {items[self.__selected_items[i]][0]}, '
            _str += f'value = {items[self.selected_items[i]][1]}'
            print(f"{_str:^50s}")

        _str = f"total weight = {self.weight}"
        print(f"{_str:^50s}")

        _str = f"total value = {self.value}"
        print(f"{_str:^50s}")

        print("*"*50)
