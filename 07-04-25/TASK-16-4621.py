def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * F(n-2) - F(n-1) + 2
    if n > 2
