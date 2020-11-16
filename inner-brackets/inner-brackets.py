"""
Return a list of text in the most inner bracket.

    >>> inner_bracket('{{()}}{d{d[hi]}}')
    ['', 'hi']
    >>> inner_bracket("hello")
    ['hello']
"""
def inner_bracket(string):
    outers = ('(', '{', '[')
    inners = (')', '}', ']')
    outer_count = 0
    current_str = ""
    final_list = []
    max_len = 0
    for i in range(len(string)):
        if string[i] in outers:
            outer_count += 1
            current_str = ""
        elif string[i] in inners:
            if outer_count > max_len:
                final_list = [current_str]
                max_len = outer_count
            elif outer_count == max_len:
                final_list.append(current_str)
            else:
                pass
            current_str= ""
            outer_count -= 1
        else:
            current_str += string[i]
    
    if max_len == 0:
        return [string]
    return final_list


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
