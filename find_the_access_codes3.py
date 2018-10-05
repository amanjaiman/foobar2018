def answer(l):
    triples = 0
    numOfDoubles = [0]*len(l)

    for i in range(1, len(l)-1):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                numOfDoubles[i] += 1

    for i in range(2, len(l)):
        for j in range(1, i):
            if l[i] % l[j] == 0:
                triples += numOfDoubles[j]
    
    return triples

print(answer([1, 2, 3, 4, 5, 6]))
