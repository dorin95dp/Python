from time import time
from math import sqrt

def isPrime(n):
        if n == 2:
                return 1
        elif n % 2 == 0:
                return 0
        i = 3
        range = int(sqrt(n)) + 1
        while i < range:
                if( n % i == 0):
                    return 0
                i += 1
        return 1

def getPrime(index):
    number = 1
    resultPlus2 = 3  #verifying only on odd positions
    while number < index:
        if isPrime(resultPlus2):
            number += 1
        resultPlus2 += 2

    return resultPlus2 - 2

if __name__ == '__main__':
        initialTime = time()
        index = 10001
        NthPrime = getPrime(index)
        print ("The %dth prime = %d"%(index, NthPrime))

        finalTime = time()
        executionTime = finalTime - initialTime
        print ("Execution time = %f s"%(executionTime))
