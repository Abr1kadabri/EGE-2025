from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 3:
        return 3
    if n >= 3:
        return 2 * n + 5 + F(n-2)

for i in range(10, 3029):
    F(i)

print(F(3027) - F(3023))