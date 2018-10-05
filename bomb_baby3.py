def answer(M, F):
    m = int(M)
    f = int(F)
    c = 0
    while m > 0 and f > 0:
        if m == 1 or f == 1:
            arr = [m, f]
            c += arr[(arr.index(1)+1)%2]-1
            return str(c)
        if m < f:
            c += f/m
            f = f%m
        else:
            c += m/f
            m = m%f
            
    return "impossible"
