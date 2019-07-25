def myAtoi(str: str) -> int:
    numFound = False
    ref = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
    res = 0
    neg = False
    for s in str:
        if not numFound and s != ' ':
                if s == '-':
                    numFound = True
                    neg = True
                    continue
                elif s not in ref:
                    return 0
                else:
                    numFound = True
        if numFound:
            if s in ref:
                res = res*10 + ref[s]
            else:
                break
    if neg:
        res = -res
    if res < -pow(2, 31):
        return -pow(2, 31)
    elif res > pow(2, 31) -1:
        return pow(2, 31) -1
    else:
        return res 

print(myAtoi("    -42"))
print(myAtoi('4193 with words'))
print(myAtoi('words and 987'))