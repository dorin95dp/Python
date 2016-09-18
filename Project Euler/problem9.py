from math import sqrt
from time import time
from functools import reduce

def generateSquares(maxim):
    array = []
    for i in range(1,maxim+1):
        array.append(i)
        
    return list(map(lambda x: x**2, array))
    
def getTriplets(squares):
    triplets = []
    for index, c in enumerate(squares):
        for indexB in range(index):
            for indexA in range(indexB):
                if squares[indexA] + squares[indexB] == c:
                    squaredTriplet = (squares[indexA], squares[indexB], c)
                    triplets.append(tuple(map(lambda x: int(sqrt(x)),
                                              squaredTriplet))) 

    return triplets

def getTripletWithSum1000(triplets):
    array = list(filter(lambda triplet: sum(list(triplet)) == 1000, triplets))
    
    return array[0] if len(array) != 0 else 0

def getTriplet(maxim):
    squares = generateSquares(maxim)
    triplets = getTriplets(squares)
    
    return getTripletWithSum1000(triplets)

def getTripletProduct(maxim):
    triplet = getTriplet(maxim)
    if triplet != 0:
        return reduce(lambda a, b: a*b, triplet)
    return 0
    
if __name__ == '__main__':    
    initialTime = time()
    maximum = 1000
    tripletProduct = getTripletProduct(maximum)
    executionTime = time() - initialTime
    print("product of the triplet with sum 1000 = %d"
          %(tripletProduct)) if tripletProduct != 0 else print(
                             "Too small maximum number, increase it")
    print("Execution time = %r s"%(executionTime))

