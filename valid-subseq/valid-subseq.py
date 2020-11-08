"""Determine if valid subseq

For example::

   >>> valid_subseq([4, 6, 8, 10], [8, 4])
   False
   >>> valid_subseq([6, 8, 4, 8], [4, 8])
   True

"""


def valid_subseq(arr, subseq):
    arr_idx = 0
    subseq_idx = 0
    while arr_idx < len(arr) and subseq_idx < len(subseq):
        if subseq[subseq_idx] == arr[arr_idx]:
            subseq_idx += 1
        arr_idx += 1

    return subseq_idx == len(subseq)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
