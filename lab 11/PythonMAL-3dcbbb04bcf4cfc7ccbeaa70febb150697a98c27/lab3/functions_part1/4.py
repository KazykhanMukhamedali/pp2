def prime(num):
    if num == 0:
        return True
    else:
        for i in range(2, num//2+1):
            if num%i==0:
                return False
    return True
def filter_prime(lst):
    primes = []
    for i in range(len(lst)):
        if prime(lst[i]):
            primes.append(lst[i])
    return primes
print(filter_prime([1,2,3,4,5,6,7,8,9,10]))