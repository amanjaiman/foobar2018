def answer(l, t):
    ans = []
    for i in xrange(len(l)):
        s = 0
        j = i+1
        prevSub = []
        while s < t:
            substr = l[i:j]
            if substr != prevSub:
                prevSub = substr
                s = sum(substr)
                j += 1
            else:
                break
        if s == t:
            ans += [[i, j-2]]
    if len(ans) == 0:
        return [-1, 1]
    return min(ans)

print(answer([4, 3, 10, 2, 8], 12))
print(answer([1, 2, 3, 4], 15))
print(answer([1,2,3,5,6],6))
print(answer([1, 2, 3],1))
print(answer([1,2,3],4))
print(answer([5,5,3,2,1],10))
print(answer([1,2,3],0))
