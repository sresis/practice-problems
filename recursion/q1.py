def print_list(lst):
    """print each element in list recursively."""
    if lst == []:
        return
    print(lst[0])
    print_list(lst[1:])

print_list([3, 2, 1])
