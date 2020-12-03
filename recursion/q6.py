def flatten_list(lst1):
    """flattens list recursively."""
    if lst1 == []:
        return lst1
    if isinstance(lst1[0], list):
        return flatten_list(lst1[0]) + flatten_list(lst1[1:])
    return lst1[:1] + flatten_list(lst1[1:])

print(flatten_list([3, 4,[4, [5, 6], 7], 98]))