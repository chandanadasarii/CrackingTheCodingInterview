
def palinPermutation(string):
    charcnt = dict()
    oddCounter = 0

    for c in string:
        if c in charcnt:
            charcnt[c] += 1
        else:
            charcnt[c] = 1

        if charcnt[c] % 2 == 0:
            oddCounter -= 1
        else:
            oddCounter += 1

    if oddCounter > 1:
        return False
    else:
        return True

print(palinPermutation("tactcoa"))
print(palinPermutation("toioot"))


    