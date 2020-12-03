def return_max(lst, highest=None):
    """Use recursion to return highest number in list."""
    if highest is None and len(lst) > 0:
        highest = lst[0]
    if len(lst) <= 1:
        return highest
    highest = max(highest, lst[0])
    return return_max(lst[1:], highest)

print(return_max([5, 8, -1, 22, 1]))
