class ListOperations:
    def __init__(self, initial_list=None):
        # Initialize the list with the provided list or an empty list
        if initial_list is None:
            initial_list = []
        self.list = initial_list

    def append(self, item):
        self.list.append(item)
        print(f"After append({item}): {self.list}")

    def extend(self, items):
        self.list.extend(items)
        print(f"After extend({items}): {self.list}")

    def insert(self, index, item):
        self.list.insert(index, item)
        print(f"After insert({index}, {item}): {self.list}")

    def remove(self, item):
        try:
            self.list.remove(item)
            print(f"After remove({item}): {self.list}")
        except ValueError:
            print(f"{item} not found in the list")

    def pop(self, index=None):
        if index is None:
            item = self.list.pop()
        else:
            item = self.list.pop(index)
        print(f"After pop({index}): {self.list} | Popped item: {item}")

    def clear(self):
        self.list.clear()
        print(f"After clear(): {self.list}")

    def index(self, item):
        try:
            idx = self.list.index(item)
            print(f"Index of {item}: {idx}")
        except ValueError:
            print(f"{item} not found in the list")

    def count(self, item):
        count = self.list.count(item)
        print(f"Count of {item}: {count}")

    def sort(self, reverse=False):
        self.list.sort(reverse=reverse)
        print(f"After sort(reverse={reverse}): {self.list}")

    def reverse(self):
        self.list.reverse()
        print(f"After reverse(): {self.list}")

    def copy(self):
        new_list = self.list.copy()
        print(f"After copy(): {new_list}")
        return new_list

    def __str__(self):
        return str(self.list)


# Example Usage
list_ops = ListOperations([1, 2, 3, 4])

list_ops.append(5)
list_ops.extend([6, 7])
list_ops.insert(2, 10)
list_ops.remove(3)
list_ops.pop(1)
list_ops.clear()
list_ops.index(10)  # Example to show error handling
list_ops.count(2)
list_ops.sort(reverse=True)
list_ops.reverse()
list_ops.copy()

print('''\nExplanation of List Methods Demonstrated:\n
append(item): Adds an item to the end of the list.\n
extend(items): Extends the list by appending all the items from the iterable.\n
insert(index, item): Inserts an item at a specific position.\n
remove(item): Removes the first occurrence of the item from the list.\n
pop(index=None): Removes and returns the item at the given index. If no index is provided, it removes and returns the last item.\n
clear(): Removes all items from the list.\n
index(item): Returns the index of the first occurrence of the item.\n
count(item): Returns the number of occurrences of the item in the list.\n
sort(reverse=False): Sorts the list in ascending or descending order.\n
reverse(): Reverses the elements of the list in place.\n
copy(): Returns a shallow copy of the list.''')
