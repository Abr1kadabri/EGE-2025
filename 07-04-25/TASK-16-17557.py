from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n-1)

for i in range(10, 2026):
    F(i)

print((F(2024) // 16 - F(2023)) // F(2022))