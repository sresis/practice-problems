def double_lst(lst, lst2=[]):
    """Return list where all numbers are doubled."""
    if lst == []:
        return lst2
    val = lst[0] * 2
    lst2.append(val)
    return double_lst(lst[1:], lst2)

print(double_lst([2, 3, 5]))