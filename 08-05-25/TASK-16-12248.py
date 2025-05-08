from functools import lru_cache

@lru_cache(None)
def F(n):
    if n <= 3:
        return n
    if n > 3:
        return (n + 3) * F(n-2)

for i in range(10, 2029):
    F(i)

print(F(2028) / F(2024))


