# Цикл for

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    if i == 1:
        continue
    if i == 2:
        is_prime = False
    for k in range(2,i):
        if (i % k) == 0:
            is_prime = True
            break
        else:
            is_prime = False
    if is_prime :
        not_primes.append(i)
    else:
        primes.append(i)
print(primes)
print(not_primes)

