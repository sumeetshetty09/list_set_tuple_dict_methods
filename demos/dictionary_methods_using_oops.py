class DictOperations:
    def __init__(self, initial_dict=None):
        # Initialize the dictionary with the provided dictionary or an empty dictionary
        if initial_dict is None:
            initial_dict = {}
        self.dictionary = initial_dict

    def add(self, key, value):
        self.dictionary[key] = value
        print(f"After add({key}: {value}): {self.dictionary}")

    def remove(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            print(f"After remove({key}): {self.dictionary}")
        else:
            print(f"{key} not found in the dictionary")

    def get(self, key, default=None):
        value = self.dictionary.get(key, default)
        print(f"Get value for {key}: {value}")
        return value

    def update(self, other_dict):
        self.dictionary.update(other_dict)
        print(f"After update({other_dict}): {self.dictionary}")

    def pop(self, key, default=None):
        value = self.dictionary.pop(key, default)
        print(f"After pop({key}): {self.dictionary} | Popped value: {value}")
        return value

    def popitem(self):
        if self.dictionary:
            key, value = self.dictionary.popitem()
            print(f"After popitem(): {self.dictionary} | Popped item: {key}: {value}")
            return key, value
        else:
            print("Dictionary is empty")
            return None

    def keys(self):
        keys = self.dictionary.keys()
        print(f"Keys: {keys}")
        return keys

    def values(self):
        values = self.dictionary.values()
        print(f"Values: {values}")
        return values

    def items(self):
        items = self.dictionary.items()
        print(f"Items: {items}")
        return items

    def clear(self):
        self.dictionary.clear()
        print(f"After clear(): {self.dictionary}")

    def copy(self):
        new_dict = self.dictionary.copy()
        print(f"After copy(): {new_dict}")
        return new_dict

    def __str__(self):
        return str(self.dictionary)


# Example Usage
dict_ops = DictOperations({'a': 1, 'b': 2, 'c': 3})

dict_ops.add('d', 4)
dict_ops.remove('b')
dict_ops.get('a')
dict_ops.update({'e': 5, 'f': 6})
dict_ops.pop('c')
dict_ops.popitem()
dict_ops.keys()
dict_ops.values()
dict_ops.items()
dict_ops.clear()

# Copying the dictionary
copied_dict = dict_ops.copy()

print('''\nExplanation of Dictionary Operations Demonstrated:\n
add(key, value): Adds a new key-value pair to the dictionary. If the key already exists, it updates the value.\n
remove(key): Removes the key-value pair with the specified key. If the key doesn't exist, it prints a message.\n
get(key, default=None): Returns the value associated with the key. If the key doesn't exist, it returns the default value (or None if not specified).\n
update(other_dict): Updates the dictionary with key-value pairs from another dictionary other_dict.\n
pop(key, default=None): Removes the key-value pair for the given key and returns the value. If the key doesn't exist, it returns the default value.\n
popitem(): Removes and returns an arbitrary key-value pair from the dictionary. If the dictionary is empty, it returns None.\n
keys(): Returns a view object containing all the keys of the dictionary.\n
values(): Returns a view object containing all the values in the dictionary.\n
items(): Returns a view object containing all the key-value pairs (tuples) in the dictionary.\n
clear(): Removes all key-value pairs from the dictionary.\n
copy(): Returns a shallow copy of the dictionary.\n
You can interact with an object of the DictOperations class to demonstrate these dictionary methods and how they modify or retrieve data from the dictionary.''')
