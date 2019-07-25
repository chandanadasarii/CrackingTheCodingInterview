from collections import Counter

def checkPermutation(s, t):
    
    if len(s) != len(t):
        return False

    charcnt = Counter()

    for c in s:
        charcnt[c] += 1
    
    for c in t:
        if charcnt[c] == 0:
            return False
        charcnt[c] -= 1

    return True


print(checkPermutation("sandy", "yands"))
print(checkPermutation("sandy", "yanssds"))
print(checkPermutation("", ""))