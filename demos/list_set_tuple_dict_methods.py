# List, Set, Tuple, and Dictionary Methods in Python

def list_methods_demo():
    print("\nList Methods: Demonstrates methods like append, extend, insert, remove, pop, index, count, reverse, sort, copy, and clear.")
    my_list = [1, 2, 3, 4, 5, 2]
    print("Original List:", my_list)

    # append
    my_list.append(6)
    print("After append(6):", my_list)

    # extend
    my_list.extend([7, 8])
    print("After extend([7, 8]):", my_list)

    # insert
    my_list.insert(2, 99)
    print("After insert(2, 99):", my_list)

    # remove
    my_list.remove(2)
    print("After remove(2):", my_list)

    # pop
    popped_item = my_list.pop(3)
    print(f"After pop(3) (popped: {popped_item}):", my_list)

    # index
    index_of_5 = my_list.index(5)
    print("Index of 5:", index_of_5)

    # count
    count_of_2 = my_list.count(2)
    print("Count of 2:", count_of_2)

    # reverse
    my_list.reverse()
    print("After reverse:", my_list)

    # sort
    my_list.sort()
    print("After sort:", my_list)

    # copy
    copied_list = my_list.copy()
    print("Copied List:", copied_list)

    # clear
    my_list.clear()
    print("After clear():", my_list)

def set_methods_demo():
    print("\nSet Methods: Covers add, update, remove, discard, pop, union, intersection, difference, symmetric_difference, and clear.")
    my_set = {1, 2, 3, 4}
    print("Original Set:", my_set)

    # add
    my_set.add(5)
    print("After add(5):", my_set)

    # update
    my_set.update([6, 7])
    print("After update([6, 7]):", my_set)

    # remove
    my_set.remove(3)  # Raises KeyError if not found
    print("After remove(3):", my_set)

    # discard
    my_set.discard(10)  # No error if element not found
    print("After discard(10):", my_set)

    # pop
    popped = my_set.pop()
    print(f"After pop() (popped: {popped}):", my_set)

    # union
    set2 = {8, 9}
    print("Union with {8, 9}:", my_set.union(set2))

    # intersection
    print("Intersection with {6, 7, 8}:", my_set.intersection({6, 7, 8}))

    # difference
    print("Difference with {6, 7}:", my_set.difference({6, 7}))

    # symmetric_difference
    print("Symmetric Difference with {6, 7}:", my_set.symmetric_difference({6, 7}))

    # clear
    my_set.clear()
    print("After clear():", my_set)

def tuple_methods_demo():
    print("\nTuple Methods: Only includes count and index because tuples are immutable.")
    my_tuple = (1, 2, 3, 4, 2, 5)
    print("Original Tuple:", my_tuple)

    # count
    count_of_2 = my_tuple.count(2)
    print("Count of 2:", count_of_2)

    # index
    index_of_4 = my_tuple.index(4)
    print("Index of 4:", index_of_4)

def dictionary_methods_demo():
    print("\nDictionary Methods: Includes keys, values, items, get, update, pop, popitem, setdefault, copy, and clear.")
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Original Dictionary:", my_dict)

    # keys
    print("Keys:", my_dict.keys())

    # values
    print("Values:", my_dict.values())

    # items
    print("Items:", my_dict.items())

    # get
    value = my_dict.get('b')
    print("Value for key 'b':", value)

    # update
    my_dict.update({'d': 4, 'e': 5})
    print("After update({'d': 4, 'e': 5}):", my_dict)

    # pop
    popped_value = my_dict.pop('c')
    print(f"After pop('c') (popped: {popped_value}):", my_dict)

    # popitem
    popped_item = my_dict.popitem()
    print(f"After popitem() (popped: {popped_item}):", my_dict)

    # setdefault
    my_dict.setdefault('f', 6)
    print("After setdefault('f', 6):", my_dict)

    # copy
    copied_dict = my_dict.copy()
    print("Copied Dictionary:", copied_dict)

    # clear
    my_dict.clear()
    print("After clear():", my_dict)

if __name__ == "__main__":
    list_methods_demo()
    set_methods_demo()
    tuple_methods_demo()
    dictionary_methods_demo()
