def answer(s):
    passes = 0
    for i in range(0, len(s)):
        if s[i] == ">":
            passes += s[i:len(s)].count("<")
    return passes*2
