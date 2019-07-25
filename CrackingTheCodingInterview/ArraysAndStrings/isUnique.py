# Assume that string is ASCII
def isUnique(st):
    charset =  [False]*128

    if len(st) == 0:
        return True

    if len(st) > 128:
        return False

    for c in st:
        if charset[ord(c)] == True:
            return False
        else:
            charset[ord(c)] = True

    return True

print(isUnique("Chandana"))
print(isUnique("Sandy"))