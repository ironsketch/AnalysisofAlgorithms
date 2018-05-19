import random

A = []

while len(A) < 1000001:
    randomNumber = random.randint(0, 1000000001)
    if randomNumber not in A:
        A.append(randomNumber)

print A
