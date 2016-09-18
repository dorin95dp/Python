from time import time
from functools import reduce

def squares():
    i = 1
    while i < 1000:
        yield (i,i**2)
        i += 1

initialTime = time()
triplets = []
prev = []
seen = {}
found = False

for (i,isq) in squares():
    for (j, jsq) in prev:
        k = seen.get(isq-jsq)
        if not k: continue
        if i + j + k == 1000:
            triplets.append((j, k, i))
            found = True
            break
    if found: break
    prev.append((i,isq))
    seen[isq] = i


triplet = triplets[0]
product = reduce(lambda x, y: x*y, triplet)
executionTime = time() - initialTime
print("Product = %d"%(product))
print("Execution time = %r"%(executionTime))
