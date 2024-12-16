class TupleOperations:
    def __init__(self, initial_tuple=None):
        # Initialize the tuple with the provided tuple or an empty tuple
        if initial_tuple is None:
            initial_tuple = ()
        self.tuple = initial_tuple

    def count(self, item):
        count = self.tuple.count(item)
        print(f"Count of {item}: {count}")
        return count

    def index(self, item):
        try:
            idx = self.tuple.index(item)
            print(f"Index of {item}: {idx}")
            return idx
        except ValueError:
            print(f"{item} not found in the tuple")
            return -1

    def concatenate(self, other_tuple):
        result = self.tuple + other_tuple
        print(f"Concatenated tuple: {result}")
        return result

    def repeat(self, times):
        result = self.tuple * times
        print(f"Repeated tuple {times} times: {result}")
        return result

    def slice(self, start, end):
        result = self.tuple[start:end]
        print(f"Sliced tuple from {start} to {end}: {result}")
        return result

    def __str__(self):
        return str(self.tuple)


# Example Usage
tuple_ops = TupleOperations((1, 2, 3, 4))

tuple_ops.count(3)  # Count occurrences of an item
tuple_ops.index(2)  # Find the index of an item
tuple_ops.concatenate((5, 6))  # Concatenate another tuple
tuple_ops.repeat(2)  # Repeat the tuple
tuple_ops.slice(1, 3)  # Slice the tuple

# Trying index with an item that doesn't exist
tuple_ops.index(7)

print('''\nExplanation of Tuple Operations Demonstrated:\n
count(item): Returns the number of occurrences of the specified item in the tuple.\n
index(item): Returns the index of the first occurrence of the specified item in the tuple. If the item doesn't exist, it raises a ValueError.\n
concatenate(other_tuple): Concatenates the current tuple with another tuple and returns the resulting tuple.\n
repeat(times): Repeats the current tuple times times and returns the new tuple.\n
slice(start, end): Returns a sliced version of the tuple from the start index to the end index (not including end).\n
Note that tuples are immutable, so you can't modify them directly like lists. However, you can still demonstrate operations like counting, finding indices, and creating new tuples using operations like concatenation and repetition.''')
