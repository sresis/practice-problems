import math
def get_all_primes(num):
    """Returns all primes up to a given number."""
    # store primes in primes list
    primes_list = []
    if num > 2:
        primes_list.append(2)
    # if num is  divisible by any number in prime, it is not prime
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        divis_count = 0
        for prime in primes_list:
            if i % prime == 0:
                divis_count += 1
                break
        if divis_count == 0:
            primes_list.append(i)
    return primes_list


def largest_prime_factor(num):
    """Return the largest prime factor for a given num."""
    primes_list = get_all_primes(num)
    primes_list.sort(reverse=True)
    print(primes_list)
    for prime in primes_list:
        if num % prime == 0:
            return prime
        

print(largest_prime_factor(600851475143))