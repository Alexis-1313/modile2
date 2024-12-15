numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    k=int(i)
    if k==1:
        continue
    elif k==2 or k==3:
        primes.append(k)
        continue
    for j in range(2,k-1):
        if k%j==0:
            not_primes.append(k)
            break
    if k%j>0:
        primes.append(k)
print(primes)
print(not_primes)