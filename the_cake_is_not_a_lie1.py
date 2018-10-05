def answer(s):
    worstCase = 1
    sArr = list(s)
    max_len = len(sArr)/2
    for i in range(1, max_len+1):
        x = sArr[0:i]
        failed = False
        for j in range(0, len(sArr)//len(x)):
            #print("X: ",x)
            if sArr[j*len(x):(j*len(x)+len(x))] != x:
                #print(sArr[j*len(x):(j*len(x)+len(x))])
                failed = True
        if failed == False:
            if len(sArr)*1.0/len(x) != len(sArr)//len(x):
                continue
            else:
                return len(sArr)/len(x)
    return worstCase

print(answer("abccbaabccba"))
print(answer("abcabcabcabc"))
print(answer("abcabcabcd"))
print(answer("ababcababcababcababc"))
