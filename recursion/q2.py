def print_to_5(n=1):
    if n > 5:
        return
    print(n)
    print_to_5(n+1)

print_to_5()