from math import floor, sqrt
from time import time
initialTime = time()
def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    for number in range(2,int(sqrt(n))+1):
        if n % number == 0:
            return False
    return True

def generatePrimes(n):
    primes = []
    for number in range(2, n):
        if isPrime(number):
            primes.append(number)

    return primes

def isPrimeInPrimes(primes, number):
    for prime in primes:
        if number % prime == 0:
            return False

    return True

def getPrime(n):
    primes = []
    index = 1
    primes = generatePrimes(n)
    while len(primes) != n:
        number = n + index
        if isPrimeInPrimes(primes, number):
            primes.append(number)
            
        index +=1 
    return primes[n-1]

index = 10001
prime = getPrime(index)
print("The %dth prime = %d"%(index,prime))
executionTime = time() - initialTime
print("The execution time = %f s"%(executionTime))


