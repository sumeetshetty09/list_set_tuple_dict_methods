class SetOperations:
    def __init__(self, initial_set=None):
        # Initialize the set with the provided set or an empty set
        if initial_set is None:
            initial_set = set()
        self.set = initial_set

    def add(self, item):
        self.set.add(item)
        print(f"After add({item}): {self.set}")

    def update(self, items):
        self.set.update(items)
        print(f"After update({items}): {self.set}")

    def remove(self, item):
        try:
            self.set.remove(item)
            print(f"After remove({item}): {self.set}")
        except KeyError:
            print(f"{item} not found in the set")

    def discard(self, item):
        self.set.discard(item)
        print(f"After discard({item}): {self.set}")

    def pop(self):
        item = self.set.pop() if self.set else None
        print(f"After pop(): {self.set} | Popped item: {item}")

    def clear(self):
        self.set.clear()
        print(f"After clear(): {self.set}")

    def copy(self):
        new_set = self.set.copy()
        print(f"After copy(): {new_set}")
        return new_set

    def union(self, other_set):
        result = self.set.union(other_set)
        print(f"Union with {other_set}: {result}")
        return result

    def intersection(self, other_set):
        result = self.set.intersection(other_set)
        print(f"Intersection with {other_set}: {result}")
        return result

    def difference(self, other_set):
        result = self.set.difference(other_set)
        print(f"Difference with {other_set}: {result}")
        return result

    def symmetric_difference(self, other_set):
        result = self.set.symmetric_difference(other_set)
        print(f"Symmetric difference with {other_set}: {result}")
        return result

    def is_subset(self, other_set):
        result = self.set.issubset(other_set)
        print(f"Is subset of {other_set}: {result}")
        return result

    def is_superset(self, other_set):
        result = self.set.issuperset(other_set)
        print(f"Is superset of {other_set}: {result}")
        return result

    def is_disjoint(self, other_set):
        result = self.set.isdisjoint(other_set)
        print(f"Is disjoint with {other_set}: {result}")
        return result

    def __str__(self):
        return str(self.set)


# Example Usage
set_ops = SetOperations({1, 2, 3})

set_ops.add(4)
set_ops.update({5, 6})
set_ops.remove(2)
set_ops.discard(7)  # Example of discarding an item that's not in the set
set_ops.pop()
set_ops.clear()

# Operations with another set
another_set = {3, 4, 7}
set_ops.union(another_set)
set_ops.intersection(another_set)
set_ops.difference(another_set)
set_ops.symmetric_difference(another_set)
set_ops.is_subset({1, 2, 3, 4, 5, 6})
set_ops.is_superset({4, 5})
set_ops.is_disjoint({8, 9})
set_ops.copy()

print('''\nExplanation of Set Methods Demonstrated:\n
add(item): Adds an item to the set. If the item already exists, it doesn't change the set.\n
update(items): Adds multiple items (from another iterable) to the set.\n
remove(item): Removes the specified item from the set. If the item doesn't exist, it raises a KeyError.\n
discard(item): Removes the item from the set if it exists. If not, it does nothing (no error raised).\n
pop(): Removes and returns an arbitrary item from the set. If the set is empty, it returns None.\n
clear(): Removes all items from the set.\n
copy(): Returns a shallow copy of the set.\n
union(other_set): Returns a set containing all elements from the current set and other_set.\n
intersection(other_set): Returns a set containing only the elements that are in both sets.\n
difference(other_set): Returns a set containing elements in the current set but not in other_set.\n
symmetric_difference(other_set): Returns a set containing elements in either of the sets but not in both.\n
is_subset(other_set): Returns True if the current set is a subset of other_set.\n
is_superset(other_set): Returns True if the current set is a superset of other_set.\n
is_disjoint(other_set): Returns True if the current set and other_set have no common elements.''')
