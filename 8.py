n, m = map(int, input().split())
print((((n + 1) - ((n + 1) % m)) // m)) # n + 1, т.к. Буратино мы тоже считаем