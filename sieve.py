LIMIT = 10000
is_prime = [True] * (LIMIT + 1)

for n in range(2, LIMIT):
    if is_prime[n]:  # n is prime
        print(n, end=" ")
        for m in range(2 * n, LIMIT + 1, n):
            is_prime[m] = False
