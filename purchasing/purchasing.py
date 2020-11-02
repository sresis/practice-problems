"""Return the max containers that you can purchase.

For example::

   >>> max_containers(1, ['4 1 2'])
   7
   >>> max_containers(3, ['10 2 5', '12 4 4', '6 2 2'])
   6
   3
   5
   >>> max_containers(2, ['8 4 2', '7 2 3'])
   3
   4
"""


def max_containers(n, scenarios):
    """Returns the max containers you can purchase."""
    # get the budget, cost and empties to get a free one
    for scenario in scenarios:
        list_format = scenario.split(' ')
    
        budget = int(list_format[0])
        cost = int(list_format[1])
        empty_conversion = int(list_format[2])
        # how to handle remainders
        # purchcase as many as you can
        num_purchased = int(budget / cost)
        empties = budget % cost
        # loop until no more to return
        # while to_return > empty_conversion
        to_return = num_purchased + empties

        while to_return >= empty_conversion:
            addtl_purchase = int(to_return / empty_conversion)
            num_purchased += addtl_purchase
            unused = to_return % empty_conversion
            to_return = addtl_purchase + unused
        print(num_purchased)

 
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")