def get_even_fib_sum(num):
    """Returns the sum of all even fibs up to a giben val."""

    # get all fibs up to a given sum
    # take that list and only sum the even values

    fib_nums = [1, 2]
    i = 2
    current_num = 2
    while current_num < num:
        fib_nums.append(fib_nums[i-2] + fib_nums[i-1])
        current_num += fib_nums[i-2] + fib_nums[i-1]
        i += 1
        print(current_num)
        print(fib_nums)

    print(fib_nums)
    
    even_sum = 0
    for num in fib_nums:
        if num % 2 == 0:
            even_sum += num
    return even_sum

print(get_even_fib_sum(4000000))