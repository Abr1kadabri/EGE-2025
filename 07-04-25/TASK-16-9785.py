from functools import lru_cache

@lru_cache(None)
def F(n):
    if n < 7:
        return 7
    if n >= 7:
        return n + 1 + F(n-2)

for i in range(10, 2026):
    F(i)

print(F(2024) - F(2020))
